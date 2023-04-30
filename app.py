import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'

@app.route("/", methods=['GET', 'POST'])
def user_options():

    return render_template("index.html")


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    
    return render_template("admin.html")

@app.route("/reservation", methods=['GET', 'POST'])
def reservations():

    return render_template("reservations.html")

app.run(host="0.0.0.0")