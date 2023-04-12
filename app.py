from flask import Flask, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def list_pets():
    """show home page"""
    # *query to get all pets
    pets = Pet.query.all()

    # * pass all pets object to template
    return render_template('pet_list.html', pets=pets)


@app.route('/<int:pet_id>', methods=["GET"])
def show_pet(pet_id):
    """Show details about a single pet"""
    # *Query to get pet info
    pet = Pet.query.get_or_404(pet_id)

    # *render template for pet details and pass pet object to template
    return render_template("pet_details.html", pet=pet)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show add pet form and handle add single pet instance"""
    # *create form instance using WTForm
    form = PetForm()

    # * validate form on submit
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        # * with valid form data create an instance of Pet model with form data
        p = Pet(name=name, species=species, photo_url=photo_url,
                age=age, notes=notes, available=available)

        # * add the new pet to the session and commit the session changes to the db
        db.session.add(p)
        db.session.commit()
        flash(f'Pet {p.name} has been added')
        # * redirect to the home page at successful completion
        return redirect('/')
    else:
        # * if unsuccessful or no data in form redirect to the form template page
        return render_template('add_pet_form.html', form=form)


@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show edit form and handle edit of single pet instance"""
    # *find matching pet based on pet.id => pet_id
    pet = Pet.query.get_or_404(pet_id)

    # *create form instance using WTForm
    form = PetForm(obj=pet)

    # * validate form on submit
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        # * commit changes to db
        db.session.commit()

        # *flash message on successful completion
        flash(f' Pet {pet.name} has been updated')

        # * redirect to the home page at successful completion
        return redirect('/')
    else:
        # * if unsuccessful or no data in form redirect to the form template page
        return render_template('edit_pet_form.html', form=form, pet=pet)
