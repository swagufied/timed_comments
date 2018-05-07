from server import db
from datetime import datetime

class ShowSeries(db.Model):
    __tablename__ = 'ShowSeries'

    id          = db.Column(db.Integer, primary_key = True)
    site_id     = db.Column(db.String(100))
    title       = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    parent_id   = db.Column(db.Integer, db.ForeignKey('ShowSeries.id'))
    add_date    = db.Column(db.DateTime(), default = datetime.utcnow)
    modify_date = db.Column(db.DateTime(), onupdate = datetime.utcnow)


    comments    = db.relationship('TimedComment', backref = 'show_series', lazy='dynamic')
    urls        = db.relationship('ShowSeriesURL', backref = 'show_series', lazy='dynamic')
    children    = db.relationship("ShowSeries", backref = db.backref('parent',remote_side = id))

    def __init__(self, title, **kwargs):
        self.title = title

        columns = ShowSeries.__table__.columns
        for c in columns:
            if c.key in kwargs:
                setattr(self,c.key, kwargs[c.key])



class ShowSeriesURL(db.Model):
    __tablename__ = 'ShowSeriesURL'

    id             = db.Column(db.Integer, primary_key = True)
    show_series_id = db.Column(db.Integer, db.ForeignKey('ShowSeries.id'))
    url            = db.Column(db.String(1000), unique = True)

    def __init__(self, show_series_id, url):
        self.show_series_id = show_series_id
        self.url = url
