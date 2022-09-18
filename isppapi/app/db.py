from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModelMixin:
    def save():
        db.session.add(self)
        db.session.commit()
    
    def delete():
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()