
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField, DateField
from wtforms.validators import InputRequired
from flask_wtf.file import  FileRequired, FileAllowed

    
 

class IllustrationForm(FlaskForm):
    illustitle = StringField('Illustitle', validators=[InputRequired()]) 
    #piece = SelectField('Piece',  choices=ipieceList)
    stage = StringField('Illustration Stage', validators=[InputRequired()]) 
    #universe = SelectField('Universe',  choices=iuniverseList)
    illcription = TextAreaField('Illcription', validators=[InputRequired()])
    dateCreated = DateField('Date Created', format='%m/%d/%Y', validators=[InputRequired()])
    dateCompleted = DateField('Date Completed', format='%m/%d/%Y', validators=[InputRequired()])
    #medium = SelectField('Medium Used',  choices=imediumList)
    #genre = SelectField('Genre',  choices=igenreList)
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg','JPG'], 'Images only!')])







