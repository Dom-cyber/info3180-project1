from . import db


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(25))
    #email = db.Column(db.String(255), unique=True)
    location = db.Column(db.String(100))
    biography = db.Column(db.Text())
    display_pic = db.Column(db.String(100))
    date_joined  = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % (self.username)
