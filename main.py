import streamlit as st
import pandas

st.set_page_config(layout="wide",page_title="Nestor's Portfolio")
col1,col2 = st.columns(2,vertical_alignment="top")

with col1:
    st.image("images/photo.png",width=200)


with col2:
    st.title("Nestor Ari")
    content = """
    Hi, I am Nestor! Right now I am studying at Pontificia Universidad Catolica del Peru. I've been working with python since 2025.
    I also know how to code in C and C++. I have an advance level of english and can also work with data in SQL. 
    Here are my projects I have been working on.
    """
    st.write(content)

content2 = """
Below you can find my python projects. 
"""
st.subheader(content2)
st.write("Feel free to use whichever you want")

col3,empty_col,col4 = st.columns([1.5,0.3,1.5])
df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + f"{index+1}.png")
        st.link_button(label='Link',url=row["url"])
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + f"{index+1}.png")
        st.link_button(label='Link', url=row["url"])