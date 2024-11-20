import streamlit as st
from generales_fonctions import afficher_navbar, sqmodel_to_dataframe, return_specialite_index
import utils as u
from models import Coachs

if not "admin_state" in st.session_state:
    st.session_state.admin_state = 0
    st.session_state.modify_state = 1

afficher_navbar()

colA, colB, colC = st.columns(3)

with colA:
    if st.button(label="Gérer les coachs"):
        st.session_state.coach_list = u.obtenir_list_coachs()
        st.session_state.admin_state = 1

with colB:
    if st.button(label="Ajouter coach"):
        st.session_state.admin_state = 2
    

with colC:
    if st.button(label="Modifier coach"):
        st.session_state.admin_state = 3
       
    
        
if st.session_state.admin_state == 1:
    
    # data = sqmodel_to_dataframe(st.session_state.coach_list)
    # st.dataframe(data=data)
    
     # # Show users table 
    colms = st.columns((1, 2, 2, 1, 1))
    fields = ["ID", 'NOM', 'SPECIALITE', 'Supprimer']
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    for coach in st.session_state.coach_list:
        col1, col2, col3, col4 = st.columns((1, 2, 2, 1))
        col1.write(coach.id) 
        col2.write(coach.nom)  
        col3.write(coach.specialite)
        button_phold = col4.empty()  # create a placeholder
        do_action = button_phold.button("X", key=coach.id)
        if do_action:
                u.supprimer_coach(coach.id)
                st.session_state.coach_list = u.obtenir_list_coachs()
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
    if st.session_state.modify_state == 1:
        colms = st.columns((1, 2, 2, 1, 1))
        fields = ["ID", 'NOM', 'SPECIALITE', 'Selectionner']
        for col, field_name in zip(colms, fields):
            # header
            col.write(field_name)

        for coach in st.session_state.coach_list:
            col1, col2, col3, col4 = st.columns((1, 2, 2, 1))
            col1.write(coach.id) 
            col2.write(coach.nom)  
            col3.write(coach.specialite)
            button_phold = col4.empty()  # create a placeholder
            do_action = button_phold.button("Mod.", key=coach.id)
            if do_action:
                    st.session_state.current_coach_id = coach.id
                    st.session_state.modify_state = 2
                    st.rerun()
                    
                    
    if st.session_state.modify_state == 2:
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
                st.session_state.modify_state = 1
                st.session_state.coach_list = u.obtenir_list_coachs()
                st.rerun()
            else:
                st.write(":red[Veuillez entrer un nom]") 

 