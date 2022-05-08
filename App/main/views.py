from flask import render_template as render
from .main import main_blueprint as main

@main.route('/')       #Aliasing
def index():
    return render('index.html')