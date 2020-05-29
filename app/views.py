"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, random, datetime, time
from app import app, db
from flask import render_template, request, redirect, url_for, flash, abort
from app.forms import UserProfileForm
from app.models import UserProfile
from werkzeug.utils import secure_filename




###
# Routing for your application.
###



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods = ['GET', 'POST'])
def profile():

    form = UserProfileForm()

    if request.method == 'POST' and form.validate_on_submit():

        firstname = form.firstname.data
        lastname = form.lastname.data
        gender = form.gender.data
        #email = form.email.data
        location = form.location.data
        biography = form.biography.data

        display_pic = form.display_pic.data
        filename = secure_filename(display_pic.filename)
        display_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        date_joined = format_date_join()


        newprofile = UserProfile(first_name=firstname, last_name=lastname, gender=gender, location=location, biography=biography, display_pic=filename)
        db.session.add(newprofile)
        db.session.commit()

        flash('Thank You For Joining Us!. Profile created..', 'success')
        return redirect(url_for('profiles'))
    else:
        flash_errors(form)

    return render_template('profile.html', form=form)

@app.route('/profiles')
def profiles():
    """Render the website's profiles page."""
    profiles = db.session.query(UserProfile).all()
    return render_template('profiles.html',profiles=profiles)

@app.route('/profile/<userid>')
def loadprofile(userid):
    """Render the website's profiles page."""
    usertag = UserProfile.query.get(userid)
    return render_template('loadprofile.html', usertag=usertag)


def format_date_join():
    return (time.strftime("%B,%Y"))
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (getattr(form, field).label.text,error))


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'danger')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
