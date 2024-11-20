from sqlmodel import Field, SQLModel
import datetime

class Cartes_Acces(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    numero_unique: int

class Membres(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key=True)
    nom: str = Field(index=True)
    email: str
    carte_acces_id: int | None = Field(default=None, foreign_key="cartes_acces.id")
 
class Coachs(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    specialite: str
        
class Cours(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    nom: str
    horaire: datetime.datetime
    capacite_max: int
    coach_id: int |None = Field(default=None, foreign_key="coachs.id")
    
class Inscriptions(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key=True)
    membre_id: int |None = Field(default=None, foreign_key="membres.id")
    cours_id: int |None = Field(default=None, foreign_key="cours.id")
    date_inscription: datetime.datetime


