
from flask import Blueprint, render_template

providers_bp = Blueprint('providers', __name__, template_folder='templates')

@providers_bp.route('/providers')
def view_providers():
    return render_template('providers.html')
