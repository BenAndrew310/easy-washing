from flask import Flask,render_template,url_for,jsonify,flash,redirect,request
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from MANSYS import db, app, bcrypt, mail
from MANSYS.registration import Login, Register
from MANSYS.models import User, System, Server1, Server2, Server3, Server4
from MANSYS.system_updater import SYSTEM_UPDATER

import os

SYS_UP = SYSTEM_UPDATER(db, System, Server1, Server2, Server3, Server4, User)
SYS_UP.start()
TIMES = ['09:00', '09:40', '10:20', '11:00', '11:40', '12:20', '13:00', '13:40', '14:20', '15:00', '15:40', '16:20', '17:00', '17:40', '18:20', '19:00', '19:40', '20:20', '21:00', '21:40', '22:20']

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
@login_required
def home():
	form = Register()
	if form.validate_on_submit():
		date = str(form.date.data)
		time = str(form.time.data)
		serv = str(form.server.data)

		if serv == "server 1":
			server=Server1.query.filter_by(id=1).first()
		elif serv == "server 2":
			server=Server2.query.filter_by(id=1).first()
		elif serv == "server 3":
			server=Server3.query.filter_by(id=1).first()
		elif serv == "server 4":
			server=Server4.query.filter_by(id=1).first()

		for ind,t in enumerate(TIMES):
			if len(current_user.time_slot)//24 >= 3:
				flash('You have reached the maximum number of reservations allowed','danger')
				break

			if t == time:
				s = eval(f'server.t{ind+1}')
				if s.find(date[:10]) == -1:
					exec(f"server.t{ind+1} = s+'{date[:10]}'+';'")
					exec(f"db.session.commit()")
					uInfo = current_user.time_slot
					current_user.time_slot = uInfo + f'({date[:10]},{time},serv{serv[-1]})'
					db.session.commit()
					flash('Your reservation was successful','success')
					
					activation_code = SYS_UP.get_activation_code(3)

					
					# msg = Message('Easy Washing reservation', sender='bensoftware0101@gmail.com', recipients = [current_user.email])
					# msg.body = f"Dear {current_user.username},\nYou have successfully registered for using the washing machine" +\
					# 			f" labeled {serv} on {date} at {time}. The activation code of the machine is {activation_code}"
					# mail.send(msg)
					# S.connect("smtp.gmail.com",587)
					# S.ehlo()
					# S.starttls()
					# S.ehlo()
					# S.login(email, password)
					# S.send(email,current_user.email,
					# 	f"Dear {current_user.username},\nYou have successfully registered for using the washing machine" +\
					# 	f" labeled {serv} on {date} at {time}. The activation code of the machine is {activation_code}")
					# S.quit()
				
				else:
					flash('This time slot has already been taken.\nPlease select another time slot','danger')

				break

	return render_template("home.html", title="Easy Washing", form=form)

# @app.route("/email-notification/<status>/<date>/<time>/<serv>/<activation_code>")
# def send_email(status,date,time,serv,activation_code):
# 	global mail
# 	'''
# 	status
# 		 1 : new reservation
# 		-1 : reservation deleted
# 	'''
# 	if status == 1:
# 		msg = Message('Easy Washing reservation', sender=os.environ.get('PROJ_EMAIL'), recipients = [current_user.email])
# 		msg.body = f"Dear {current_user.username},\nYou have successfully registered for using the washing machine" +\
# 					f" labeled {serv} on {date} at {time}. The activation code of the machine is {activation_code}"
# 		mail.send(msg)

# 	return redirect(url_for('home'))

@app.route("/reservations",methods=["GET","POST"])
@login_required
def manage_reservations():
	reservations = []
	for i in range(0,len(current_user.time_slot),24):
		reservations.append(current_user.time_slot[i:i+24])

	return render_template("reservations.html",title="reservations",reservations=reservations)

@app.route("/delete/<date>/<time>/<serv>")
def delete_reservation(date,time,serv):
	if serv == '1':
		server = Server1.query.filter_by(id=1).first()
	elif serv == '2':
		server = Server2.query.filter_by(id=1).first()
	elif serv == '3':
		server = Server3.query.filter_by(id=1).first()
	elif serv == '4':
		server = Server4.query.filter_by(id=1).first()

	s = eval(f"server.t{TIMES.index(time)+1}")
	ind = s.find(date)
	exec(f"server.t{TIMES.index(time)+1} = s[:ind]+s[ind+11:]")
	db.session.commit()

	s = current_user.time_slot
	ind = s.find(f"({date},{time},serv{serv})")
	current_user.time_slot = s[:ind] + (s[ind+24:] if ind+24<len(s) else '')
	db.session.commit()

	return redirect(url_for('manage_reservations'))

@app.route("/login",methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password.','danger')
	return render_template("login.html",title="Login",form=form)

@app.route("/logout",methods=["GET","POST"])
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))