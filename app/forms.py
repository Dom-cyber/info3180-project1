from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email


class UserProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
   # email = StringField('E-mail', validators=[DataRequired(), Email()])
    location = StringField('ocation', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[("Male", "Male"), ('Female', 'Female')], validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    display_pic = FileField("Display Pic", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])