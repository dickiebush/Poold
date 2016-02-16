from flask import render_template, request
from app import app
from .forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
def welcome():
    # check if they logged in -- if they have call function that
    # shoes you next screen
    form = LoginForm()
    

    # Name, Age, Email, Phone Number, Type of Car

    # Page with two buttons that say I am looking for a ride or I have a ride 

    return render_template('welcome.html', form=form)
 

@app.route('/giveorfind')
def giveOrFind():

    return "here we will present some text"

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
    