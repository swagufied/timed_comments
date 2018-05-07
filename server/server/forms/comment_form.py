from wtforms import Form, StringField, IntegerField, validators
from server.forms.validators import *

class CommentForm(Form):
    comment_time = IntegerField()
    content      = StringField()
    tab_url      = StringField('tab_url', [accepted_URL_hosts])
