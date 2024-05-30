class Queries:
    def __init__(self, db):
        self.db = db

    def get_min_personagem_name(self):
        query = "MATCH (n:Personagem) RETURN MIN(n.name) AS min_name"
        return self.db.execute_query(query)


    def get_max_personagem_name(self):
        query = "MATCH (n:Personagem) RETURN MAX(n.name) AS max_name"
        return self.db.execute_query(query)
