import os

SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL') or 'postgres://postgres:2dover3d@localhost/live_comments'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(32)
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'qwerty'
