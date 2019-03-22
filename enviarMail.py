import smtplib
user = 'lsystemsecuador@gmail.com'
pwd = '1509Charles*'
FROM = 'lsystemsecuador@gmail.com'
TO = 'pastorchessmaster@gmail.com'
SUBJECT = 'Saludo'
TEXT = 'Hola'
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, TO, SUBJECT, TEXT)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')
except:
    print('failed to send mail')