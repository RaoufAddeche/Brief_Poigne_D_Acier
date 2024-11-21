import streamlit as st
from generales_fonctions import afficher_navbar, sqmodel_to_dataframe, return_specialite_index
import utils as u
from models import Coachs

def radio_change():
    st.session_state.radio_change_admin = not st.session_state.radio_change_admin

if not "admin_state" in st.session_state:
    st.session_state.admin_state = 1
    st.session_state.radio_change_admin = False
    st.session_state.coach_list = u.obtenir_list_coachs()

afficher_navbar()

if st.session_state.admin_state in [0,1,2,3]:

    if st.button(label="Ajouter coach"):
        st.session_state.admin_state = 2
        
        
        
if st.session_state.admin_state == 1:
    
    #AFFICHAGE PANDAS
    # data = sqmodel_to_dataframe(st.session_state.coach_list)
    # st.dataframe(data=data)
    
     # # Show users table 
    colms = st.columns((1, 2, 2, 1, 1))
    fields = ["ID", 'NOM', 'SPECIALITE', 'Supprimer', 'Modifier']
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    for coach in st.session_state.coach_list:
        col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
        col1.write(coach.id) 
        col2.write(coach.nom)  
        col3.write(coach.specialite)
        button_phold = col4.empty()  # create a placeholder
        do_action = button_phold.button("❌", key=coach.id)
        if do_action:
                u.supprimer_coach(coach.id)
                st.session_state.coach_list = u.obtenir_list_coachs()
                st.rerun()
        button_phold_2 = col5.empty()  # create a placeholder
        do_action_2 = button_phold_2.button("Mod.", key=f"{coach.id}_2")
        if do_action_2:
                print("DEBUG")
                st.session_state.current_coach_id = coach.id
                st.session_state.admin_state = 3
                st.rerun()

if st.session_state.admin_state == 2:
    with st.form("Formulaire d'ajout de coach", clear_on_submit=True):
        input_nom = st.text_area("Nom")
        input_specialite = st.selectbox("Spécialité", ["Yoga", "Pump", "Pilates", "Musculation", "Boxe"])
        submitted = st.form_submit_button("Valider")
        if submitted:
            if input_nom.strip() != "":
                u.ajouter_ligne(Coachs(nom= input_nom, specialite=input_specialite))   
                st.write(":green[Coach ajouté avec succès!]")
            else:
                st.write(":red[Veuillez entrer un nom]") 
    
if st.session_state.admin_state == 3:

     with st.form("Formulaire de modification de coach", clear_on_submit=True):
        temp_coach = u.obtenir_coach(st.session_state.current_coach_id)
        input_nom = st.text_area("Nom", value=temp_coach.nom)
        input_specialite = st.selectbox("Spécialité", ["Yoga", "Pump", "Pilates", "Musculation", "Boxe"], return_specialite_index(temp_coach.specialite))
        submitted = st.form_submit_button("Valider")
        if submitted:
            if input_nom.strip() != "":
                temp_coach.nom = input_nom
                temp_coach.specialite = input_specialite
                u.ajouter_ligne(temp_coach)   
                st.write(":green[Coach modifié avec succès!]")
                st.session_state.admin_state = 1
                st.session_state.coach_list = u.obtenir_list_coachs()
                st.rerun()
            else:
                st.write(":red[Veuillez entrer un nom]") 


if st.session_state.admin_state == 4:
    st.write("Gestion des Cours")
    
if st.session_state.admin_state == 5:
    st.write("Gestion Membre")

st.sidebar.title("Gestion Admin")

choix =st.sidebar.radio("Que veux-tu faire ?", ["Gestion des Coachs","Gestion des Cours","Gestion Membres"], on_change=radio_change)

if choix == "Gestion des Coachs" :
    st.session_state.admin_state = 1

if choix == "Gestion des Cours" :
    st.session_state.admin_state = 4

if choix == "Gestion Membres" :
    st.session_state.admin_state = 5

if st.session_state.radio_change_admin:
    radio_change()
    st.rerun()
 