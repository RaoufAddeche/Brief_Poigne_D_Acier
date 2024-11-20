from init_db import engine
from sqlmodel import select, or_, col, Session
from models import Membres, Cours, Cartes_Acces, Coachs, Inscriptions


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

def obtenir_coach(id):
     with Session(engine) as session:
        return session.exec(select(Coachs).where(Coachs.id == id)).one()

        
        
        


# if __name__ == "__main__":
#     Main()
#     carte = Cartes_Acces(numero_unique=1)
#     ajouter_ligne(carte)
#     membre = Membres(nom="Jean Duparp", email="monemail@hotmail.fr", carte_acces_id=carte.id)
#     ajouter_ligne(membre)

