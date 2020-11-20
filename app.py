from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.notes import NotesController


@app.route('/', methods=['GET'])
def notes_list():
    return NotesController.get()


@app.route('/form', methods=['GET'])
def notes_form():
    return render_template('form.html', title='New note')


@app.route('/notes', methods=['POST'])
def create_note():
    return NotesController.post()


@app.route('/notes/<int:p_key>/delete', methods=['GET'])
def delete_note(p_key):
    return NotesController.delete(p_key)


if __name__ == '__main__':
    app.run()
