import streamlit as st
from generales_fonctions import afficher_navbar, sqmodel_to_dataframe
import utils as u

if not "show_coaches" in st.session_state:
    st.session_state.show_coaches = False

afficher_navbar()



if st.button(label="Gérer les coachs"):
    st.session_state.coach_list = u.obtenir_list_coachs()
    st.session_state.show_coaches = True
        
col1, col2, col3, col4, col5 = st.columns(5)
if st.session_state.show_coaches:
    i = 0
    data = sqmodel_to_dataframe(st.session_state.coach_list)
    st.dataframe(data=data)
    # for coach in st.session_state.coach_list:
    #     with col1:
    #         st.write(f"ID : {coach.id}")
    #     with col2:
    #         st.write(f"Nom : {coach.nom}")
    #     with col3:
    #         st.write(f"Specialité : {coach.specialite}")
    #     with col4:
    #         if st.button(label="Supprimer", key=f"c_button_{coach.id}"):
    #             u.supprimer_coach(coach.id)
    #             st.session_state.coach_list = u.obtenir_list_coachs()
    #             st.rerun()
    #     with col5:
    #         st.button(label="test2", key=f"c_button_2_{i}")
        
        # i+=1

