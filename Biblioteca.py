
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
    biblioteca = escolher_biblioteca() #Chama a função do seletor de bibliotecas
    usuario = login() #Chama a função de login do usuário

    while True: #Enquanto o usuário existir
        op = menu_user(usuario) #Chama a função de menu e admite seu valor para op
        if op == 1:
            start_book_search(usuario) #Se 1 for digitado, chama a função de busca de livros
        elif op == 2:
            mostrar_situacao(usuario) #Se 2 for digitado, chama a função que mostra a situação do usuário
        elif op == 3:
            start_book_return(usuario) #Se 3 for digitado, chama a função para devolver um livro
        elif op == 4:
            print("Encerrando sessão...")
            break #Se 4 for digitado, encerra o programa
        else:
            print("❌ Ação Inválida")

if __name__ == "__main__":
    main()