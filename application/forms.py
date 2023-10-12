from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    # email = StringField('Email', validators=[DataRequired(), Email(), Length(max=128)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=128)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class EditProfile(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=128)])
    bio = TextAreaField('Bio', validators=[Length(max=256)])
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Save Changes')

class CreatePost(FlaskForm):
    caption = TextAreaField('Caption', validators=[DataRequired(), Length(max=256)])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Create Post')

class EditPost(FlaskForm):
    caption = TextAreaField('Caption', validators=[DataRequired(), Length(max=256)])
    image = FileField('Edit Image', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Save Changes')
