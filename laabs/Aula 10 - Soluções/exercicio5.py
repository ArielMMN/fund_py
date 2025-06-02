# Exercício 05
#  Faça um programa que cria um matriz A 10 X 5 com números
#  inteiros aleatórios e, então, exiba a matriz transposta de
#  A(At)
#  Determinar a transposta de uma matriz é reescrevê-la de forma
#  que suas linhas e colunas troquem de posições ordenadamente,
#  isto é, a primeira linha é reescrita como a primeira coluna, a
#  segunda linha é reescrita como a segunda coluna e assim por
#  diante, até que se termine de reescrever todas as linhas na
#  forma de coluna.Exercício 05
#  Faça um programa que cria um matriz A 10 X 5 com números
#  inteiros aleatórios e, então, exiba a matriz transposta de
#  A(At)
#  Determinar a transposta de uma matriz é reescrevê-la de forma
#  que suas linhas e colunas troquem de posições ordenadamente,
#  isto é, a primeira linha é reescrita como a primeira coluna, a
#  segunda linha é reescrita como a segunda coluna e assim por
#  diante, até que se termine de reescrever todas as linhas na
#  forma de coluna.

from random import randint

# Criando a matriz
A = []
for num_linha in range(10): # Para cada linha
    linha = [] # inicializa a linha
    for num_coluna in range(5): # Para cada coluna
        linha.append(randint(0, 100)) # adiciona o elemento à linha
    A.append(linha) # adiciona a linha à matriz
    
# Exibindo a matriz A
print("Matriz A:")
for linha in range(10): # Para cada linha
    for coluna in range(5): # Para cada coluna
        print(f'{A[linha][coluna]:2d}', end=' ') # Exibe o elemento com 2 dígitos
    print() # pula para a próxima linha
    
# Criando a matriz transposta At
At = []
for num_coluna in range(5): # Para cada coluna
    linha = [] # inicializa a linha
    for num_linha in range(10): # Para cada linha
        linha.append(A[num_linha][num_coluna]) # adiciona o elemento à linha
    At.append(linha) # adiciona a linha à matriz transposta
    
# Exibindo a matriz transposta At
print("\nMatriz transposta At:")
for linha in range(5): # Para cada linha
    for coluna in range(10): # Para cada coluna
        print(f'{At[linha][coluna]:2d}', end=' ') # Exibe o elemento com 2 dígitos
    print() # pula para a próxima linha