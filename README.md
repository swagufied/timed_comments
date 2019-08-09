# Timed Comments
  A test application that displays comments on a video screen based on the timestamp associated with the comment, similar to the timed comments found on Viki's videos (Ex. a comment designated to appear at 0:05 would appear on the video when the video's progress reaches 0:05). Comments made on a certain episode of a show would be able to be displayed on all sites streaming the same episode. This is made possible by storing and managing the comments on a dedicated server. 

### Notes
* The prototype only runs locally and on crunchyroll. It should be more broadly applicable to any video that is played using the html5 video element (Ex. Youtube, Hulu, Netflix, etc.)

### Requirements
* Must install [the crunchyroll html5er](https://chrome.google.com/webstore/detail/crunchyroll-html5/ihegfgnkffeibpmnajnoiemkcmlbmhmi). This is because at the moment, html5 players for crunchyroll are not publicly available.
* Postgresql, flask, flask-admin, flask-cors, and flask-sqlalchemy, python3
* Change database location and credentials in server/dev_config.py to match its location on your computer.


### To run
* Make sure the db configuration in "server/dev_config.py" is correct.
* Run server/db_create.py to initialize tables.
* Run server/run.py to run the server.
* Link the extension folder to Google chrome's developer mode extensions
* Go to crunchyroll and add a comment through the extension button at the top of your browser.
* You can go to localhost:5000/admin to easily see all changes made to db.
