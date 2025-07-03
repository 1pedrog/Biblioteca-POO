from dataclasses import dataclass
from enum import Enum, auto
import json

# -------------------- Model --------------------
class Genre(Enum):
    FICTION = auto()
    NONFICTION = auto()
    MYSTERY = auto()
    SCIENCE_FICTION = auto()
    FANTASY = auto()
    BIOGRAPHY = auto()
    HISTORY = auto()
    CHILDREN = auto()

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    genre: Genre
    copies: int


# -------------------- ViewModel -------------------

class BookViewModel:
    def __init__(self, book: Book):
        self.book = book

    def display(self) -> str:
        return f"{self.book.title} by {self.book.author} ({self.book.genre.name})"

    def is_available(self) -> bool:
        return self.book.copies > 0

    def rent(self) -> bool:
        """
        Aluga uma cópia do livro, se disponível.
        Retorna True se o aluguel foi feito, False se não tinha cópias.
        """
        if self.is_available():
            self.book.copies -= 1
            return True
        else:
            return False

    @staticmethod
    def load_from_json(file_path: str) -> list['BookViewModel']:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        books_vm = []
        for item in data:
            genre = Genre[item['genre']]
            book = Book(
                isbn=item['isbn'],
                title=item['title'],
                author=item['author'],
                genre=genre,
                copies=item['copies']
            )
            books_vm.append(BookViewModel(book))
        return books_vm


# -------------------- View --------------------
def show_book(vm: BookViewModel):
    print("\n📘 Livro:")
    print(f"ISBN: {vm.book.isbn}")
    print(vm.display())
    print("✅ Disponível" if vm.is_available() else "❌ Indisponível")


# -------------------- Main --------------------

def start_book_search():
    livros_vm = BookViewModel.load_from_json('Books.json')

    print("\n### Lista de livros:")
    for vm in livros_vm:
        show_book(vm)

    while True:
        isbn_input = input("\nDigite o ISBN do livro que deseja alugar (ou 'sair' para encerrar): ").strip()
        if isbn_input.lower() == 'sair':
            print("Encerrando busca de livros...")
            break

        livro_encontrado = None
        for vm in livros_vm:
            if vm.book.isbn == isbn_input:
                livro_encontrado = vm
                break

        if livro_encontrado is None:
            print(f"❌ Livro com ISBN '{isbn_input}' não encontrado. Tente novamente.")
            continue

        if livro_encontrado.rent():
            print(f"✅ Livro '{livro_encontrado.book.title}' alugado com sucesso!")
        else:
            print(f"❌ Livro '{livro_encontrado.book.title}' está indisponível para aluguel.")

        show_book(livro_encontrado)
