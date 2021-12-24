from flask import Flask, render_template, redirect
import mail_otp
import random
global app
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('portal.html', func=mail_otp.mail())

@app.route('/home')
def home():
    return "Hello"
if __name__ == "__main__":
    app.run(debug=True)


