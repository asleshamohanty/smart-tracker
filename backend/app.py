from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Import db from models
from models import db  
db.init_app(app)

# ✅ Import routes AFTER initializing db
from routes import api  
app.register_blueprint(api)

# ✅ Corrected template rendering
@app.route("/")
def home():
    return render_template("index.html")  # ✅ Just "index.html"

@app.route("/login")
def login():
    return render_template("login.html")  # ✅ Just "login.html"

@app.route("/register")
def register():
    return render_template("register.html")  # ✅ Just "register.html"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ Ensure database tables are created
    app.run(debug=True)
