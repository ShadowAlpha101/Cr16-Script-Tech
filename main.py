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
otp_bool = False
x = False 

f = open('data.json')
data = json.load(f)
names = []
passwords = []
emails = []
office = []
employee = []
for x in data["details"]:
    names.append(x["name"])
    passwords.append(x["password"])
    emails.append(x["email"])
    office.append(x["office_code"])
    employee.append(x["employee_code"])
print(employee)
def login_request():
    global otp_bool
    opt_bool= True


def otp_request():
    global x
    x = True

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_bool = False
    session['incorrect_password'] = False
    session['incorrect_employee'] = False
    session['incorrect_office'] = False
    try:
        if request.method == "POST" and x:
            session["email"]   = request.form.get("email")
            session['password'] = request.form.get("password")
            session["mail_otp_bool"] = True
            session['office'] = request.form.get("office")
            session['employee'] = request.form.get("xyz")
            if session['email'] in emails:
                session['number'] = emails.index(session['email'])
                if session['password'] != passwords[session['number']]:
                    session['incorrect_password'] = True
                    print("NOT CORRECT PASSWORD")
                elif session['password'] == passwords[session['number']]:
                    print("CORRECT PASSWORD")
                    if session['office'] == office[session["number"]]:
                        if session['employee'] == employee[session['number']]:
                            mail_otp.mail()
                            return redirect("/otp", code=302)
                        elif session['emloyee'] != employee[session['number']]:
                            session['incorrect_employee'] = True
                            print("INCORRECT EMPLOYEE CODE")
                        elif session["employee"] == '':
                            client_login = True
                    elif session['office'] != office[session['number']]:
                            session['incorrect_office'] = True
                            print("INCORRECT OFFICE CODE")
                    elif session["office"] == "":
                        client_login = True
                        mail_otp.mail()
                        return redirect("/otp", code=302)
            return render_template('portal.html', error_bool=error_bool, mail_var=session['email'], password_var=session['password'], incorrect_password=session['incorrect_password'], ie=session['incorrect_employee'], io=session['incorrect_office'])
    except error:       
        error_bool = True
        return render_template('portal.html', error_bool=error_bool)
    return render_template('portal.html', error_bool=error_bool)
@app.route('/home', methods=["POST", "GET"])
def home():
    if not session.get("email"):
        return redirect('/login')
    return "Hi"

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if not session.get("email"):
        return redirect('/login')
    if request.method == "POST":
        return redirect('/dashboard')
    return render_template('otp.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
    