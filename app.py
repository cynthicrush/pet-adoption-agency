from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] =True
app.config['SECRET_KEY'] = 'shhh-secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()

# Pet.query.delete()

# cloud = Pet(name='Cloud', species='Bird', photo_url='https://images.freeimages.com/images/small-previews/fee/budgies-1401402.jpg', age=3, notes='She loves to nod', available=True)
# frog_prince = Pet(name='Frog Prince', species='Tree Frog', photo_url='https://images.freeimages.com/images/small-previews/01a/pet-tree-frog-1-1520232.jpg', age=5, notes='He likes moist', available=True)
# happy = Pet(name='Happy', species='Dog', photo_url='https://images.freeimages.com/images/small-previews/787/kvik-1365612.jpg', age=1, notes='He loves to play with people', available=True)
# kitty = Pet(name='Kitty', species='Cat', photo_url='https://images.freeimages.com/images/small-previews/4cb/paw-1394447.jpg', age=10, notes='She is an old lady and loves to sleep', available=True)
# snow_white = Pet(name='Snow White', species='Rabbit', photo_url='https://images.freeimages.com/images/small-previews/cdd/my-pet-2-1362659.jpg', age=6, notes='He likes to chewing on paper', available=True)

# db.session.add(cloud)
# db.session.add(frog_prince)
# db.session.add(happy)
# db.session.add(kitty)
# db.session.add(snow_white)

# db.session.commit()

@app.route('/')
def homepage():
  '''Listing pets on the home page.'''
  pets = Pet.query.all()
  return render_template('homepage.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
  '''Show add pet form and handle add.'''

  form = AddPetForm()
  if form.validate_on_submit():
    new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
    db.session.add(new_pet)
    db.session.commit()
    flash(f'New pet {new_pet.name} added')
    return redirect('/')
  else:
    return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
  '''Show edit pet form and handle edit'''

  pet = Pet.query.get_or_404(pet_id)
  form = EditPetForm(obj=pet)
  if form.validate_on_submit():

    pet.photo_url = form.photo_url.data
    pet.notes = form.notes.data
    pet.available = form.available.data
    db.session.commit()
    return redirect('/')

  else:
    return render_template('pet.html', pet=pet, form=form)
