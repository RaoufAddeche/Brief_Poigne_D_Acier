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