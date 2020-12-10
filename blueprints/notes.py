from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from middlewares.auth import get_user
from models.notes import Notes

notes_bp = Blueprint('notes', __name__)


@notes_bp.route('/', methods=['GET'])
@get_user
def get():
    notes = Notes.list()
    data = Notes.schema(many=True).dump(notes)
    return {'data': data}


@notes_bp.route('/', methods=['POST'])
@get_user
def create():
    json_data = request.get_json()
    if not json_data:
        return {'error': "No input data provided"}, 400
    try:
        entity = Notes.create(json_data)
        data = entity.schema().dump(entity)
        return {'data': data}, 201
    except ValidationError as err:
        return {'error': err.messages}, 422


@notes_bp.route('/<int:p_key>/', methods=['DELETE'])
@get_user
def delete(p_key):
    Notes.get(p_key).delete()
    return '', 204
