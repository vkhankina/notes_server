from flask import Flask, render_template

from db import db, migrate
from config import config
from controllers.notes import NotesController

app = Flask(__name__)
app.config.from_object(config)


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


db.init_app(app)
migrate.init_app(app, db)

if __name__ == '__main__':
    app.run()
