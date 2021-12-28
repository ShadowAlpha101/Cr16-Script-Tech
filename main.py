from flask import Flask, render_template, redirect, request, session
import mail_otp
import random
from flask_session import Session
global app
app  = Flask(__name__)
email = ' '
global mail_otp_bool
mail_otp_bool = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session["email"]   = request.form.get("email")
        session["mail_otp_bool"] = True

        return f"Hey {session['email']}"
    return render_template('portal.html', func=mail_otp.mail())

@app.route('/home', methods=["POST", "GET"])
def home():
    if not session.get("email"):
        return redirect('/login')
    return "Hi"


if __name__ == "__main__":
    app.run(debug=True)


