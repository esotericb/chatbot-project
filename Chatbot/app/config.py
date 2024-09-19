class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root%40esoteric90@localhost/water_utility_db'
    SQLALCHEMY_TRACK_MODOFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'