from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
    description  = StringField(u'Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
    		FileRequired(),
    		FileAllowed(['jpg', 'png', 'Images only!'])
    ])

