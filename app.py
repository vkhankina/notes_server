from flask import Flask
from flask_cors import CORS

from blueprints.notes import notes_bp
from blueprints.users import users_bp
from db import db, migrate
from config import config

app = Flask(__name__)
CORS(app)
app.config.from_object(config)

v1_prefix = '/api/v1'
app.register_blueprint(notes_bp, url_prefix=f'{v1_prefix}/notes')
app.register_blueprint(users_bp, url_prefix=f'{v1_prefix}/users')


@app.route('/')
def index():
    return 'OK'


db.init_app(app)
migrate.init_app(app, db)

if __name__ == '__main__':
    app.run()
