from Users_Login import Professor

def mostrar_situacao(usuario):
    print(f"\n📚 Livros alugados por {usuario.__class__.__name__} ID {usuario.user_id}:")

    if not usuario.rentedBooks: #Se o usuário não alugou nenhum livro
        print("Nenhum livro alugado.")
    else: #Se ele tiver alugado algum livro
        for livro in usuario.rentedBooks: #Busca os livros alugados
            print(f"- {livro.title} por {livro.author}") #Mostra os livros alugados

    if isinstance(usuario, Professor): #Se o usuário for um professor
        livros_restantes = 5 - len(usuario.rentedBooks)
        print(f"📖 Ainda pode alugar {livros_restantes} livro(s).") #Mostra quantos livros ele ainda pode alugar


def menu_user(usuario):
    while True: #Enquanto o programa rodar
        op = 0
        print(f"\nBem-vindo, o que você deseja fazer?")
        print("1 - Alugar um livro")
        print("2 - Ver sua situação")
        print("3 - Devolver livro")
        print("4 - Sair do app")

        try: #Exceção criada para caso o cliente digite algo que não seja um número inteiro.
            op = int(input("Digite a opção: ")) #Repete a função se a opção digitada não for um número
        except ValueError:
            print("Entrada inválida. Apenas números aceitos.")
            continue
        return op
