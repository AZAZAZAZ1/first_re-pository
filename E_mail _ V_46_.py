import smtplib

def send_mail (email, password, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, password)
    server.sendmail( email , email, message)
    server.quit()
send_mail("a1160azz@gmail.com","Password@2Password@2", "how are you")

# refer to vedio 98 learn python ....

# go to google security and turn " on " less secure app access

# the above command works sucessfuly .
