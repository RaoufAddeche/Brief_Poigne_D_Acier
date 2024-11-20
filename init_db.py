from sqlmodel import SQLModel, Session, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine= create_engine(sqlite_url, echo=True)


def Main():
    creer_BDD()

def creer_BDD():    
    SQLModel.metadata.create_all(engine)
    

