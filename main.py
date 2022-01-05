from os import error
from flask import Flask, render_template, redirect, request, session
import mail_otp
import random
from flask_session import Session
import json 
from flask_mail import Mail, Message


global app
app  = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'techinside1007@gmail.com'
app.config['MAIL_PASSWORD'] = 'cMH$<JBd65KxZzBc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mailer= Mail(app)
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
    print("lol")

def func_1():
    global x
    x = True

def turn():
    global x
    x = False
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_bool = False
    print(x)
    try:
        if request.method == "POST" and logged:
            session["email"]   = request.form.get("email")
            session['password'] = request.form.get("password")
            session["mail_otp_bool"] = True
            if session["mail_otp_bool"] :
                numbers = ["1","2","3","4","5","6","7","8","9","0"]
                alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                global otp
                otp = ""
                for i in range(3):
                    otp += random.choice(numbers)
                    otp += random.choice(alphabets)

                message = Message(
                            'OTP for Tech Inside',
                            sender ='techinside1007@gmail.com',
                            recipients = [session['email']]
                        )
                message.body = f'Your OTP for logging in is {otp}'
                mailer.send(message)
                print(otp)
                print("mail_sent")
        if request.method == "POST" and x:
            print("HAHAHAHAHAHAHAHAHAHAHA")
            turn()
            session['otp'] = request.form.get("otp")
            if session['otp'] == otp:
                return render_template('portal.html', func=func(), func_1=func_1(), error_bool=error_bool, mail_var=session['email'], password_var=session['password'])
            if session['otp'] != otp:
                print("WRONG OTP")
            return render_template('portal.html', func=func(), func_1=func_1(), error_bool=error_bool, mail_var=session['email'], password_var=session['password'])
    except error:       
        error_bool = True
        return render_template('portal.html', func=func(),func_1=func_1(), error_bool=error_bool)
    return render_template('portal.html', func=func(), func_1=func_1(), error_bool=error_bool)
@app.route('/home', methods=["POST", "GET"])
def home():
    if not session.get("email"):
        return redirect('/login')
    return "Hi"

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)