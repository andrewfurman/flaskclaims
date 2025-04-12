
from flask import Blueprint, render_template

plans_bp = Blueprint('plans', __name__, template_folder='templates')

@plans_bp.route('/plans')
def view_plans():
    return render_template('plans.html')
