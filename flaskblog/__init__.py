from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
#from flask_admin import Admin


db = SQLAlchemy() # A db instance
bcrypt = Bcrypt() # For hashing passwords
login_manager = LoginManager() # Handles all the DB login sessions in the background
login_manager.login_view = 'users.login' # Tells the flask_login manager where our login route is located 
login_manager.login_message_category = 'info' # Uses bootstrap's 'info' class to beautify login message

mail = Mail()


#admin = Admin(app)
#app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Imported here to avoid circular import error(These are the blueprints import)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    
    return app
