from flask import Flask
from flask_session import Session
import mysql.connector

# workshop_db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='1234',
#     database='database_workshop'
# )

workshop_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='database_workshop',
    port='3307',
    auth_plugin='mysql_native_password'

)

workshop_cursor = workshop_db.cursor()

app = Flask(__name__)

app.config['SECRET_KEY'] = '2136cdc56a8ad364b251f9bb645d1e56'  # Create S.K. for anti csrf attack
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

from application.moduls.authorization.routs import authorization
from application.moduls.posts.routs import posts
from application.moduls.main.routs import main
from application.moduls.upload.routs import upload
from application.moduls.search.routs import search

app.register_blueprint(authorization)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(upload)
app.register_blueprint(search)
