from flask import render_template, request, redirect
from app import app
from .forms import LoginForm, SignUpForm

# Reroute to login screen
@app.route('/', methods=['GET', 'POST'])
def hello():
    return redirect('/login')


# Have user log in or redirect to sign up 
@app.route('/login', methods=['GET', 'POST'])
def welcome():
    # check if they logged in -- if they have call function that
    # shoes you next screen
    form = LoginForm()

    if form.validate_on_submit():
        return
        # 
    # Name, Age, Email, Phone Number, Type of Car
    # Page with two buttons that say I am looking for a ride or I have a ride 
    return render_template('welcome.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    form = SignUpForm()

    if form.validate_on_submit():
        # save data to database here 
            return redirect('/login')

        # need to put error checking in here somewhere 

    return render_template('signup.html', form = form)










@app.route('/findrides')
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
def giveOrFind():

    return "here we will present some text"
if __name__ == '__main__':
    app.run(debug=True)



""" 1) HTML and Web Forms and Database hookup for intro register screen """
""" 2) Intermediary screen that asks whether you want a ride or need a ride """
""" 3) Set up the 'I can give a ride' screen to enter the information that then links
        to the database and tells them they will be put in contact with anyone who needs it
"""
""" 4) Set up the function to query into the database to find people leaving the
        same destination and going to a certain one 
"""
    