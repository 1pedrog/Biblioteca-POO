# inicialização da classe principal Client
class Client:
    def __init__(self, user_id, password, rentedBooks):
        self.user_id = user_id  #int
        self.password = password # str - minimo 6 caracteres  # str
        self.rentedBooks = rentedBooks  # int

# inicialização da subclasse estudante
class Student(Client):
    def __init__(self, user_id, password, rentedBooks, academicRecord):
        super().__init__(user_id, password, rentedBooks)
        self.academicRecord = academicRecord

# inicialização da subclasse professor
class Professor(Client):
    def __init__(self, user_id, password, rentedBooks, code):
        super().__init__(user_id, password, rentedBooks)
        self.code = code

# ------- criação dos usuarios -------

Estudante1 = Student(
    user_id=1,
    academicRecord="20242015020220",
    password="tantofaz",
    rentedBooks=[]
)

Estudante2 = Student(
    user_id=2,
    academicRecord="20242015020123",
    password="qualquercoisa",
    rentedBooks=[]
)

Professor1 = Professor(
    user_id=3,
    code="1234",
    password="senha",
    rentedBooks=[]
)

Professor2 = Professor(
    user_id=4,
    code="5678",
    password="seila",
    rentedBooks=[]
)

def login():

    # menu para saber a classe
    option = 0

    while option != 1 and option != 2:
        print("\ndigite sua ocupação:")
        print("1. Aluno")
        print("2. Professor")
        option = int(input())
        if option != 1 and option != 2:
            print("❌ Valor inválido!")
        else:
            print("✅ Ocupação selecionada!")

    if option == 1: # se a opção for aluno

        while True:
            AcademicRecord = input("Digite seu registro acadêmico (13 caracteres):\n")
            Password = input("Digite a senha:\n")

            if (AcademicRecord == Estudante1.academicRecord and Password == Estudante1.password) or (AcademicRecord == Estudante2.academicRecord and Password == Estudante2.password):
                print("\n✅ Login efetuado!")
                break
            else:
                print("\n❌ RA ou senha incorretos.")

    if option == 2: # se a opção for professor

        while True:
            Code = input("Digite seu código (4 caracteres):\n")
            Password = input("Digite a senha:\n")

            if Code == Professor1.code and Password == Professor1.password:
                print("\n✅ Login efetuado!")
                return Professor1.user_id
            elif Code == Professor2.code and Password == Professor2.password:
                print("\n✅ Login efetuado!")
                return Professor2.user_id
            else:
                print("\n❌ Código ou senha incorretos.")
