from server import db
from server.models.timed_comment import TimedComment
from server.models.show_series import ShowSeries, ShowSeriesURL

def get_comments(request):

    id = 1

    series = ShowSeries.get(id)
    serialize_query(series.comments)
    TimedComment.query.filter_by()

def add_comment(tab_url, comment_time, content):

    series_url = ShowSeriesURL.query.filter_by(url = tab_url).first()
    print(series_url)
    if series_url:
        new_comment = TimedComment(
            show_series_id=series_url.show_series.id,
            user_id=1,
            comment_time=comment_time,
            content=content,
            parent_id=series_url.show_series_id
            )
        try:
            db.session.add(new_comment)
            db.session.flush()
            # db.session.commit()
            print('comment added')
            return new_comment
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False
