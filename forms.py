from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, NumberRange


pet_choices = ["Cat", "Dog", "Porcupine"]


class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired()])
    species = SelectField("Species", choices=[
        (p, p) for p in pet_choices], default='Dog')
    photo_url = StringField("Photo URL")
    age = FloatField("Age", validators=[NumberRange(
        min=0, max=30, message="Age Range: 0 - 30 years")])
    notes = StringField('Notes')
    available = BooleanField("Available", default=True)


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL")
    notes = StringField('Notes')
    available = BooleanField("Available", default=True)
