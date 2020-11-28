from MANSYS import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from collections import deque

class Server1(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Boolean,nullable=False,default=True)
	t2 = db.Column(db.Boolean,nullable=False,default=True)
	t3 = db.Column(db.Boolean,nullable=False,default=True)
	t4 = db.Column(db.Boolean,nullable=False,default=True)
	t5 = db.Column(db.Boolean,nullable=False,default=True)
	t6 = db.Column(db.Boolean,nullable=False,default=True)
	t7 = db.Column(db.Boolean,nullable=False,default=True)
	t8 = db.Column(db.Boolean,nullable=False,default=True)
	t9 = db.Column(db.Boolean,nullable=False,default=True)
	t10 = db.Column(db.Boolean,nullable=False,default=True)
	t11 = db.Column(db.Boolean,nullable=False,default=True)
	t12 = db.Column(db.Boolean,nullable=False,default=True)
	t13 = db.Column(db.Boolean,nullable=False,default=True)
	t14 = db.Column(db.Boolean,nullable=False,default=True)
	t15 = db.Column(db.Boolean,nullable=False,default=True)
	t16 = db.Column(db.Boolean,nullable=False,default=True)
	t17 = db.Column(db.Boolean,nullable=False,default=True)
	t18 = db.Column(db.Boolean,nullable=False,default=True)
	t19 = db.Column(db.Boolean,nullable=False,default=True)
	t20 = db.Column(db.Boolean,nullable=False,default=True)
	t21 = db.Column(db.Boolean,nullable=False,default=True)

	time_slots = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21]

class Server2(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Boolean,nullable=False,default=True)
	t2 = db.Column(db.Boolean,nullable=False,default=True)
	t3 = db.Column(db.Boolean,nullable=False,default=True)
	t4 = db.Column(db.Boolean,nullable=False,default=True)
	t5 = db.Column(db.Boolean,nullable=False,default=True)
	t6 = db.Column(db.Boolean,nullable=False,default=True)
	t7 = db.Column(db.Boolean,nullable=False,default=True)
	t8 = db.Column(db.Boolean,nullable=False,default=True)
	t9 = db.Column(db.Boolean,nullable=False,default=True)
	t10 = db.Column(db.Boolean,nullable=False,default=True)
	t11 = db.Column(db.Boolean,nullable=False,default=True)
	t12 = db.Column(db.Boolean,nullable=False,default=True)
	t13 = db.Column(db.Boolean,nullable=False,default=True)
	t14 = db.Column(db.Boolean,nullable=False,default=True)
	t15 = db.Column(db.Boolean,nullable=False,default=True)
	t16 = db.Column(db.Boolean,nullable=False,default=True)
	t17 = db.Column(db.Boolean,nullable=False,default=True)
	t18 = db.Column(db.Boolean,nullable=False,default=True)
	t19 = db.Column(db.Boolean,nullable=False,default=True)
	t20 = db.Column(db.Boolean,nullable=False,default=True)
	t21 = db.Column(db.Boolean,nullable=False,default=True)

	time_slots = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21]

class Server3(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Boolean,nullable=False,default=True)
	t2 = db.Column(db.Boolean,nullable=False,default=True)
	t3 = db.Column(db.Boolean,nullable=False,default=True)
	t4 = db.Column(db.Boolean,nullable=False,default=True)
	t5 = db.Column(db.Boolean,nullable=False,default=True)
	t6 = db.Column(db.Boolean,nullable=False,default=True)
	t7 = db.Column(db.Boolean,nullable=False,default=True)
	t8 = db.Column(db.Boolean,nullable=False,default=True)
	t9 = db.Column(db.Boolean,nullable=False,default=True)
	t10 = db.Column(db.Boolean,nullable=False,default=True)
	t11 = db.Column(db.Boolean,nullable=False,default=True)
	t12 = db.Column(db.Boolean,nullable=False,default=True)
	t13 = db.Column(db.Boolean,nullable=False,default=True)
	t14 = db.Column(db.Boolean,nullable=False,default=True)
	t15 = db.Column(db.Boolean,nullable=False,default=True)
	t16 = db.Column(db.Boolean,nullable=False,default=True)
	t17 = db.Column(db.Boolean,nullable=False,default=True)
	t18 = db.Column(db.Boolean,nullable=False,default=True)
	t19 = db.Column(db.Boolean,nullable=False,default=True)
	t20 = db.Column(db.Boolean,nullable=False,default=True)
	t21 = db.Column(db.Boolean,nullable=False,default=True)

	time_slots = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21]

class Server4(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	t1 = db.Column(db.Boolean,nullable=False,default=True)
	t2 = db.Column(db.Boolean,nullable=False,default=True)
	t3 = db.Column(db.Boolean,nullable=False,default=True)
	t4 = db.Column(db.Boolean,nullable=False,default=True)
	t5 = db.Column(db.Boolean,nullable=False,default=True)
	t6 = db.Column(db.Boolean,nullable=False,default=True)
	t7 = db.Column(db.Boolean,nullable=False,default=True)
	t8 = db.Column(db.Boolean,nullable=False,default=True)
	t9 = db.Column(db.Boolean,nullable=False,default=True)
	t10 = db.Column(db.Boolean,nullable=False,default=True)
	t11 = db.Column(db.Boolean,nullable=False,default=True)
	t12 = db.Column(db.Boolean,nullable=False,default=True)
	t13 = db.Column(db.Boolean,nullable=False,default=True)
	t14 = db.Column(db.Boolean,nullable=False,default=True)
	t15 = db.Column(db.Boolean,nullable=False,default=True)
	t16 = db.Column(db.Boolean,nullable=False,default=True)
	t17 = db.Column(db.Boolean,nullable=False,default=True)
	t18 = db.Column(db.Boolean,nullable=False,default=True)
	t19 = db.Column(db.Boolean,nullable=False,default=True)
	t20 = db.Column(db.Boolean,nullable=False,default=True)
	t21 = db.Column(db.Boolean,nullable=False,default=True)

	time_slots = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21]


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	email      = db.Column(db.String(100), unique=True, nullable=False)
	password   = db.Column(db.String(60), nullable=False)
	time_slot  = db.Column(db.Text,nullable=False,default="")

	def __repr__(self):
		return f'<USER {self.username}>'

