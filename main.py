import streamlit as st
from generales_fonctions import afficher_navbar
from init_db import Main
from populate_db import peupler_bdd
import utils as u

def set_user():
    st.session_state.id_membre_actuel = u.obtenir_membre_par_nom(st.session_state.selectbox).id
    st.session_state.nom_membre_actuel = st.session_state.selectbox
    print(f"ID membre actuel  = {st.session_state.id_membre_actuel}")

if not "initialization" in st.session_state:
    #KEEP FOR FUTUR USE MAYBE
    Main()
    st.session_state.initialization = True
 
afficher_navbar()

 
if st.button("Générer BDD fictive"):
    peupler_bdd(50)
    
st.session_state.list_membres = u.obtenir_list_membres()

noms = []
for membre in st.session_state.list_membres:
    noms.append(membre.nom)

st.selectbox("Qui suis-je ?", noms, on_change=set_user, key = "selectbox")

