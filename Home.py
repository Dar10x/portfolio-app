import streamlit as st
import pandas

st.set_page_config(layout="wide",page_title="Nestor's Portfolio")
col1,col2 = st.columns(2,vertical_alignment="top")

with col1:
    st.image("images/photo.jpeg",width=200)


with col2:
    st.title("Nestor Dario Ari Machaca")
    content = """
    Hi, I am Nestor! 
    I am a student at Pontificia Universidad Catolica del Peru with a strong 
    focus on Data Science and Software Engineering. I have been developing in 
    Python since 2025 alongside a solid foundation in C and C++ where I 
    mastered complex data structures like trees and linked lists. 
    My background includes building Machine Learning models for business 
    strategy and designing robust database systems in Oracle SQL. 
    I hold an advanced English level and I am passionate about turning 
    raw data into actionable insights through NLP and predictive analytics.
    """
    st.write(content)

content2 = """
Check out my featured projects below
"""
st.subheader(content2)
st.write("Feel free to use whichever you want")

col3,empty_col,col4 = st.columns([1.5,0.3,1.5])
df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + f"{index+1}.png")
        st.link_button(label='Link',url=row["url"])
with col4:
    for index,row in df[2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + f"{index+1}.png")
        st.link_button(label='Link', url=row["url"])