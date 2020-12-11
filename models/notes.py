from sqlalchemy.dialects.postgresql import TIMESTAMP
from marshmallow import Schema, fields, validate

from db import db


class NotesSchema(Schema):
    id = fields.Int(dump_only=True)
    inserted_at = fields.DateTime(dump_only=True, format='iso')
    name = fields.Str(validate=validate.Length(max=255), required=True)
    description = fields.Str(required=True)
    user_id = fields.Int(dump_only=True)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    inserted_at = db.Column(TIMESTAMP(precision=0), default=db.func.now(), nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('Users', lazy='select')

    schema = NotesSchema

    @classmethod
    def list(cls, user):
        return user.notes

    @classmethod
    def create(cls, user, attrs):
        data = cls.schema().load(attrs)
        entity = cls(**data)
        entity.user_id = user.id
        db.session.add(entity)
        db.session.commit()
        return entity

    @classmethod
    def get(cls, p_key):
        return cls.query.get(p_key)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
