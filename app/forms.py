from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email    = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)



class SignUpForm(Form):

    email    = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    conPass  = StringField('conPass', validators=[DataRequired()])
    fullname = StringField('fullname', validators=[DataRequired()])
    age      = IntegerField('age', validators = [DataRequired()])
    
    carType  = SelectField(u'Programming Language', choices=[('truck','Truck'),('sedan', 'Sedan'), ('SUV', 'SUV'), ('none', 'I don\'t have a car')])


