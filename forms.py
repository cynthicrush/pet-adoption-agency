from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, Optional, URL

class AddPetForm(FlaskForm):
  '''Form for adding pets.'''

  name = StringField('Pet Name', validators=[InputRequired()])
  species = SelectField('Pet Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
  photo_url = StringField('Pet Photo', validators=[Optional(), URL()])
  age = FloatField('Pet Age', validators=[Optional(), NumberRange(min=0, max=30)])
  notes = TextAreaField('Additional Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
  '''Form for editing pets.'''

  photo_url = StringField('Pet Photo', validators=[Optional(), URL()])
  notes = TextAreaField('Additional Notes', validators=[Optional()])
  available = BooleanField('Availible?')

