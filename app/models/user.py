
from app import db, create_app
from app.services.hash_password import encrypt_password, check_password


class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = encrypt_password(password)

    def login(self, password):
        if check_password(self.password, password):
            return "You are logged in"








