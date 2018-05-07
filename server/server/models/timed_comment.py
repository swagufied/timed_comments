from server import db
from datetime import datetime

timed_comment_likes = db.Table('timed_comment_likes',
    db.Column('user_id',db.Integer(),db.ForeignKey('User.id')),
    db.Column('comment_id',db.Integer(),db.ForeignKey('TimedComment.id')),
    db.UniqueConstraint('user_id', 'comment_id', name='like_constraint')
)

class TimedComment(db.Model):
    __tablename__ = 'TimedComment'

    id             = db.Column(db.Integer, primary_key = True)
    show_series_id = db.Column(db.Integer, db.ForeignKey('ShowSeries.id'))
    user_id        = db.Column(db.Integer, db.ForeignKey('User.id'))
    comment_time   = db.Column(db.Integer)
    is_reported    = db.Column(db.Boolean())

    content        = db.Column(db.String(200))
    post_date      = db.Column(db.DateTime(), default = datetime.utcnow)
    parent_id      = db.Column(db.Integer, db.ForeignKey('TimedComment.id'))

    liked_by = db.relationship('User', secondary=timed_comment_likes, backref=db.backref('liked_timed_comments',lazy='dynamic'), lazy='dynamic')
    children = db.relationship("TimedComment", backref = db.backref('parent',remote_side = id))

    def __init__(self, show_series_id, user_id, comment_time, content, parent_id):
        self.show_series_id = show_series_id
        self.user_id = user_id
        self.comment_time = comment_time
        self.content = content
        self.parent_id = parent_id

    """
    manage comment likes
    """
    def add_like(self, user):
        if not self.is_liked_by_user(user):
            self.liked_by.append(user)

    def remove_like(self, user):
        if self.is_liked_by_user(user):
            self.liked_by.remove(user)

    def is_liked_by_user(self, user):
        return self.liked_by.filter(User.id == user.id).count() > 0
