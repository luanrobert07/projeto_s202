class GameCLI:
    def __init__(self, personagem_crud, school_crud, query):
        self.personagem_crud = personagem_crud
        self.school_crud = school_crud
        self.query = query

    def run(self):
        schools = self.school_crud.read_all()
        if schools:
            print("\nEscolas disponíveis:")
            for school in schools:
                print(school['name'])
        else:
            print("\nNenhuma escola criada ainda.")
        
        while True:
            print("\nGame Harry Potter")
            print("\nCrie as escolas precionando 5, caso não tenha nenhuma criada:")

            print("1. Create Personagem")
            print("2. Read Personagem")
            print("3. Update Personagem")
            print("4. Delete Personagem")
            print("5. Create School")
            print("6. Read School")
            print("7. Update School")
            print("8. Delete School")
            print("9. Add Personagem to School")
            print("10. Remove Personagem from School")
            print("11. Get Min Universitario Nome")
            print("12. Get Max Universitario Nome")
            print("13. Exit")
            choice = input("Enter your choice: ")

            if choice == '5':
                self.create_school()
            else:
                schools = self.school_crud.read_all()
                if not schools:
                    print("Você deve criar pelo menos uma escola antes de realizar outras operações.")
                else:
                    print("Escolas disponíveis:", ", ".join(school['name'] for school in schools))
                    if choice == '1':
                        self.create_personagem()
                    elif choice == '2':
                        self.read_personagem()
                    elif choice == '3':
                        self.update_personagem()
                    elif choice == '4':
                        self.delete_personagem()
                    elif choice == '6':
                        self.read_school()
                    elif choice == '7':
                        self.update_school()
                    elif choice == '8':
                        self.delete_school()
                    elif choice == '9':
                        self.add_personagem_to_school(schools)
                    elif choice == '10':
                        self.remove_personagem_from_school()
                    elif choice == '11':
                        self.get_min_universitario_nome()
                    elif choice == '12':
                        self.get_max_universitario_nome()
                    elif choice == '13':
                        break
                    else:
                        print("Invalid choice. Please try again.")

    def create_personagem(self):
        name = input("Enter name: ")
        self.personagem_crud.create(name)

    def read_personagem(self):
        name = input("Enter name: ")
        personagem = self.personagem_crud.read(name)
        if personagem:
            print("Personagem details:")
            print(f"Name: {personagem['name']}")
            print(f"School: {personagem['school']}")
        else:
            print("Personagem not found.")

    def update_personagem(self):
        name = input("Enter name: ")
        new_school = input("Enter new school: ")
        self.personagem_crud.update(name, new_school)

    def delete_personagem(self):
        name = input("Enter name: ")
        self.personagem_crud.delete(name)
    
    def create_school(self):
        name = input("Enter name: ")
        self.school_crud.create(name)

    def read_school(self):
        name = input("Enter name: ")
        school = self.school_crud.read(name)
        if school:
            print("School details:")
            print(f"Name: {school['name']}")
            print(f"Personagens: {', '.join(school['personagens'])}")
        else:
            print("School not found.")

    def update_school(self):
        name = input("Enter name: ")
        new_name = input("Enter new name: ")
        self.school_crud.update(name, new_name)

    def delete_school(self):
        name = input("Enter name: ")
        self.school_crud.delete(name)

    def add_personagem_to_school(self, schools):
        print("Escolha a escola para adicionar o personagem:")
        for i, school in enumerate(schools, 1):
            print(f"{i}. {school['name']}")
        choice = input("Enter the number of the school: ")
        if choice.isdigit() and 0 < int(choice) <= len(schools):
            school_name = schools[int(choice) - 1]['name']
            personagem_name = input("Enter personagem name: ")
            self.school_crud.add_personagem(school_name, personagem_name)
        else:
            print("Escolha inválida.")

    def remove_personagem_from_school(self):
        school_name = input("Enter school name: ")
        personagem_name = input("Enter personagem name: ")
        self.school_crud.remove_personagem(school_name, personagem_name)

    def get_min_universitario_nome(self):
        result = self.query.get_min_personagem_name()
        if result:  # Verifique se há resultados
            min_name_result = result[0]  # Acesse o primeiro resultado da lista
            print("Nome mínimo de personagem:", min_name_result['min_name'])
        else:
            print("Nenhum nome mínimo de personagem encontrado.")

    def get_max_universitario_nome(self):
        results = self.query.get_max_personagem_name()  # Obtenha a lista de resultados
        if results:  # Verifique se há resultados
            max_name_result = results[0]  # Acesse o primeiro resultado da lista
            print("Nome máximo de personagem:", max_name_result['max_name'])
        else:
            print("Nenhum nome máximo de personagem encontrado.")