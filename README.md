# timed_comments
* A small application that tests displaying comments on a video screen based on the timestamp associated with the comment. Ex. a comment designated to appear at 0:05 would appear on the video when the video's progress reaches 0:05. 

### notes
* only runs locally and on crunchyroll. This is a prototype. It should be more broadly applicable to any video that is played using the html5 video element

### requirements
* Must install [the crunchyroll html5er](https://chrome.google.com/webstore/detail/crunchyroll-html5/ihegfgnkffeibpmnajnoiemkcmlbmhmi).
* Must have postgresql, flask, flask-admin, flask-cors, and flask-sqlalchemy installed.
* Change database location and credentials in server/dev_config.py to match its location on your computer.


### to run
* Make sure the db configuration is correct. (also make sure you have an empty database created for this app)
* run server/db_create.py.
* run server/run.py to run the server.
* Link the extension folder to Google chrome's developer mode extensions
* Go to crunchyroll and add a comment through the extension button at the top of your browser.
* You can go to localhost:5000/admin to easily see all changes made to db.
