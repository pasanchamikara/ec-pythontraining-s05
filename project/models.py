from sqlalchemy.orm import sessionmaker
from ..config.dbconfig import engine

Session = sessionmaker(bind = engine)
session = Session()

from ..project import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, fname, email):
        self.fname = fname
        self.email = email
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
