from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField
from wtforms import validators 


class LoginForm(Form):
    email    = StringField('email', validators=[validators.DataRequired()])
    password = PasswordField('password', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


validators.Length(min=4, max=25)

class SignUpForm(Form):

    email    = StringField('email', validators=[validators.DataRequired(message="Forgot this one!"), validators.Email(message="This doesn't look like an email.."), validators.Length(message="4 to 25 characters please!",min=4, max=25)])
    password = StringField('password', validators=[validators.DataRequired("Whoops!"), validators.EqualTo('conPass', message="Passwords must match"), validators.Length(message="6 to 25 characters please!", min=6, max=25)])
    conPass  = StringField('conPass', validators=[validators.DataRequired("You forgot me!"), validators.EqualTo('password')],)
    fullname = StringField('fullname', validators=[validators.DataRequired("You forgot me!")])
    age      = IntegerField('age', validators = [validators.DataRequired("This doesn't look like your age")])
    
    carType  = SelectField(u'Programming Language', choices=[('truck','Truck'),('sedan', 'Sedan'), ('SUV', 'SUV'), ('none', 'I don\'t have a car')])


