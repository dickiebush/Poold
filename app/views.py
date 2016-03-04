from flask import make_response, render_template, request, redirect, flash, session, url_for, request, g
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required 
from .forms import LoginForm, SignUpForm, TripForm, FindRidesForm
from .models import User, Trip

# Reroute to login screen
@app.route('/', methods=['GET', 'POST'])
def hello():
    return redirect('/login')


# Have user log in or redirect to sign up 
@app.route('/login', methods=['GET', 'POST'])
def welcome():


    if g.user is not None and g.user.is_authenticated:
        
        return giveOrFind()


    form = LoginForm()

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
            return render_template('login.html', form=form, msg2="Please enter a valid email")
    
    if request.cookies.get('splashed') == 'yes':
        print('cookie confirmed')
        return render_template('login.html', form=form)
    else:
        resp = make_response(render_template('splash.html'))
        resp.set_cookie('splashed', 'yes')   
        return resp


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    form = SignUpForm()

    if form.validate_on_submit():
        

        u = User(email=form.email.data,password=form.password.data,fullname=form.fullname.data, 
        age=int(form.age.data), carType=form.carType.data)
        # save data to database here 
        db.session.add(u)
        db.session.commit()

        login_user(u, remember=True);
       

        return giveOrFind()
     

    return render_template('signup.html', form = form)



@app.route('/findrides', methods=["GET",'POST'])
@login_required
def find_rides():

    form = FindRidesForm()


    if form.validate_on_submit():
        dest = form.dest.data
        orig = form.orig.data

        trips = Trip.query.all()
        users = User.query.all()

        newTrips = {}

        # how to, given a ID email, get that users information to print out on the results page 
        for trip in trips:
            if trip.origin == orig and trip.destination == dest:
                user = User.query.get(trip.user_id)
                newTrips[user] = trip
                

        for user,trip in newTrips.items():
            if user == None:
                print trip.origin
            else:
                print user.fullname + " " + trip.origin
        ## Have a dictionary of User : Trip, how to query into database based on email 
        return render_template("results.html", dest = dest, orig = orig, form = form, trips = newTrips)


    return render_template("findrides.html", form = form)

    # LEFTOFF -- GO ON RESULTS PAGE AND DISPLAY INFROMATION FROM THE TRIP ARRAY 

    

@app.route('/giveride', methods=["GET","POST"])
@login_required
def giveride():

    form = TripForm()
    

    if form.validate_on_submit():
        
        trip = Trip(origin=form.origin.data, destination=form.destination.data, timeLeaving=form.time.data, numSeats=form.numSeats.data, user_id=g.user.email)
        db.session.add(trip)
        db.session.commit()

        return "<center><h3>Thanks so much for using Poold, a potential rider will be contacting you shortly</h3> <br><br> <form action=\"/\",methods=\"get\"> <input type=\"submit\", value=\"Return to rides screen\"> </center>"
                
    
    print form.errors

    #return regular form template
    return render_template('giveride.html', form = form)

@app.route('/giveorfind', methods=["GET","POST"])
def giveOrFind():
    
    if request.method == 'POST':
        if 'logout' in request.form:
            print "logging out"
            logout_user()
            return redirect('/login')
        elif 'cancelride' in request.form:
            user = g.user
            print "cancelling ride"
            trips = Trip.query.all()
            for trip in trips:
                if trip.user_id == user.email:
                    print "deleted trip"
                    db.session.delete(trip)
                    db.session.commit()
            return render_template("giveorfind.html")
    

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



