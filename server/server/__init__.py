from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('dev_config')

db = SQLAlchemy(app)
CORS(app)
admin = Admin(app)

from server.models.user import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from server.public_api import comments
from server.views import general
app.register_blueprint(comments.mod)
app.register_blueprint(general.mod)




@app.before_first_request
def before_first_request():

    # Create any database tables that don't exist yet.
    db.create_all()

    # Create the Roles "admin" and "end-user" -- unless they already exist
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')
    user_datastore.find_or_create_role(name='master-admin', description='Master Administrator')


    # Create two Users for testing purposes -- unless they already exists.
    # In each case, use Flask-Security utility function to encrypt the password.
    # encrypted_password = utils.encrypt_password('password')
    encrypted_password = 'sss'
    if not user_datastore.get_user('someone@example.com'):
        user_datastore.create_user(username="user",  email='someone@example.com', password=encrypted_password)
    if not user_datastore.get_user('admin@example.com'):
        user_datastore.create_user(username="admin", email='admin@example.com', password=encrypted_password)

    # Commit any database changes; the User and Roles must exist before we can add a Role to the User
    db.session.commit()

    # Give one User has the "end-user" role, while the other has the "admin" role. (This will have no effect if the
    # Users already have these Roles.) Again, commit any database changes.
    user_datastore.add_role_to_user('someone@example.com', 'end-user')
    user_datastore.add_role_to_user('admin@example.com', 'master-admin')
    db.session.commit()
