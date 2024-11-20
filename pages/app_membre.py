import streamlit as st
from generales_fonctions import afficher_navbar, sqmodel_to_dataframe
from models import Membres, Cours, Cartes_Acces, Inscriptions
from init_db import engine
from sqlmodel import select, or_, col, Session
import utils as u
import pandas as pd


afficher_navbar()

def Accueil_membre():

    st.image("nutrition.jpg")

def Consulter_cours():

    st.title ("Les cours disponibles")

    st.session_state.list_cours = u.obtenir_list_cours()
    data = sqmodel_to_dataframe(st.session_state.list_cours)
    st.dataframe(data=data)


def inscription_cours():

    st.title("Je veux m'inscrire")


def annuler_inscription():

    st.title("Je souhaite annuler un cours")


def Historique():

    st.title("Accès à mon historique")


#Menu mon compte 
 
st.title("Poigne d'Acier 🏋️‍♀️")
st.subheader("Nutrition & Mode de vie")
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