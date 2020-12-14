from sqlalchemy.dialects.postgresql import TIMESTAMP

from db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inserted_at = db.Column(TIMESTAMP(precision=0), default=db.func.now(), nullable=False)
    roles = db.Column(db.ARRAY(db.String(255)), default=['user'], nullable=False)

    notes = db.relationship('Notes', lazy='select', cascade="all,delete")

    @classmethod
    def get(cls, p_key):
        return cls.query.get(p_key)

    @classmethod
    def create(cls, p_key):
        entity = cls(id=p_key)
        db.session.add(entity)
        db.session.commit()
        return entity

    @classmethod
    def upsert(cls, p_key):
        entity = cls.get(p_key)
        if entity is None:
            return cls.create(p_key)
        return entity

    def delete(self):
        db.session.delete(self)
        db.session.commit()
