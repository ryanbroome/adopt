"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

# Drop all Create all tables
db.drop_all()
db.create_all()

# CREATE INSTANCES
l = Pet(name='Leah', species='Dog',
        photo_url='/static/img/leah.jpeg', age=2, notes='Great Dog, likes to chew')

lego = Pet(name='Lego', species='Dog',
           photo_url='/static/img/lego.jpg', age=3, notes='Humper Dog, hide the pillows')

cat = Pet(name='Sprinkles', species='Cat',
          photo_url='/static/img/cat.jpeg', age=26, notes='Super chill cat, really nice')

kitty = Pet(name='Kitty Kat', species='Cat',
            photo_url='/static/img/kitty.jpeg', age=1, notes='Princess kitty has arrived')

spike = Pet(name='Spike', species='Porcupine',
            photo_url='/static/img/spike.jpeg', age=1, notes='Maybe best kept outside and away ')

noface = Pet(name='No Face', species='dog', age=1, notes='No Face Dog')

# COMMIT TO db
db.session.add_all([l, lego, cat, kitty, spike, noface])
db.session.commit()

# CLEAR OUT QUERY OBJECTS ON EACH MODEL
Pet.query.delete()
