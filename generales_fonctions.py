import streamlit as st

def afficher_navbar():
    with st.sidebar:
        st.subheader("Navigation")
        st.page_link("pages/app_membre.py", label="Membres")
        st.page_link("pages/app_admin.py", label="admin")