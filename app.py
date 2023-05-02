import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from forms import SignForm, SeatForm





# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True


#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'SCRUM4'





@app.route("/", methods=['GET', 'POST'])
def user_options():
    return render_template("layout.html")


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = SignForm()
    return render_template("admin.html", form = form)

@app.route("/reservation", methods=['GET', 'POST'])
def reservations():
    form = SeatForm()
    return render_template("reservation.html", form = form)

app.run(host="0.0.0.0")