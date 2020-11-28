from MANSYS import db, bcrypt
from MANSYS.models import User, Server1, Server2, Server3, Server4
import random

if __name__=="__main__":
	# db.create_all()

	# server1 = Server1()
	# for i in range(21):
	# 	server1.time_slots[i] = random.choice([True,False])
	
	# db.session.add(server1)
	# server1 = Server1.query.filter_by(id=1).first()
	# print(server1.t1)
	# server2 = Server2()
	# for i in range(21):
	# 	server2.time_slots[i] = random.choice([True,False])
	
	# db.session.add(server2)
	
	# server3 = Server3()
	# for i in range(21):
	# 	server3.time_slots[i] = random.choice([True,False])
	
	# db.session.add(server3)
	
	# server4 = Server4()
	# for i in range(21):
	# 	server4.time_slots[i] = random.choice([True,False])
	
	# db.session.add(server4)
	
	# db.session.commit()

	# hashed_pw = bcrypt.generate_password_hash("password").decode('utf-8')
	# user1 = User(username="BenAndrew310",
	# 			email="benandrew2442@gmail.com",
	# 			password=hashed_pw)

	# db.session.add(user1)
	# db.session.commit()

	# user2 = User(username="Marc",
	# 			email="marc_etienne@gmail.com",
	# 			password=hashed_pw)

	# db.session.add(user2)
	# db.session.commit()

	# users = User.query.all()
	# server1s = Server1.query.all()
	# server2s = Server2.query.all()
	# server3s = Server3.query.all()
	# server4s = Server4.query.all()
	# for user in users:
	# 	db.session.delete(user)
	# for server1 in server1s:
	# 	db.session.delete(server1)
	# for server2 in server2s:
	# 	db.session.delete(server2)
	# for server3 in server3s:
	# 	db.session.delete(server3)
	# for server4 in server4s:
	# 	db.session.delete(server4)
	# db.session.commit()