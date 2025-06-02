# Exercício 04
#  Solicitar dados de uma matriz 4 X 4
#  Montar uma lista de 4 elementos com a soma dos elementos
#  ímpares de cada linha da matriz

# Solicita 9 números inteiros ao usuário
M = []
for i in range(16):
    num = int(input(f'Digite o {i+1}º número: '))
    M.append(num)
    
# Converte a lista em uma matriz 3x3
matriz = []
contador = 0
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(M[contador])
        contador += 1
    matriz.append(linha)
    
# Exibe a matriz
print("\nMatriz:")
for linha in matriz:
    for elemento in linha:
        print(f'{elemento:2d}', end=' ')
    print() # pula para a próxima linha
    
# Calcula a soma dos elementos ímpares de cada linha
soma_impares = []
for i in range(4):
    soma = 0
    for j in range(4):
        if matriz[i][j] % 2 != 0: # verifica se o elemento é ímpar
            soma += matriz[i][j] # soma os elementos ímpares
    soma_impares.append(soma) # adiciona a soma à lista
print(f'\nLista: {soma_impares}')