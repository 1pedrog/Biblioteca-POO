from dataclasses import dataclass
from enum import Enum, auto
from Users_Login import Professor
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

    def return_book(self):  # ✅ ADICIONE ISSO
        self.book.copies += 1

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

    @staticmethod
    def filter_by_genre(book_view_models: list['BookViewModel'], genre: Genre) -> list['BookViewModel']:
        return [vm for vm in book_view_models if vm.book.genre == genre]


# -------------------- View --------------------
def show_book(vm: BookViewModel):
    print("\n📘 Livro:")
    print(f"ISBN: {vm.book.isbn}")
    print(vm.display())
    print("✅ Disponível" if vm.is_available() else "❌ Indisponível")


# -------------------- Main --------------------

def start_book_search(usuario):
    livros_vm = BookViewModel.load_from_json('Books.json')

    print("\n### Lista de livros:")
    for vm in livros_vm:
        show_book(vm)

    while True:
        isbn_input = input(
            "\nDigite o ISBN do livro que deseja alugar,\nou digite 'filtros' para buscar por gênero (ou 'sair' para encerrar): ").strip()

        if isbn_input.lower() == 'sair':
            print("Encerrando busca de livros...")
            break

        if isbn_input.lower() == 'filtros':
            print("\n🎯 Gêneros disponíveis:")
            for genre in Genre:
                print(f"- {genre.name.title()}")

            genero_input = input("Digite o nome do gênero desejado: ").strip().upper()

            # Tenta encontrar o gênero digitado
            genero_enum = next((g for g in Genre if g.name == genero_input), None)

            if genero_enum is None:
                print("❌ Gênero inválido.")
            else:
                livros_filtrados = BookViewModel.filter_by_genre(livros_vm, genero_enum)
                if not livros_filtrados:
                    print("⚠️ Nenhum livro encontrado para esse gênero.")
                else:
                    print(f"\n📚 Livros do gênero {genero_enum.name.title()}:")
                    for vm in livros_filtrados:
                        show_book(vm)

            continue  # <-- IMPORTANTE: Impede que vá para a verificação de ISBN

        livro_encontrado = None
        for vm in livros_vm:
            if vm.book.isbn == isbn_input:
                livro_encontrado = vm
                break

        if livro_encontrado is None:
            print(f"❌ Livro com ISBN '{isbn_input}' não encontrado. Tente novamente.")
            continue

        # Verifica limite de empréstimos
        limite_aluguel = 5 if isinstance(usuario, Professor) else 1

        if len(usuario.rentedBooks) >= limite_aluguel:
            print(f"❌ Limite de empréstimos atingido. Você só pode alugar até {limite_aluguel} livro(s).")
        else:
            if livro_encontrado.rent():
                print(f"✅ Livro '{livro_encontrado.book.title}' alugado com sucesso!")
                usuario.rentedBooks.append(livro_encontrado.book)
            else:
                print(f"❌ Livro '{livro_encontrado.book.title}' está indisponível para aluguel.")

        show_book(livro_encontrado)
