class PersonagemCRUD:
    def __init__(self, conn):
        self.conn = conn

    def create(self, name):
        query = """
        CREATE (p:Personagem {name: $name})
        """
        self.conn.execute_query(query, parameters={"name": name})
        print("Personagem created successfully.")

    def read(self, name):
        query = """
        MATCH (p:Personagem {name: $name})-[:BELONGS_TO]->(s:School)
        RETURN p.name AS name, s.name AS school
        """
        result = self.conn.execute_query(query, parameters={"name": name})
        return result[0] if result else None

    def update(self, name, new_school):
        query = """
        MATCH (p:Personagem {name: $name})-[r:BELONGS_TO]->(s:School)
        DELETE r
        MERGE (new_s:School {name: $new_school})
        MERGE (p)-[:BELONGS_TO]->(new_s)
        """
        self.conn.execute_query(query, parameters={"name": name, "new_school": new_school})
        print("Personagem updated successfully.")

    def delete(self, name):
        query = """
        MATCH (p:Personagem {name: $name})
        DETACH DELETE p
        """
        self.conn.execute_query(query, parameters={"name": name})
        print("Personagem deleted successfully.")

class SchoolCRUD:
    def __init__(self, conn):
        self.conn = conn

    def create(self, name):
        query = """
        MERGE (s:School {name: $name})
        """
        self.conn.execute_query(query, parameters={"name": name})
        print("School created successfully.")

    def read(self, name):
        query = """
        MATCH (s:School {name: $name})
        OPTIONAL MATCH (s)<-[:BELONGS_TO]-(p:Personagem)
        RETURN s.name AS name, collect(p.name) AS personagens
        """
        result = self.conn.execute_query(query, parameters={"name": name})
        return result[0] if result else None

    def update(self, name, new_name):
        query = """
        MATCH (s:School {name: $name})
        SET s.name = $new_name
        """
        self.conn.execute_query(query, parameters={"name": name, "new_name": new_name})
        print("School updated successfully.")

    def delete(self, name):
        query = """
        MATCH (s:School {name: $name})
        DETACH DELETE s
        """
        self.conn.execute_query(query, parameters={"name": name})
        print("School deleted successfully.")
    
    def add_personagem(self, school_name, personagem_name):
        # Verificar se o personagem já existe
        personagem_exists_query = """
        MATCH (p:Personagem {name: $personagem_name})
        RETURN p
        """
        personagem_exists_result = self.conn.execute_query(personagem_exists_query, parameters={"personagem_name": personagem_name})
        
        # Se o personagem já existir, relacioná-lo à escola
        if personagem_exists_result:
            add_relation_query = """
            MATCH (s:School {name: $school_name}), (p:Personagem {name: $personagem_name})
            MERGE (p)-[:BELONGS_TO]->(s)
            """
            self.conn.execute_query(add_relation_query, parameters={"school_name": school_name, "personagem_name": personagem_name})
            print("Personagem added to school successfully.")
        else:
            print("Personagem does not exist. Please create the personagem first.")

    def remove_personagem(self, school_name, personagem_name):
        query = """
        MATCH (p:Personagem {name: $personagem_name})-[r:BELONGS_TO]->(s:School {name: $school_name})
        DELETE r
        """
        self.conn.execute_query(query, parameters={"school_name": school_name, "personagem_name": personagem_name})
        print("Personagem removed from school successfully.")


    def read_all(self):
        query = "MATCH (s:School) RETURN s.name AS name"
        return self.conn.execute_query(query)
