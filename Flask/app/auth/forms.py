from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
   # resetpasswd = SubmitField('Rest Password')
    #test = PasswordField('test', validators=[Required()])


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[
                        Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores, must start with A-z')])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])

    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangepasswordForm(FlaskForm):

    old_password = PasswordField('Old Password', validators=[Required()])

    new_password = PasswordField('New Password', validators=[Required(), EqualTo(
        'confirm_new_password', message='Passwords must match.')])
    confirm_new_password = PasswordField(
        'Confirm New Password', validators=[Required()])

    submit = SubmitField('Submit')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Submit')


class PasswordResetForm(FlaskForm):

    new_password = PasswordField('New Password', validators=[Required(), EqualTo(
        'confirm_new_password', message='Passwords must match.')])
    confirm_new_password = PasswordField(
        'Confirm New Password', validators=[Required()])

    submit = SubmitField('Submit')


# resetpasswd = SubmitField('Rest Password')


'''
class ChangeemailForm(FlaskForm):

    old_password = PasswordField('Old Password', validators=[Required()])

    new_password = PasswordField('New Password', validators=[Required(), EqualTo(
        'confirm_new_password', message='Passwords must match.')])
    confirm_new_password = PasswordField(
        'Confirm Password', validators=[Required()])

    submit = SubmitField('Confirm')
'''
