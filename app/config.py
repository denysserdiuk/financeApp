import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', 3306)
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_NAME', 'your_database_name')
    DB_CHARSET = os.getenv('DB_CHARSET', 'utf8mb4')
    DB_COLLATION = os.getenv('DB_COLLATION', 'utf8mb4_general_ci')

    # SQLAlchemy Database URI (if using Flask-SQLAlchemy)
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        f"?charset={DB_CHARSET}&collation={DB_COLLATION}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False