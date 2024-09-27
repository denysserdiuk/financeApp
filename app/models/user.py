
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


if __name__=="__main__":
    app = create_app()

    with app.app_context():
        # Check if the user already exists
        if not User.query.filter_by(username="test_user").first():
            user = User("denystest", "email@test.com", "password")
            db.session.add(user)
            db.session.commit()
            print("Test user created.")
        else:
            print("User already exists.")





