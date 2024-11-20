import streamlit as st
import pandas as pd

def afficher_navbar():
    with st.sidebar:
        st.subheader("Navigation")
        st.page_link("pages/app_membre.py", label="Membres")
        st.page_link("pages/app_admin.py", label="admin")
        
def sqmodel_to_dataframe(items) -> pd.DataFrame:
    records = [i.dict() for i in items]
    df = pd.DataFrame.from_records(records)
    return df

def return_specialite_index(spe: str) -> int:
     match spe.lower():
        case "yoga":
            return 0
        case "pump":
            return 1
        case "pilates":
            return 2
        case "musculation":
            return 3
        case "boxe":
            return 4