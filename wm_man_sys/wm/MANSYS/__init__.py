from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import smtplib

app=Flask(__name__)

app.config["DEBUG"]=True
app.config["SECRET_KEY"]='03e1702b848810d119df16a470a26bbb'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = email
# app.config['MAIL_PASSWORD'] = password
# app.config['MAIL_USE_TLS'] = True
# # app.config['MAIL_USE_SSL'] = True

# S = smtplib.SMTP('smtp.gmail.com', 587)



mail = Mail(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from MANSYS import routes