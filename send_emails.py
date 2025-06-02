import smtplib, ssl,os
import streamlit as st


def send_email(message):
    host = st.secrets["database"]["host"]
    port = 465
    username = st.secrets["database"]["username"]
    password = st.secrets["database"]["password"]
    receiver = st.secrets["database"]["receiver"]
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver,message)