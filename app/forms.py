from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
    description  = TextAreaField(u'Description')
    photo = FileField('Photo', validators=[
    		FileRequired(),
    		FileAllowed(['jpg', 'png', 'Images only!'])
    ])

