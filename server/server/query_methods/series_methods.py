from server import db
from server.models.show_series import ShowSeries, ShowSeriesURL
from server.utils.generic_utils import remove_substrings_in_string

def add_series(title, description, parent_id = None):

    new_series = ShowSeries(title=title, description=description, parent_id=parent_id)
    try:
        db.session.add(new_series)
        db.session.flush()
        # db.session.commit()
        print('new series added')
        return new_series
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def add_series_url(show_series_id, tab_url):
    new_series_url = ShowSeriesURL(show_series_id=show_series_id, url=tab_url)
    try:
        db.session.add(new_series_url)
        db.session.flush()
        # db.sessions.commit()
        print('new series url added')
        return new_series_url
    except Exception as e:
        print(e)
        db.session.rollback()
        return False


def generate_title_from_url(url):

    if '.crunchyroll.' in url:
        url = remove_substrings_in_string(url, ['http://','https://'])
        split_url = url.split('/')
        return split_url[1]
    else:
        return url[0:99]

def generate_episode_from_url(url):

    if '.crunchyroll.' in url:
        url = remove_substrings_in_string(url, ['http://','https://'])
        split_url = url.split('/')
        return split_url[2]
    else:
        return url[0:99]
