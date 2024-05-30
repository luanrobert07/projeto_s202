from CLI_game import GameCLI
from database import Database
from CRUD import PersonagemCRUD, SchoolCRUD
from query import Queries



db = Database("bolt://44.202.201.172:7687", "neo4j", "emitters-budgets-confidences") 

personagem_crud = PersonagemCRUD(db)
school_crud = SchoolCRUD(db)
query = Queries(db)

game_cli = GameCLI(personagem_crud, school_crud, query)
game_cli.run()

db.close()
