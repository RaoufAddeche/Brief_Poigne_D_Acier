from init_db import engine
from sqlmodel import select, or_, col, Session
from models import Membres, Cours, Cartes_Acces, Coachs, Inscriptions
import datetime 


def ajouter_ligne(item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)

# def update_ligne(item):    
    

def obtenir_list_coachs():    
    with Session(engine) as session:
        return session.exec(select(Coachs)).all()

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
    
def obtenir_coach(id):
     with Session(engine) as session:
        return session.exec(select(Coachs).where(Coachs.id == id)).one()
     
def inscription_membre(membre_id, cours_id):
    with Session(engine) as session:
        inscription = Inscriptions(membre_id=membre_id, cours_id=cours_id, date_inscription= datetime.datetime(2024,11,21))
        session.add(inscription)
        session.commit()

def annuler_mon_inscription(cours_id,membre_id):
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

def obtenir_historique(membre_id):
    with Session(engine) as session:
        historique_client=  session.excec(select(Inscriptions).where(Inscriptions.membre_id == membre_id)).all()
        return historique_client



# if __name__ == "__main__":
#     Main()
#     carte = Cartes_Acces(numero_unique=1)
#     ajouter_ligne(carte)
#     membre = Membres(nom="Jean Duparp", email="monemail@hotmail.fr", carte_acces_id=carte.id)
#     ajouter_ligne(membre)

