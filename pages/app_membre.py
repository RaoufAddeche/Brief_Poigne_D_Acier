import streamlit as st
from generales_fonctions import afficher_navbar, sqmodel_to_dataframe
from models import Membres, Cours, Cartes_Acces, Inscriptions, Coachs
from init_db import engine
from sqlmodel import select, or_, col, Session
import utils as u
import pandas as pd


afficher_navbar()
if not "membre_state" in st.session_state:
    st.session_state.membre_state = 0
    st.session_state.id_membre_actuel = 9

def Accueil_membre():
    st.subheader("Nutrition & Mode de vie")
    st.image("nutrition.jpg")

def Consulter_cours():

    st.title ("Les cours disponibles")

    st.session_state.list_cours = u.obtenir_list_cours()
    data = sqmodel_to_dataframe(st.session_state.list_cours)
    st.dataframe(data=data)


def inscription_cours():

    st.title("Je veux m'inscrire")
     # # Show users table
    st.session_state.list_cours = u.obtenir_list_cours()
    st.session_state.coach_list = u.obtenir_list_coachs()
    
    colms = st.columns((1, 2, 2, 1, 1))
    fields = ["Coach", 'Horaire', 'Specialité', 'inscription']
    
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    for cours,coach in zip(st.session_state.list_cours,st.session_state.coach_list):
        col1, col2, col3, col4 = st.columns((1, 2, 2, 1))

        col1.write(coach.nom) 
        col2.write(cours.horaire)  
        col3.write(cours.nom)
        button_phold = col4.empty()  # create a placeholder

        do_action = button_phold.button("✅", key=cours.id)
        
        if do_action:
            u.inscription_membre(st.session_state.id_membre_actuel,cours.id)
            st.session_state.list_cours = u.obtenir_list_cours()
            st.rerun()

def annuler_inscription():

    st.title("Je souhaite annuler un cours")
    st.session_state.list_inscriptions_actuel = u.obtenir_inscription(st.session_state.id_membre_actuel)

    colms = st.columns((2, 1, 2))
    fields = ['Horaire', 'Nom', 'inscription']
        
    for col, field_name in zip(colms, fields):
        col.write(field_name)


    for inscription in st.session_state.list_inscriptions_actuel:
        col1, col2, col3 = st.columns((2,1,2))
 
        col1.write(inscription.date_inscription)  
        col2.write(inscription.id)
        button_phold = col3.empty()
        do_action = button_phold.button("X", key=inscription.id)
        if do_action:
            st.write(inscription.id)
            st.write(st.session_state.id_membre_actuel)
            u.annuler_mon_inscription(inscription.cours_id, st.session_state.id_membre_actuel)
            st.session_state.list_inscriptions_actuel = u.obtenir_inscription(st.session_state.id_membre_actuel)
            st.rerun()




def Historique():

    st.title("Accès à mon historique")


#Menu mon compte 
 
st.title("Poigne d'Acier 🏋️‍♀️")
st.sidebar.title("Mon compte")


choix =st.sidebar.radio("Que veux-tu faire ?", ["Accueil","Consulter les cours disponibles","S'inscrire à un cours", "Annuler une inscription", "Mon historique"])

if choix == "Consulter les cours disponibles" :
    Consulter_cours() 
    


elif choix == "S'inscrire à un cours" :
    inscription_cours()
    pass


elif choix == "Annuler une inscription":
    annuler_inscription()
    pass

elif choix == "Mon historique" : 
    Historique()
    pass

else:
    choix == "Accueil"
    Accueil_membre()

