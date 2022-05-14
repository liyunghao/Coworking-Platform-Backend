from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import uuid

db = SQLAlchemy()

class Users(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    uid = db.Column(db.String(100))
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100))
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, email, admin):
        self.username = username
        self.uid = str(uuid.uuid4())
        self.password = generate_password_hash(password, method='sha256')
        self.email = email
        self.admin = admin

    def save(self):
        db.session.add(self)
        db.session.commit()
