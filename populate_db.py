import faker
from utils import ajouter_ligne
from models import Cours, Cartes_Acces, Membres, Coachs, Inscriptions
from random import randint
from sqlmodel import select, Session
from init_db import engine, Main

fake = faker.Faker("fr_FR")

def peupler_bdd(max: int):
    for x in range(0, max):
        carte = Cartes_Acces(numero_unique=x+(fake.random_digit_not_null()*fake.random_digit_not_null()))
        ajouter_ligne(carte)
        membre = Membres(nom=fake.name(), email=fake.email(), carte_acces_id=carte.id)
        ajouter_ligne(membre)
        
    for x in range(0, int(max/4)):
        coach = Coachs(nom=fake.name(), specialite=random_specialité())
        ajouter_ligne(coach)
        

def random_specialité()-> str:
    x = randint(1, 5)
    match x:
        case 1:
            return "Yoga"
        case 2:
            return "Pump"
        case 3:
            return "Pilates"
        case 4:
            return "Musculation"
        case 5:
            return "Boxe"
        
if __name__ == "__main__":
    Main()
    peupler_bdd(100)
