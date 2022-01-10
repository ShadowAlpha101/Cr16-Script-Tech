from os import error
from flask import Flask, render_template, redirect, request, session
import mail_otp
import random
from flask_session import Session
import json 


global app
app  = Flask(__name__)
email = ' '
global mail_otp_bool
mail_otp_bool = False
logged_in = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
logged = False
x = False 

def func():
    global logged
    logged = True

def func_1():
    global x
    x = True
    print("Dhinchak Pooja")
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_bool = False
    try:
        if request.method == "POST" and logged:
            session["email"]   = request.form.get("email")
            session['password'] = request.form.get("password")
            session["mail_otp_bool"] = True
            mail_otp.mail()
            return render_template('portal.html', func=func(), error_bool=error_bool, mail_var=session['email'], password_var=session['password'], func_1=func_1())
        if request.method == "POST" and x:
            f = open('data.json')
            data = json.load(f)
            print("heh")
            print(data)
            return render_template('portal.html', func=func(), error_bool=error_bool, mail_var=session['email'], password_var=session['password'], func_1=func_1())
    except error:       
        error_bool = True
        return render_template('portal.html', func=func(), error_bool=error_bool, func_1=func_1())
    return render_template('portal.html', func=func(), error_bool=error_bool, func_1=func_1())
@app.route('/home', methods=["POST", "GET"])
def home():
    if not session.get("email"):
        return redirect('/login')
    return "Hi"

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/otp')
def otp():
    return render_template('otp.html')
if __name__ == "__main__":
    app.run(debug=True)


  
