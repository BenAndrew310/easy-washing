from MANSYS import db, login_manager
from flask_login import UserMixin
from datetime import date

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

'''
Server[n] Text column format:
2020-12-05;2020-12-06;2020-12-07;....
01234567890123456789012345678901
'''

class Server1(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Text,nullable=False,default="")
	t2 = db.Column(db.Text,nullable=False,default="")
	t3 = db.Column(db.Text,nullable=False,default="")
	t4 = db.Column(db.Text,nullable=False,default="")
	t5 = db.Column(db.Text,nullable=False,default="")
	t6 = db.Column(db.Text,nullable=False,default="")
	t7 = db.Column(db.Text,nullable=False,default="")
	t8 = db.Column(db.Text,nullable=False,default="")
	t9 = db.Column(db.Text,nullable=False,default="")
	t10 = db.Column(db.Text,nullable=False,default="")
	t11 = db.Column(db.Text,nullable=False,default="")
	t12 = db.Column(db.Text,nullable=False,default="")
	t13 = db.Column(db.Text,nullable=False,default="")
	t14 = db.Column(db.Text,nullable=False,default="")
	t15 = db.Column(db.Text,nullable=False,default="")
	t16 = db.Column(db.Text,nullable=False,default="")
	t17 = db.Column(db.Text,nullable=False,default="")
	t18 = db.Column(db.Text,nullable=False,default="")
	t19 = db.Column(db.Text,nullable=False,default="")
	t20 = db.Column(db.Text,nullable=False,default="")
	t21 = db.Column(db.Text,nullable=False,default="")


class Server2(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Text,nullable=False,default="")
	t2 = db.Column(db.Text,nullable=False,default="")
	t3 = db.Column(db.Text,nullable=False,default="")
	t4 = db.Column(db.Text,nullable=False,default="")
	t5 = db.Column(db.Text,nullable=False,default="")
	t6 = db.Column(db.Text,nullable=False,default="")
	t7 = db.Column(db.Text,nullable=False,default="")
	t8 = db.Column(db.Text,nullable=False,default="")
	t9 = db.Column(db.Text,nullable=False,default="")
	t10 = db.Column(db.Text,nullable=False,default="")
	t11 = db.Column(db.Text,nullable=False,default="")
	t12 = db.Column(db.Text,nullable=False,default="")
	t13 = db.Column(db.Text,nullable=False,default="")
	t14 = db.Column(db.Text,nullable=False,default="")
	t15 = db.Column(db.Text,nullable=False,default="")
	t16 = db.Column(db.Text,nullable=False,default="")
	t17 = db.Column(db.Text,nullable=False,default="")
	t18 = db.Column(db.Text,nullable=False,default="")
	t19 = db.Column(db.Text,nullable=False,default="")
	t20 = db.Column(db.Text,nullable=False,default="")
	t21 = db.Column(db.Text,nullable=False,default="")


class Server3(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Text,nullable=False,default="")
	t2 = db.Column(db.Text,nullable=False,default="")
	t3 = db.Column(db.Text,nullable=False,default="")
	t4 = db.Column(db.Text,nullable=False,default="")
	t5 = db.Column(db.Text,nullable=False,default="")
	t6 = db.Column(db.Text,nullable=False,default="")
	t7 = db.Column(db.Text,nullable=False,default="")
	t8 = db.Column(db.Text,nullable=False,default="")
	t9 = db.Column(db.Text,nullable=False,default="")
	t10 = db.Column(db.Text,nullable=False,default="")
	t11 = db.Column(db.Text,nullable=False,default="")
	t12 = db.Column(db.Text,nullable=False,default="")
	t13 = db.Column(db.Text,nullable=False,default="")
	t14 = db.Column(db.Text,nullable=False,default="")
	t15 = db.Column(db.Text,nullable=False,default="")
	t16 = db.Column(db.Text,nullable=False,default="")
	t17 = db.Column(db.Text,nullable=False,default="")
	t18 = db.Column(db.Text,nullable=False,default="")
	t19 = db.Column(db.Text,nullable=False,default="")
	t20 = db.Column(db.Text,nullable=False,default="")
	t21 = db.Column(db.Text,nullable=False,default="")


class Server4(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Text,nullable=False,default="")
	t2 = db.Column(db.Text,nullable=False,default="")
	t3 = db.Column(db.Text,nullable=False,default="")
	t4 = db.Column(db.Text,nullable=False,default="")
	t5 = db.Column(db.Text,nullable=False,default="")
	t6 = db.Column(db.Text,nullable=False,default="")
	t7 = db.Column(db.Text,nullable=False,default="")
	t8 = db.Column(db.Text,nullable=False,default="")
	t9 = db.Column(db.Text,nullable=False,default="")
	t10 = db.Column(db.Text,nullable=False,default="")
	t11 = db.Column(db.Text,nullable=False,default="")
	t12 = db.Column(db.Text,nullable=False,default="")
	t13 = db.Column(db.Text,nullable=False,default="")
	t14 = db.Column(db.Text,nullable=False,default="")
	t15 = db.Column(db.Text,nullable=False,default="")
	t16 = db.Column(db.Text,nullable=False,default="")
	t17 = db.Column(db.Text,nullable=False,default="")
	t18 = db.Column(db.Text,nullable=False,default="")
	t19 = db.Column(db.Text,nullable=False,default="")
	t20 = db.Column(db.Text,nullable=False,default="")
	t21 = db.Column(db.Text,nullable=False,default="")

class System(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# date format: YYYY-MM-DD
	date = db.Column(db.String(10), nullable=False, default=date.today().strftime('%Y-%m-%d'))

	def __repr__(self):
		return f'<date {self.date}>'

'''
time_slot column format:
(2020-12-05,09:00,serv1,xxx)(2020-12-05,09:00,serv2,xxx).......
'''

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	email      = db.Column(db.String(100), unique=True, nullable=False)
	password   = db.Column(db.String(60), nullable=False)
	time_slot  = db.Column(db.Text,nullable=False,default="")

	def __repr__(self):
		return f'<USER {self.username} {self.email}>'
