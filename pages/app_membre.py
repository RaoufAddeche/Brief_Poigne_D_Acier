import streamlit as st
from generales_fonctions import afficher_navbar
from models import Membres, Cours, Cartes_Acces, Inscriptions
from init_db import engine
from sqlmodel import select, or_, col, Session



afficher_navbar()



def Consulter_cours():

    st.title ("Les cours disponibles")
    with Session(engine) as session:
        statement = select(Cours)
        results= session.exec(statement) 
        for cours in results:
            print(cours)



def inscription_cours():

    st.title("Je veux m'inscrire")


def annuler_inscription():

    st.title("Je souhaite annuler un cours")


def Historique():

    st.title("Accès à mon historique")


#Menu mon compte 
 
st.title("Poigne d'Acier 🏋️‍♀️")
st.subheader("Nutrition & Mode de vie")
st.image("nutrition.jpg")
st.sidebar.title("Mon compte")



choix =st.sidebar.radio("Que veux-tu faire ?", ["Consulter les cours disponibles","S'inscrire à un cours", "Annuler une inscription", "Mon historique"])

if choix == "Consulter les cours disponibles" :
    Consulter_cours() 
    pass


elif choix == "S'inscrire à un cours" :
    inscription_cours()
    pass


elif choix == "Annuler une inscription":
    annuler_inscription()
    pass

elif choix == "Mon historique" : 
    Historique()
    pass