from sqlalchemy.dialects.postgresql import TIMESTAMP

from app import db


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    inserted_at = db.Column(TIMESTAMP(precision=0), default=db.func.now(), nullable=False)

    @classmethod
    def list(cls):
        return cls.query.all()

    @classmethod
    def create(cls, name=name, description=description):
        note = cls(name=name, description=description)
        db.session.add(note)
        db.session.commit()
        return note

    @classmethod
    def get(cls, p_key):
        return cls.query.get(p_key)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
