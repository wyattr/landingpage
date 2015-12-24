from flask import Flask, render_template, request, url_for
application = Flask(__name__)
import smtplib

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There everyone!</h1>"



def sendNewSignUpEmail(email):
    #this stuff is copied from the interwebs, might be more succint way to accomplish 
    to = "w.ratliff1@gmail.com"
    gmail_user = "w.ratliff1@gmail.com"
    gmail_pwd = "*********" #needs to be app specific pw
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    subject = "New signup"
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + subject + '\n'
    msg = header + "Someone is interested in your product. \n Their email address is: " + email

    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()



@application.route("/signupComplete/", methods=['POST'])
def signupComplete():
    email = request.form['email']
    sendNewSignUpEmail(email)
    return "thanks for joining our mailing list"


@application.route("/moreinfo/")
def displayInfo():

    return render_template("signupForm.html")



if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
