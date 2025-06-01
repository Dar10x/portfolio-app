import streamlit as st
from send_emails import send_email

st.header("Contact Me")

with st.form(key = "email_forms",clear_on_submit=True) as form:
    user_email = st.text_input("Send me an email if you are interested on my work. I'll be glad to talk with you",placeholder='Enter your email')
    raw_message = st.text_area(label="Your message here",height=90,key='text')
    message = f"""\
Subject: I see your portfolio
{raw_message}
From {user_email}
"""
    button = st.form_submit_button("Submit",)
    if button:
        print(user_email)
        send_email(message)
        st.info("Your email was sent successfully")