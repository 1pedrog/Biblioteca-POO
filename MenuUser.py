from Users_Login import Professor, Student

def mostrar_situacao(usuario):
    print(f"\n📚 Livros alugados por {usuario.__class__.__name__} ID {usuario.user_id}:")

    if not usuario.rentedBooks:
        print("Nenhum livro alugado.")
    else:
        for livro in usuario.rentedBooks:
            print(f"- {livro.title} por {livro.author}")

    if isinstance(usuario, Professor):
        livros_restantes = 5 - len(usuario.rentedBooks)
        print(f"📖 Ainda pode alugar {livros_restantes} livro(s).")


def menu_user(usuario):
    while True:
        op = 0
        print(f"\nBem-vindo, o que você deseja fazer?")
        print("1 - Alugar um livro")
        print("2 - Ver sua situação")
        print("3 - Devolver livro")
        print("4 - Sair do app")

        try:
            op = int(input("Digite a opção: "))
        except ValueError:
            print("Entrada inválida. Apenas números aceitos.")
            continue
        return op
