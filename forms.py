from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class SignInForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    date_of_birth = StringField('Date of Birth', validators=[DataRequired()])
    address = StringField('Address')
    phone_number = StringField('Phone Number')
    emergency_contact_number = StringField('Emergency Contact Number')
    submit = SubmitField('Sign In')
