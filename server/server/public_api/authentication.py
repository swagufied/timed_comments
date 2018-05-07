from flask import
from jwt import




@app.route('/login')
def login():

    token = jwt.encode({'user': username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
