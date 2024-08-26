from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from storeUser import *
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, password):
        self.name = name
        self.password = password

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username, password = request.form["username"], request.form["password"]
        session["username"], session["password"] = username, password
        found_user = users.query.filter_by(name=username).first()
        if found_user:
            if password == found_user.password:
                session["profileUsername"] = found_user.name
            else:
                flash("Incorrect Password. Please try again.")
                return render_template("login.html")
        else:
            flash("There is no account under this name. Please create one.")
            return render_template("login.html")
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route("/create_account", methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        username, password = request.form["create-username"], request.form["create-password"]
        session["username"], session["password"] = username, password
        found_user = users.query.filter_by(name=username).first()
        if found_user:
            flash("A user with this username already exists.", "info")
            return redirect(url_for("createAccount"))
        else:
            try:
                usr = users(username, password)
                userCreate(usr)
                db.session.add(usr)
                db.session.commit()
            except ValueError:
                flash("Password is Ineligible. Please try a new one.", "info")
                return render_template("createAccount.html")
        flash("Account created!")
        return render_template("createAccount.html")
    return render_template("createAccount.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)