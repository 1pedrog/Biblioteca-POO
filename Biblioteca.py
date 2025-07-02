
##TODO: 4 classes Livro user emprestimo e biblioteca
##TODO: herança - aluno / professor
##TODO: metodo - emprestar livro / devolver livro listar emprestimos
##TODO: regra - não emprestar livros indisponiveis

#Criação da classe Biblioteca
class Biblioteca:
    def __init__(self, name, address, idBiblioteca):
        self.name = name
        self.address = address
        self.idBiblioteca = idBiblioteca
    def exibir(self): #Metodo para exibir as informações das Bibliotecas
        print("-" * 50)
        print(f"Biblioteca: {self.name}\nEndereço: {self.address}\nID: {self.idBiblioteca}")
        print("-" * 50)

#Criação da classe Book
class Book:
    def __init__(self, title, author, year, genre, pages, isRented):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.isRented = isRented

#Criação da classe Cliente
class Cliente:
    def __init__(self, nome, livrosAlugados, idade, isMale):
        self.nome = nome
        self.livrosAlugados = livrosAlugados  # Lista de objetos Book
        self.idade = idade
        self.isMale = isMale

#Lista com 5 Bibliotecas
dados_bibliotecas = [
    ("Biblioteca Paulo Freire", "Rua Dona Leopoldina, 907", 1),
    ("Biblioteca Dolor Barreira", "Avenida da Universidade, 2572", 2),
    ("Biblioteca Engenheiro Waldyr Diogo de Siqueira", "Avenida Treze de Maio, 2081", 3),
    ("Biblioteca Professor Ari de Sá Cavalcante", "Avenida da Universidade, 2700", 4),
    ("Biblioteca Rachel de Queiroz", "Rua Gen. Clarindo de Queiroz, 1740", 5),
]
#Adiciona as informações da lista à classe Biblioteca
bibliotecas = [Biblioteca(name, address, idBiblioteca) for name, address, idBiblioteca in dados_bibliotecas]

book1 = Book( ##aqui foi criado o livro
    title="1984",
    author="George Orwell",
    year=1949,
    genre="Dystopian",
    pages=328,
    isRented=False
)
client1 = Cliente( ##aqui foi criado o cliente
    nome="João Silva",
    livrosAlugados=[],
    idade=30,
    isMale=True
)

print(f"Gênero: {book1.genre}, Páginas: {book1.pages}, Disponível: {not book1.isRented}")
print(f"Cliente: {client1.nome}, Idade: {client1.idade}, Gênero: {'Masculino' if client1.isMale else 'Feminino'}")

#Seletor de Bibliotecas
print("Bibliotecas disponíveis:")
for b in bibliotecas:
    print(f"ID - {b.idBiblioteca}: {b.name}") #Mostra todas Bibliotecas e seus IDs
loop= True #Loop para continuar pedindo um ID existente
while loop==True:
    id_escolhido = int(input("Digite o ID da Biblioteca que deseja acessar: ")) #Cliente escolhe a Biblioteca pelo ID
    bibliotecaEncontrada= False #Define um padrão para quando o ID escolhido não existir
    for b in bibliotecas:
        #Se o ID existir
        if b.idBiblioteca == id_escolhido:
            b.exibir() #Exibe os dados da Biblioteca escolhida
            bibliotecaEncontrada = True
            loop = False #Fim do loop
            break
    #Se o ID não existir
    if not bibliotecaEncontrada:
        print("Biblioteca não Encontrada") #Loop continuará até o ID digitado existir