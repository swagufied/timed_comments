from flask import Blueprint, jsonify, request, abort
from server.constants import CommentTable

from server.models.show_series import ShowSeriesURL
from server.models.timed_comment import TimedComment

from server.utils.comment_utils import *
import server.query_methods.comment_methods as CommentMethods
import server.query_methods.series_methods as SeriesMethods

from server.forms.comment_form import CommentForm
from server.test_data import *
from server import db

mod = Blueprint('comments', __name__)


@mod.route('/get-timed-comments', methods=['GET'])
def get_comments():

	try:
		url = request.args['url']
	except:
		abort(400)

	print('request from: {}'.format(url))
	show_series_url = ShowSeriesURL.query.filter_by(url = url).first()
	if show_series_url:
		comments = TimedComment.query.filter_by(show_series_id = show_series_url.show_series.id).all()

		comments = organize_comments_by_time(comments)
		return jsonify({'success': True, 'timed_comments':comments})
	else:
		return jsonify({'success':False})

@mod.route('/add-timed-comment', methods=['POST'])
def add_timed_comment():
	print('adding comment')
	print(request.form)

	form = CommentForm(request.form)
	if form.validate():

		tab_url = form.tab_url.data
		comment_time = form.comment_time.data
		content = form.content.data
		print(tab_url, comment_time, content)
		try:
			if not CommentMethods.add_comment(tab_url, comment_time, content):
				print('jheoirhwe')
				title = SeriesMethods.generate_title_from_url(tab_url)
				print('title added')
				new_series = SeriesMethods.add_series(title, "")
				print('new series added: {}'.format(new_series))
				episode = SeriesMethods.generate_episode_from_url(tab_url)
				print('episode: {}'.format(episode))
				new_episode = SeriesMethods.add_series(episode, "", parent_id=new_series.id)
				print('new episode')
				SeriesMethods.add_series_url(new_series.id, tab_url)
				if not CommentMethods.add_comment(tab_url, comment_time, content):
					print('failed 3')
					return jsonify({'success':False})

			db.session.commit()
			return jsonify({'success':True})

		except Exception as e:
			print(e)
			db.session.rollback()
	if form.errors:
		print(form.errors)
		return jsonify({'success':False, 'form_errors':form.errors})
	else:
		return jsonify({'success':False})
