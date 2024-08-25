from flask import Flask, render_template, redirect, url_for, session, request, flash
from storeUser import *
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username, password = request.form["username"], request.form["password"]
        try:
            userLogin(username, password)
            session["profileUsername"] = username
        except ValueError:
            flash("There is no account under this name. Please create one.")
            return render_template("login.html")
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route("/create_account", methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        username, password = request.form["create-username"], request.form["create-password"]
        try:
            userCreate(username, password) 
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
    main()
    app.run(debug=True)