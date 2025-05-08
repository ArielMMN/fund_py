nome = input("Digite o nome: ")

while nome !="":
    telefone = input("Digte o telefone: ")
    with open("Contatos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{telefone}\n")
    nome = input("Digite o nome: ")


with open("contatos.txt", "r") as arquivo:
    for linha in arquivo.readline():
        nome, telefone = linha.strip().split(",")
        print(f"Nome: {nome}, Telefone: {telefone}")