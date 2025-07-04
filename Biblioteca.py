##TODO: 4 classes Livro user emprestimo e biblioteca
##TODO: herança - aluno / professor
##TODO: metodo - emprestar livro / devolver livro listar emprestimos
##TODO: regra - não emprestar livros indisponiveis

from organizar_biblioteca import escolher_biblioteca
from BookSearch import start_book_search

def main():
    biblioteca = escolher_biblioteca()
    print(f"\nVocê escolheu a biblioteca: {biblioteca.name}")

    start_book_search()

if __name__ == "__main__":
    main()
