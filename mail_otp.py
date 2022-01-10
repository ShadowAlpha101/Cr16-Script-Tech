from flask import sessions
from main import app, random, redirect, email, mail_otp_bool, session
from flask_mail import Mail, Message

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'techinside1007@gmail.com'
app.config['MAIL_PASSWORD'] = 'cMH$<JBd65KxZzBc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mailer= Mail(app)

def mail():
    if session["mail_otp_bool"] :
        numbers = ["1","2","3","4","5","6","7","8","9","0"]
        alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
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
