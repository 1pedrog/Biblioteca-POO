
##TODO: 4 classes Livro user emprestimo e biblioteca
##TODO: herança - aluno / professor
##TODO: metodo - emprestar livro / devolver livro listar emprestimos
##TODO: regra - não emprestar livros indisponiveis



from organizar_biblioteca import escolher_biblioteca
from Users_Login import login
from MenuUser import menu_user, mostrar_situacao
from BookSearch import start_book_search
from BookReturn import start_book_return

def main():
    biblioteca = escolher_biblioteca()
    usuario = login()

    while True:
        op = menu_user(usuario)
        if op == 1:
            start_book_search(usuario)
        elif op == 2:
            mostrar_situacao(usuario)
        elif op == 3:
            start_book_return(usuario)
        elif op == 4:
            print("Encerrando sessão...")
            break
        else:
            print("❌ Ação Inválida")

if __name__ == "__main__":
    main()