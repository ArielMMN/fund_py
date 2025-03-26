# Exercício 5
# Faça um programa que permita imprimir uma representação da tabela quadrada seguindo o padrão. 

t = int(input("digite tamanho: "))


for linha in range(t):
    for coluna in range(t):
        if linha %2 == 0 and coluna %2 == 0:
            print("x", end=" ")
        if linha %2 == 0 and coluna %2 == 1:
            print("0", end=" ")
        if linha %2 == 1 and coluna %2 == 0:
            print("*", end=" ")
        if linha %2 == 1 and coluna %2 == 1:
            print("&", end=" ")
    print()