
from BookSearch import BookViewModel, show_book

def start_book_return(usuario, livros_vm):
    if not usuario.rentedBooks:
        print("\n❌ Você não possui livros para devolver.")
        return

    print("\n📚 Seus livros alugados:")
    for livro in usuario.rentedBooks:
        print(f"- {livro.title} (ISBN: {livro.isbn})")

    isbn_input = input("\nDigite o ISBN do livro que deseja devolver: ").strip()

    livro_para_devolver = None
    for livro in usuario.rentedBooks:
        if livro.isbn == isbn_input:
            livro_para_devolver = livro
            break

    if livro_para_devolver is None:
        print("❌ ISBN não encontrado na sua lista de empréstimos.")
        return

    # Cria um ViewModel temporário para chamar o metodo return_book
    vm = next((v for v in livros_vm if v.book.isbn == livro_para_devolver.isbn), None)
    if vm is None:
        print("⚠️ Erro interno: livro não encontrado nos dados carregados.")
        return
    vm.return_book()
    usuario.rentedBooks.remove(livro_para_devolver)

    print(f"✅ Livro '{livro_para_devolver.title}' devolvido com sucesso!")

