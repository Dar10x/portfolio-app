import smtplib, ssl,os


def send_email(message):
    host = os.getenv("HOST")
    port = 465
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("USERNAME")
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver,message)