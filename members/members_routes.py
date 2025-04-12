from flask import Blueprint, render_template

members_bp = Blueprint('members', __name__, template_folder='templates')

@members_bp.route('/members')
def view_members():
    return render_template('members.html')