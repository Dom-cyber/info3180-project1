from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email


class UserProfileForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
   # email = StringField('E-mail', validators=[DataRequired(), Email()])
    location = StringField('location', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[("Male", "Male"), ('Female', 'Female')], validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    photo = FileField("Display Pic", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])