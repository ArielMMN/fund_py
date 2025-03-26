# Exercício 4
# Faça um programa que permita imprimir uma represetação de tabela quadrada com $ e @. 
# Nesta tabela o triangulo inferior esquerdo deve ser preenchido com $ e o triângulo superior direito deve ser preenchido com @.

t = int(input("digite tamanho: "))


for linha in range(t):
    for coluna in range(t):
        if linha <= coluna:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()