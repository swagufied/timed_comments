from server import db
from datetime import datetime
from flask_security import UserMixin, RoleMixin


# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('Role.id')))

class Role(db.Model, RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return self.name



class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id            = db.Column(db.Integer, primary_key = True)
    username      = db.Column(db.String(30))
    email         = db.Column(db.String(255))
    password      = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime(), default = datetime.utcnow)
    last_login    = db.Column(db.DateTime(), default = datetime.utcnow)
    is_deleted    = db.Column(db.Boolean(), default = False)
    is_validated  = db.Column(db.Boolean())

    roles    = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    comments = db.relationship('TimedComment', backref = 'user', lazy='dynamic')

    def __init__(self, username, email, password, **kwargs):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return self.username

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self): # line 37
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username
