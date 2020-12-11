from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,DateField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from MANSYS.models import User
import datetime


def get_time_slots(start="09:00",stop_="23:00",delay=40):
    ts = [start]
    current = start

    while True:
        ho = int(current[:2])
        mi = int(current[-2:])

        new_mi = mi+delay

        if new_mi>=60:
            ho += new_mi//60
            new_mi = new_mi%60

        if ho>int(stop_[:2]):
            break

        if ho==int(stop_[:2]) and new_mi>=int(stop_[-2:]):
            break

        str_ho = str(ho) if len(str(ho))==2 else '0'+str(ho)
        str_mi = str(new_mi) if len(str(new_mi))==2 else '0'+str(new_mi)

        ts.append(str_ho+':'+str_mi)
        current = str_ho+':'+str_mi

    return ts

def get_dates():
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	today = datetime.date.today()
	day_name = days[today.weekday()]
	date_str = today.strftime('%Y-%m-%d')
	DATES = [f'{date_str} - {day_name}']
	
	date = today
	for i in range(1,7):
		date = today+datetime.timedelta(days=i)
		day_name = days[date.weekday()]
		date_str = date.strftime('%Y-%m-%d')
		DATES.append(f'{date_str} - {day_name}')

	return DATES

TIMES = get_time_slots()
DATES = get_dates()

class Login(FlaskForm):
	email = StringField('Email', validators=[DataRequired(),Length(min=4,max=100)], render_kw={"placeholder": "email"})
	password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=60)],render_kw={"placeholder": "password"})
	remember = BooleanField('Remember me')

	submit = SubmitField('Login')

class SignUp(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),Length(min=4,max=20)], render_kw={"placeholder": "username"})
	email = StringField('Email', validators=[DataRequired(),Length(min=4,max=100)], render_kw={"placeholder": "email"})
	password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=60)],render_kw={"placeholder": "password"})
	confirm_password = PasswordField('Confirm Password',
			validators=[DataRequired(),EqualTo('password')],
			render_kw={"placeholder": "confirm password"})

	submit = SubmitField('Sign up')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("That username is already taken.")

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("That email is already taken.")

class Register(FlaskForm):
	date = SelectField('Select a date', choices=DATES ,validators=[DataRequired()])
	time = SelectField('Select a time', choices = TIMES , validators=[DataRequired()])
	server = SelectField('Select a machine', choices = ['Washing machine 1','Washing machine 2','Washing machine 3','Washing machine 4'], validators=[DataRequired()])

	submit = SubmitField('Register')