# timed_comments

### notes
# currently only runs locally and on crunchyroll. other sites under experimentation.

### requirements
* must install [the crunchyroll html5er](https://chrome.google.com/webstore/detail/crunchyroll-html5/ihegfgnkffeibpmnajnoiemkcmlbmhmi)
* must have postgres and flask. change database location in server/dev_config.py accordingly
* you can go to localhost://5000/admin to easily see all changes made to db.

### to run
* make sure db configuration is correct. (also make sure you have an empty database created for this app)
* run server/db_create.py.
* run server/run.py to run the server. and link the extension folder to dev mode extensions
* go to crunchyroll and add a comment
