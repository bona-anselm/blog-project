from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from flask_admin import Admin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd7ca5984452ea5113592d55a53efde5c' # App secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # DB connection
db = SQLAlchemy(app) # A db instance
bcrypt = Bcrypt(app) # For hashing passwords
login_manager = LoginManager(app) # Handles all the DB login sessions in the background
login_manager.login_view = 'login' # Tells the flask_login extension where our login route is located 
login_manager.login_message_category = 'info' # Uses bootstrap's 'info' class to beautify login message
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bona.anselm@gmail.com'
app.config['MAIL_PASSWORD'] = 'qkoveexicuddcnsp'
mail = Mail(app)

#admin = Admin(app)
#app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


from flaskblog import routes # imported here to avoid circular import error

with app.app_context():
    db.create_all()