from app import db 

class User(db.Model):
    email = db.Column(db.String(120), index=True, unique=True, primary_key=True)
    password = db.Column(db.String(120), index=True, unique=True)
    fullname = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer, index=True)
    carType = db.Column(db.String(64), index=True, unique=True)
   

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


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(10), index=True, unique=True)
    destination = db.Column(db.String(10), index=True, unique=True)
    timeLeaving = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'this is a trip'
