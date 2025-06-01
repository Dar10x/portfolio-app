import streamlit as st

st.set_page_config(layout="centered")
col1,col2 = st.columns(2,vertical_alignment="center")

with col1:
    st.image("images/photo.png",width=200,use_container_width="auto")

with col2:
    st.title("Nestor Ari")
    content = """
    Hi, I am Nestor! Right now I am studying at Pontificia Universidad Catolica del Peru. I've been working with python since 2025.
    I also know how to code in C and C++. I have an advance level of english and can also work with data in SQL. 
    Here are my projects I have been working on
    """
    st.write(content,width=720)
