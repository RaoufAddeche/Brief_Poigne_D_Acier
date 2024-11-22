from sqlmodel import Field, SQLModel
import datetime

class Cartes_Acces(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    numero_unique: int
    __table_args__ = {'extend_existing': True} # Si la table existe déjà et vous souhaitez la redéfinir

class Membres(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key=True)
    nom: str = Field(index=True)
    email: str
    carte_acces_id: int | None = Field(default=None, foreign_key="cartes_acces.id")
    __table_args__ = {'extend_existing': True} 
 
class Coachs(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    specialite: str
    __table_args__ = {'extend_existing': True} 
        
class Cours(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    nom: str
    horaire: datetime.datetime
    capacite_max: int
    coach_id: int |None = Field(default=None, foreign_key="coachs.id")
    __table_args__ = {'extend_existing': True}
    
class Inscriptions(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key=True)
    membre_id: int |None = Field(default=None, foreign_key="membres.id")
    cours_id: int |None = Field(default=None, foreign_key="cours.id")
    date_inscription: datetime.datetime
    __table_args__ = {'extend_existing': True}


