from flask import render_template, request, redirect, flash, session, url_for, request, g
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required 
from .forms import LoginForm, SignUpForm
from .models import User, Trip

# Reroute to login screen
@app.route('/', methods=['GET', 'POST'])
def hello():
    return redirect('/login')


# Have user log in or redirect to sign up 
@app.route('/login', methods=['GET', 'POST'])
def welcome():

    if g.user is not None and g.user.is_authenticated:
        print g.user
        return redirect('/giveorfind')

    form = LoginForm()
 ###################################################
 #### LEFT OFF #### 
 #
 # I just put two buttons on the giveorfind screen
 # i have linked those buttons to two urls that will be implemeneted, one 
 # already is implemented, the other will needs to be put together with a 
 # form that links to a database inputting the destination adn origin in that trip 
 # and associate that trip with the current user
        # this includes a redirection after entering the data that says something
        # along the lines of "A rider will get in touch with you shortly "
 # then, we need to redo the parsing of the database on the find rides screen that will
 # look through all Trips and see which ones match 

 #######################################################






    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if form.password.data == user.password:
                if form.remember_me.data:
                    session['remember_me'] = form.remember_me.data
                    login_user(user, remember=True)
                else:
                    login_user(user, remember=False)
                return giveOrFind() #login successful

            else:
                return render_template('login.html', form=form, msg1="Password incorrect")
        else:
            return render_template('login.html', form=form, msg2="Pleas enter a valid email")
        
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    form = SignUpForm()

    if form.validate_on_submit():
        flash('Thanks for Signing Up, %s -- Go ahead an Log In now' % str(form.fullname.data).split(" ")[0])

        u = User(email=form.email.data,password=form.password.data,fullname=form.fullname.data, 
        age=int(form.age.data), carType=form.carType.data)
        # save data to database here 
        db.session.add(u)
        db.session.commit()
       

        return redirect('/login')

     

    return render_template('signup.html', form = form)


@app.route('/findrides', methods=["GET","POST"])
@login_required
def find_rides():
    return render_template("findrides.html")

@app.route('/findrides', methods=['POST'])
def my_form_post():

    dest = request.form['dest']
    orig = request.form['orig']

    newPersons = []

    #for person in persons:
    #   if person['origin'] == orig and person['destination'] == dest:
    #       newPersons.append(person)

    return render_template("results.html", dest = dest, orig = orig, persons = newPersons)


 
@app.route('/giveorfind')
@login_required
def giveOrFind():

    return render_template("giveorfind.html")
if __name__ == '__main__':
    app.run(debug=True)

#########################################################################
# Helper functions 
#########################################################################

@lm.user_loader
def load_user(id):
    return User.query.get(id)

@app.before_request
def before_request():
    g.user = current_user








