from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import uuid
import datetime

db = SQLAlchemy()

class dbTemplate():
    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def as_dict(self):
        return {col.name: str(getattr(self, col.name)) for col in self.__table__.columns}
        
class Users(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    uid = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100))
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, nickname, password, email, admin):
        self.username = username
        self.uid = str(uuid.uuid4())
        self.password = generate_password_hash(password, method='sha256')
        self.email = email
        self.admin = admin

    def save(self):
        db.session.add(self)
        db.session.commit()

    def as_dict(self):
        return {col.name: str(getattr(self, col.name)) for col in self.__table__.columns}
    
    def update(self, data):
        for key in data:
            if key == 'password':
                setattr(self, key, generate_password_hash(data[key], method='sha256'))
            else:
                setattr(self, key, data[key])
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

class Bulletin(db.Model, dbTemplate):
    postId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    author = db.Column(db.String(100))
    tag = db.Column(db.String(100))
    date = db.Column(db.Date)

    def __init__(self, title, content, author, tag):
        self.title = title
        self.content = content
        self.author = author
        self.tag = tag
        self.date = datetime.datetime.now()

    def update(self, data, author):
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'author', author)
        setattr(self, 'date', datetime.datetime.now())
        db.session.commit()
