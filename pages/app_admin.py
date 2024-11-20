import streamlit as st
from generales_fonctions import afficher_navbar, sqmodel_to_dataframe
import utils as u

if not "show_coaches" in st.session_state:
    st.session_state.show_coaches = False

afficher_navbar()



if st.button(label="Gérer les coachs"):
    st.session_state.coach_list = u.obtenir_list_coachs()
    st.session_state.show_coaches = True
        
if st.session_state.show_coaches:
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


