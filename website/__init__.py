from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv, getcwd
from flask_login import LoginManager
from dotenv import load_dotenv

#object we use to add to database etc
db = SQLAlchemy()
DB_name = "database.db"

load_dotenv('./instance/.env')
print(getenv('SECRET'))
print(getcwd())

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET')
    # Database stored in below location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_name}'
    # Take database we have and use it below
    db.init_app(app)

    from .views import views
    from .auth import auth

    # how to register the prefix
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/') 

    # Used to ensure models file is ran, to define classes
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # tells flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        # its going to look for primary key
        return User.query.get(int(id))

    return app

# Checks if db exists, if not it doesnt overried
def create_database(app):
    if not path.exists('website/ + DB_NAME'):
        with app.app_context():
            db.create_all()
        print('Created Database!')