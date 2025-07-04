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