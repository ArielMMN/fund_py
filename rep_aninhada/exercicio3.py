# Exercício 3
# Faça um program que permita imprimir uma representação de um tabuleiro de xadrez utilizando os caracteres "o" e "x".
# O canto superior esquerdo do tabuleiro deve ser preenchido com o caractere "o".

t = int(input("digite tamanho: "))


for linha in range(t):
    for coluna in range(t):
        if linha <= coluna:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()