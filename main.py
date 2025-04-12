from flask import Flask
from login.login_routes import login_bp
from plans.plans_routes import plans_bp
from providers.providers_routes import providers_bp
from members.members_routes import members_bp
from claims.claims_routes import claims_bp

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(plans_bp)
app.register_blueprint(providers_bp)
app.register_blueprint(members_bp)
app.register_blueprint(claims_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
