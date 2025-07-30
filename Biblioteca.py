
##TODO: 4 classes Livro user emprestimo e biblioteca
##TODO: herança - aluno / professor
##TODO: metodo - emprestar livro / devolver livro listar emprestimos
##TODO: regra - não emprestar livros indisponiveis



from organizar_biblioteca import escolher_biblioteca
from Users_Login import login
from MenuUser import menu_user, mostrar_situacao
from BookSearch import start_book_search
from BookReturn import start_book_return
from BookSearch import BookViewModel
import threading
import time

livros_vm = [] #Cria uma variável global que recebe a viewmodel responsável pela pesquisa e carregamento dos livros

def main():
    biblioteca = escolher_biblioteca() #Chama a função do seletor de bibliotecas
    usuario = login() #Chama a função de login do usuário

    def carregar_livros(): #Função que carrega os livros e armazena na variável global
        global livros_vm
        time.sleep(3) #Define tempo de carregamento
        livros_vm = BookViewModel.load_from_json('Books.json')
        print("\n✅ Livros carregados em segundo plano.")

    print("🔄 Iniciando carregamento dos livros...")
    thread = threading.Thread(target=carregar_livros) #Criação da thread
    thread.start() #Da início a Thread de execução
    print("🚀 Continuando execução do programa...") #Confirmação do carregamento em segundo plano

    while True: #Enquanto o usuário existir
        op = menu_user(usuario) #Chama a função de menu e admite seu valor para op
        if op == 1:
            thread.join() #Analisa se os dados estão prontos
            start_book_search(usuario, livros_vm) #Se 1 for digitado, chama a função de busca de livros
        elif op == 2:
            mostrar_situacao(usuario) #Se 2 for digitado, chama a função que mostra a situação do usuário
        elif op == 3:
            thread.join()
            start_book_return(usuario, livros_vm) #Se 3 for digitado, chama a função para devolver um livro
        elif op == 4:
            print("Encerrando sessão...")
            break #Se 4 for digitado, encerra o programa
        else:
            print("❌ Ação Inválida")

if __name__ == "__main__":
    main()