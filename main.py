import streamlit as st
from generales_fonctions import afficher_navbar
from init_db import Main
from populate_db import peupler_bdd

if not "initialization" in st.session_state:
    Main()
    st.session_state.initialization = True

afficher_navbar()

if st.button("Générer BDD fictive"):
    peupler_bdd(50)

