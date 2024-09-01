import smtplib
to= input("enter the reciptent \n")
content=input("enter the content \n")
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("maariraj302@gmail.com","**********")
    server.sendmail("username2@gmail.com",to,content)
    server.close()
sendmail(to,content)
