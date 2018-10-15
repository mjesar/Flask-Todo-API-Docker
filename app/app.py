import os
import time

from flask import Flask, jsonify, make_response

#importing database model class
from databaseModel import db

#importing routes with blueprints
from Routes.get_all import getall_api
from Routes.get_one import getone_api
from Routes.post import post_api
from Routes.delete import delete_api
from Routes.update_done import update_one_api
from Routes.update_text import update_text_api



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db_path = os.path.join(os.path.dirname(__file__), 'database.db')
# db_uri = 'sqlite:///{}'.format(db_path)
# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aliali@127.0.0.1:5432/todo'

DBUSER = 'postgres'
DBPASS = 'aliali'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'todo'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
db.init_app(app)


#Register blueprints
app.register_blueprint(getall_api)
app.register_blueprint(getone_api)
app.register_blueprint(post_api)
app.register_blueprint(update_one_api)
app.register_blueprint(delete_api)
app.register_blueprint(update_text_api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')