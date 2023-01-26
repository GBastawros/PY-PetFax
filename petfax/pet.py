# Importing Demendencies
from flask import (Blueprint, render_template) 
import json

# Encoding and opening JSON data (pets.json)
pets = json.load(open('pets.json'))
print(pets)

# Pet Blueprint
bp = Blueprint('pet', __name__, url_prefix="/pets")

# Index Route
@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

