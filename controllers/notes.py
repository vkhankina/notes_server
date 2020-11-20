from flask import render_template, request, redirect, url_for
from flask.views import MethodView

from models.notes import Notes


class NotesController(MethodView):
    @staticmethod
    def get():
        return render_template('list.html', title='Notes', notes=Notes.list())

    @staticmethod
    def post():
        data = request.form
        Notes.create(name=data['name'], description=data['description'])
        return redirect(url_for('notes_list'))

    @staticmethod
    def delete(p_key):
        Notes.get(p_key).delete()
        return redirect(url_for('notes_list'))
