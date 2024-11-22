from init_db import engine
from sqlmodel import select, or_, col, Session
from models import Membres, Cours, Cartes_Acces, Coachs, Inscriptions
import datetime 


def ajouter_ligne(item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)

def obtenir_list_coachs():    
    with Session(engine) as session:
        return session.exec(select(Coachs)).all()
    
def obtenir_list_coachs_par_specialite(spe: str):
    with Session(engine) as session:
        return session.exec(select(Coachs).where(Coachs.specialite == spe)).all()

def supprimer_coach(id):
    with Session(engine) as session:
        coach = session.exec(select(Coachs).where(Coachs.id == id)).one()
        session.delete(coach)
        session.commit()
    
def supprimer_cours(id):
    with Session(engine) as session:
        cours = session.exec(select(Cours).where(Cours.id == id)).one()
        session.delete(cours)
        session.commit()

def obtenir_list_cours():    
    with Session(engine) as session:
        return session.exec(select(Cours)).all()
    
def obtenir_coach_par_id(id):
    with Session(engine) as session:
        return session.exec(select(Coachs).where(Coachs.id == id)).one_or_none()

def obtenir_coach_par_nom(nom):
    with Session(engine) as session:
        return session.exec(select(Coachs).where(Coachs.nom == nom)).first()
     
def inscription_membre(membre_id, cours_id):
    with Session(engine) as session:
        inscription = Inscriptions(membre_id=membre_id, cours_id=cours_id, date_inscription= datetime.datetime(2024,11,21))
        session.add(inscription)
        session.commit()

def annuler_mon_inscription(cours_id,membre_id):
    print(f"DEBUG : Membre id = {membre_id} ; Cours_id = {cours_id}")
    with Session(engine) as session:
        annulation = session.exec(select(Inscriptions).where(Inscriptions.membre_id== membre_id,Inscriptions.cours_id== cours_id)).one()
        session.delete(annulation)
        session.commit()
        
def obtenir_inscription(id):
    with Session(engine) as session:
        obtention_membre = session.exec(select(Inscriptions).where(Inscriptions.membre_id== id)).all()
        return obtention_membre

def obtenir_cours(id):
    with Session(engine) as session:
        obtention_membre = session.exec(select(Cours).where(Cours.id== id)).one()
        return obtention_membre

def supprimer_cours(id):
    with Session(engine) as session:
        cours_du_membre= session.exec(select(Cours).where(Cours.id == id)).one()
        session.delete(cours_du_membre)
        session.commit()

def obtenir_membres_inscrits(cours_id):
    with Session(engine) as session:
        membres_inscrits = session.exec(select(Inscriptions, Membres).join(Membres, Membres.id == Inscriptions.membre_id).where(Inscriptions.cours_id== cours_id)).all()

        inscrits = []

        for inscription, i in membres_inscrits:
            inscrits.append(i)

        return inscrits




# if __name__ == "__main__":
#     Main()
#     carte = Cartes_Acces(numero_unique=1)
#     ajouter_ligne(carte)
#     membre = Membres(nom="Jean Duparp", email="monemail@hotmail.fr", carte_acces_id=carte.id)
#     ajouter_ligne(membre)

