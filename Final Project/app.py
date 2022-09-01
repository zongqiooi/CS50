from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session
from datetime import datetime

from helpers import apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///food.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def wheel():
    foods = db.execute("SELECT * FROM foods")
    return render_template("wheel.html", foods=foods)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Add food into wheel"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Obtain the data
        food = request.form.get("food")

        # Ensure food was submitted
        if not food:
            return apology("missing food", 400)

        # Add user's food to history database
        db.execute("INSERT INTO history (food, type, time) VALUES (?, ?, ?)", food, "ADDED", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Add food to food database
        db.execute("INSERT INTO foods (food) VALUES (?)", food)

        # Redirect user to home page
        flash("Added!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("add.html")


@app.route("/remove", methods=["GET", "POST"])
def remove():
    """Remove food from wheel"""

    if request.method == "POST":
        # Obtain the data
        food = request.form.get("food")

        # Ensure food was submitted
        if not food:
            return apology("missing food", 400)

        db.execute("DELETE FROM foods WHERE food = ?", food)

        # Remove user's food to history database
        db.execute("INSERT INTO history (food, type, time) VALUES (?, ?, ?)", food, "REMOVED", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Redirect user to home page
        flash("Removed!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        foods = db.execute("SELECT * FROM foods")
        return render_template("remove.html", foods=foods)


@app.route("/history")
def history():
    """List history of foods added or removed"""

    # Obtain the data
    histories = db.execute("SELECT * FROM history")
    return render_template("history.html", histories=histories)