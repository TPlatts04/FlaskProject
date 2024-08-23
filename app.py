from flask import Flask, render_template, redirect, url_for, session, request
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)