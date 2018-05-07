from flask import Blueprint

from flask_admin.contrib import sqla
from server import db, admin

from server.models.user import User, Role
from server.models.show_series import ShowSeries, ShowSeriesURL
from server.models.timed_comment import TimedComment


from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils

mod = Blueprint('general', __name__)

@mod.route('/')
def init():
    return 'live comment home'
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(ShowSeries, db.session))
admin.add_view(ModelView(ShowSeriesURL, db.session))
admin.add_view(ModelView(TimedComment, db.session))


# @mod.route('/', methods=['GET'])
# def init():
#
#
#
#
#
#     return 'this is live comment home'
