from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField
from wtforms import validators 
from app import db, models



## I will link into the database here making validators for the username and password 
## of the login form 

class LoginForm(Form):
    email    = StringField('email', validators=[validators.DataRequired(), validators.email()])
    password = PasswordField('password', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=True)


class SignUpForm(Form):

    email    = StringField('email', validators=[validators.DataRequired(message="Forgot this one!"), validators.Email(message="This doesn't look like an email.."), validators.Length(message="4 to 25 characters please!",min=4, max=25)])
    password = PasswordField('password', validators=[validators.DataRequired("Whoops!"), validators.EqualTo('conPass', message="Passwords must match"), validators.Length(message="6 to 25 characters please!", min=6, max=25)])
    conPass  = PasswordField('conPass', validators=[validators.DataRequired("You forgot me!"), validators.EqualTo('password')],)
    fullname = StringField('fullname', validators=[validators.DataRequired("You forgot me!")])
    age      = IntegerField('age', validators = [validators.DataRequired("This doesn't look like your age")])
    
    carType  = SelectField(u'Programming Language', choices=[('truck','Truck'),('sedan', 'Sedan'), ('SUV', 'SUV'), ('none', 'I don\'t have a car')])

class FindRidesForm(Form):

    dest = StringField('dest', validators=[validators.DataRequired(message="Where you heading to?"), validators.Length(message="Please enter a 2 digit state code", min=2,max=2)])
    orig = StringField('orig', validators=[validators.DataRequired(message="Where you departing from?"), validators.Length(message="Please enter a 2 digit state code", min=2,max=2)])


class TripForm(Form):

    origin = StringField('origin', validators = [validators.DataRequired(message="Where are you coming from?"), validators.Length(message="Please enter a valid state code",min=2, max=2)])
    destination = StringField('destination', validators = [validators.DataRequired(message="Where are you heading?"), validators.Length(message="Please enter a valid state code",min=2, max=2)])
    numSeats = IntegerField('numSeats', validators=[validators.DataRequired(message="How many people can you fit?")])
    time = StringField('time', validators=[validators.DataRequired(message="What time are you leaving?")])
