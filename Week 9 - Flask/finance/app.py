import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Obtain the data
    total = 0
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    stocks = db.execute("SELECT * FROM stocks WHERE id = ?", session["user_id"])

    # Calculate the overall money from stocks and update the real-time price
    for stock in stocks:
        price = lookup(stock["symbol"])["price"]
        stock.update({"price": price})
        total += (stock["shares"] * price)

    return render_template("index.html", stocks=stocks, cash=cash[0]["cash"], total=total+cash[0]["cash"])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Obtain the data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        stock = lookup(symbol)

        # Ensure symbol was submitted
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure symbol was valid
        if lookup(symbol) == None:
            return apology("invalid symbol", 400)

        # Ensure shares was submitted
        if not shares:
            return apology("missing shares", 400)

        # Ensure shares was valid
        try:
            if int(shares) <= 0:
                raise ValueError()
        except ValueError:
            return apology("invalid shares", 400)

        # Ensure the user can afford the stock
        balance = cash[0]["cash"] - (int(shares) * stock["price"])

        if balance < 0:
            return apology("can't afford", 400)

        # Add user's activity to history database. Reference for time: https://www.geeksforgeeks.org/get-current-date-and-time-using-python/#:~:text=Datetime%20module%20comes%20built%20into,current%20local%20date%20and%20time.
        db.execute("INSERT INTO history (id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], symbol.upper(), int(shares), stock["price"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Update user's stock after purchasing the stock
        holding = db.execute("SELECT shares FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol.upper())

        if not holding:
            db.execute("INSERT INTO stocks (id, symbol, name, shares, price) VALUES (?, ?, ?, ?, ?)",
                       session["user_id"], symbol.upper(), lookup(symbol)["name"], int(shares), stock["price"])
        else:
            db.execute("UPDATE stocks SET shares = shares + ? WHERE id = ? AND symbol = ?",
                       int(shares), session["user_id"], symbol.upper())

        # Update user's cash after purchasing the stock
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"])

        # Redirect user to home page
        flash("Bought!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Obtain the data
    stocks = db.execute("SELECT * FROM history WHERE id = ?", session["user_id"])
    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Obtain the data
        symbol = request.form.get("symbol")

        # Ensure symbol was submitted
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure symbol was valid
        if lookup(symbol) == None:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", symbol=lookup(symbol))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Obtain the data
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username is valid and it does not exist previously
        if not username or len(rows) == 1:
            return apology("username is not available", 400)

        # Ensure password is valid
        if not password:
            return apology("missing password", 400)

        # Ensure password confirmation matches password entered
        if not confirmation or (password != confirmation):
            return apology("passwords don't match", 400)

        # Insert username and password into the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username,
                   generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Registered!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # Obtain the data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        currStock = db.execute("SELECT shares FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol.upper())
        stock = lookup(symbol)

        # Ensure symbol was submitted
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure shares was submitted
        if not shares:
            return apology("missing shares", 400)

        # Ensure the user has sufficient stocks to be sold
        if not currStock or int(shares) > currStock[0]["shares"]:
            return apology("insufficient shares", 400)

        # Add user's activity to history database. Reference for time: https://www.geeksforgeeks.org/get-current-date-and-time-using-python/#:~:text=Datetime%20module%20comes%20built%20into,current%20local%20date%20and%20time.
        db.execute("INSERT INTO history (id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], symbol.upper(), -int(shares), stock["price"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Update user's stock after purchasing the stock
        db.execute("UPDATE stocks SET shares = shares - ? WHERE id = ? AND symbol = ?",
                   int(shares), session["user_id"], symbol.upper())

        # Update user's cash after purchasing the stock
        balance = cash[0]["cash"] + (int(shares) * stock["price"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"])

        # Remove stock with 0 share from the database
        currStock = db.execute("SELECT shares FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol.upper())

        if currStock[0]["shares"] == 0:
            db.execute("DELETE FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol.upper())

        # Redirect user to home page
        flash("Sold!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        stocks = db.execute("SELECT * FROM stocks WHERE id = ?", session["user_id"])
        return render_template("sell.html", stocks=stocks)


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Deposit money into account."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Obtain the data
        amount = request.form.get("amount")

        # Ensure amount was submitted
        if not amount:
            return apology("missing amount", 400)

        # Update user's cash after deposit
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, session["user_id"])

        # Redirect user to home page
        flash("Deposited!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("deposit.html")