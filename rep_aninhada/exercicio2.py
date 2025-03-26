# Exercício 2
# Faça um porgrama que permita imprimir apenas as bordas de um retângulo. 
# O programa deve receber dois números inteiros L > 0 e C > 0, que representam a quantidade de linhas e colunas do retângulo, respectivamente.

t = int(input("digite tamanho: "))


for linha in range(t):
    for coluna in range(t):
        if linha <= coluna:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()