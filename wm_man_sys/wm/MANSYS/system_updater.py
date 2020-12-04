import datetime
from time import sleep
from threading import Thread
import random

class SYSTEM_UPDATER:

	def __init__(self,db,System, Server1, Server2, Server3, Server4, User):
		self.db = db
		self.SYS_INFO = System.query.filter_by(id=1).first()
		self.Users = User.query.all()
		self.SERV1 = Server1.query.filter_by(id=1).first()
		self.SERV2 = Server2.query.filter_by(id=1).first()
		self.SERV3 = Server3.query.filter_by(id=1).first()
		self.SERV4 = Server4.query.filter_by(id=1).first()


	def check_date(self):
		while True:
			today = datetime.date.today()
			self.SYS_INFO.date = today.strftime('%Y-%m-%d')
			self.db.session.commit()
			yesterday = datetime.date.today() - datetime.timedelta(days=1)
			tomorrow = datetime.date.today() + datetime.timedelta(days=1)
			delay = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day) - datetime.datetime.now()
			self.update_users(yesterday)
			sleep(delay.seconds+60)

	def update_users(self,yesterday):
		offset = 24
		yesterday = yesterday.strftime('%Y-%m-%d')
		for user in self.Users:
			utime = user.time_slot
			while True:
				ind = utime.find(yesterday)
				if ind==-1:
					break
				utime = utime[ind+offset:]
			user.time_slot = utime
			self.db.session.commit()

	def start(self):
		t = Thread(target=self.check_date)
		t.daemon = True
		t.start()

	def get_activation_code(self,n=3):
		code = [str(random.randint(0,9)) for x in range(n)]
		return "".join(code)