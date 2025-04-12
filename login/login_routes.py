
from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/')
def welcome():
    return render_template('welcome.html')

@login_bp.route('/header')
def header():
    return render_template('header.html')
