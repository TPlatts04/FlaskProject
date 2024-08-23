from flask import Flask, render_template, redirect, url_for, session, request
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if __name__ == "__main__":
    app.run(debug=True)