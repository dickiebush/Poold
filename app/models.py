from app import db 

class User(db.Model):
    email = db.Column(db.String(120), index=True, unique=True, primary_key=True)
    password = db.Column(db.String(120), index=True)
    fullname = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    carType = db.Column(db.String(64), index=True)
   
    def __repr__(self):
        return ('<User %r>' % (self.fullname))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.email)  # python 2
        except NameError:
            return str(self.email)  # python 3

### LEFTOFF -- LAST THING IS LINKING THE NEW FINDRIDES TO QUERY INTO THE DATABASE AND FIND MATCHING RIDES
### ALSO ADD PICTURE AND WELCOME TO SCREEN AFTER SUBMITTING RIDE 
class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(10))
    destination = db.Column(db.String(10))
    timeLeaving = db.Column(db.String(10))
    numSeats = db.Column(db.Integer)
    user_id = db.Column(db.String(120))

    def __repr__(self):
        return ("Trip leaving from %s driving to %s leaving at %s posted by %s" % (self.origin, self.destination, self.timeLeaving, self.user_id))
