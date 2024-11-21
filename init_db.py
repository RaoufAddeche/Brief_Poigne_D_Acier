from sqlmodel import SQLModel, create_engine



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine= create_engine(sqlite_url, echo=False)


def Main():
    SQLModel.metadata.create_all(engine)

def creer_BDD():    
   pass

if __name__ == "__main__":
    Main()
