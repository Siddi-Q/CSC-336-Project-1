from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class SignInForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    ssn = StringField('Social Security Number', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    date_of_birth = StringField('Date of Birth', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    emergency_contact_name = StringField('Emergency Contact Full Name', validators=[DataRequired()])
    emergency_contact_number = StringField('Emergency Contact Number', validators=[DataRequired()])
    submit = SubmitField('Sign In', validators=[DataRequired()])
