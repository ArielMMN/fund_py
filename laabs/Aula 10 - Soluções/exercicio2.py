# Exercício 02
#  Faça um programa que cria uma matriz M 10 X 15, sendo que cada
#  elemento é um inteiro gerado aleatoriamente.
#  Então, exiba a matriz completa e, na sequência, somente os
#  elementos da primeira coluna da matriz.

from random import randint

# Criando a matriz
M = []
for num_linha in range(10): # Para cada linha
    linha = [] # inicializa a linha
    for num_coluna in range(15): # Para cada coluna
        linha.append(randint(0, 100)) # adiciona o elemento à linha
    M.append(linha) # adiciona a linha à matriz
    
# Exibindo a matriz completa
print("Matriz completa:")
for linha in range(10): # Para cada linha
    for coluna in range(15): # Para cada coluna
        print(f'{M[linha][coluna]:2d}', end=' ') # Exibe o elemento com 2 dígitos
    print() # pula para a próxima linha
    
# Exibindo os elementos da primeira coluna
print("\nElementos da primeira coluna:")
for linha in range(10): # Para cada linha
    print(f'{M[linha][0]:2d}', end=' ') # Exibe o elemento da primeira coluna
print() # pula para a próxima linha