
##TODO: 4 classes Livro user emprestimo e biblioteca
##TODO: herança - aluno / professor
##TODO: metodo - emprestar livro / devolver livro listar emprestimos
##TODO: regra - não emprestar livros indisponiveis


from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    genre: str
    pages: int
    isRented: bool

@dataclass
class Cliente:
    nome: str
    livrosAlugados: [Book]
    idade: int
    isMale: bool

book1 = Book( ##aqui foi criado o livro
    title="1984",
    author="George Orwell",
    year=1949,
    genre="Dystopian",
    pages=328
)

print(book1)
print(f"{book1.title} foi escrito por {book1.author} em {book1.year}.")