#Criação da classe Biblioteca
class Biblioteca:
    def __init__(self, name, address, idBiblioteca):
        self.name = name
        self.address = address
        self.idBiblioteca = idBiblioteca
    def exibir(self): #Metodo para exibir as informações das Bibliotecas
        print("-" * 50)
        print(f"Biblioteca: {self.name}\nEndereço: {self.address}\nID: {self.idBiblioteca}")
        print("-" * 50)

#Lista com 5 Bibliotecas
dados_bibliotecas = [
    ("Biblioteca Paulo Freire", "Rua Dona Leopoldina, 907", 1),
    ("Biblioteca Dolor Barreira", "Avenida da Universidade, 2572", 2),
    ("Biblioteca Engenheiro Waldyr Diogo de Siqueira", "Avenida Treze de Maio, 2081", 3),
    ("Biblioteca Professor Ari de Sá Cavalcante", "Avenida da Universidade, 2700", 4),
    ("Biblioteca Rachel de Queiroz", "Rua Gen. Clarindo de Queiroz, 1740", 5),
]
#Adiciona as informações da lista à classe Biblioteca
bibliotecas = [Biblioteca(name, address, idBiblioteca) for name, address, idBiblioteca in dados_bibliotecas]

#Seletor de Bibliotecas
print("Bibliotecas disponíveis:")
for b in bibliotecas:
    print(f"ID - {b.idBiblioteca}: {b.name}") #Mostra todas Bibliotecas e seus IDs
loop= True #Loop para continuar pedindo um ID existente
while loop==True:
    try:
        id_escolhido = int(input("Digite o ID da Biblioteca que deseja acessar: "))  # Cliente escolhe a Biblioteca pelo ID
    except ValueError:
        print("Entrada inválida. Digite apenas números.") #Mensagem de erro caso cliente digite algo que não seja número
        continue
    bibliotecaEncontrada= False #Define um padrão para quando o ID escolhido não existir
    for b in bibliotecas:
        #Se o ID existir
        if b.idBiblioteca == id_escolhido:
            b.exibir() #Exibe os dados da Biblioteca escolhida
            bibliotecaEncontrada = True
            loop = False #Fim do loop
            break
    #Se o ID não existir
    if not bibliotecaEncontrada:
        print("Biblioteca não Encontrada") #Loop continuará até o ID digitado existir