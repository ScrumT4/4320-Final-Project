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
    if request.method == 'POST':
        username = request.form['user_name']
        password = request.form['password']
        if not username:
            flash("Must input Username")
        elif not password:
            flash("Must input Password")
        else:
           if username == "admin1" and password == "12345" or username == "admin2" and password == "24680" or username == "admin3" and password == "98765":
               return render_template("adminpage.html")
           else:
               flash("Login not authourized. please enter valid credentials")
    
    return render_template("admin.html")
    

@app.route("/reservation", methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      row = request.form['row']
      seat= request.form['seat']

      if not firstname:
        flash('Firstname is required!')
      elif not lastname:
        flash('Lastname is required!')
      elif not row:
        flash('Row is required!')
      elif not seat:
        flash('Seat is required!')
    return render_template("reservation.html")

app.run(host="0.0.0.0")