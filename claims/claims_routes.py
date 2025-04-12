from flask import Blueprint, render_template

claims_bp = Blueprint('claims', __name__, template_folder='templates')

@claims_bp.route('/claims')
def view_claims():
    return render_template('claims.html')