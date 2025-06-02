# Exercício 06
# Cria uma matriz m[12][12] com números inteiros aleatórios.
# Em seguida, calcule e mostre a soma ou a média considerando
# somente aqueles elementos que estão abaixo da diagonal
# principal da matriz, conforme ilustrado abaixo (área verde).
# A entrada do programa deve ser um único caractere maiúsculo
# ’S’ ou ’M’, indicando a operação (Soma ou Média) que deverá
# ser realizada com os elementos da matriz.

from random import randint

# Criando a matriz
M = []
for num_linha in range(12): # Para cada linha
    linha = [] # inicializa a linha
    for num_coluna in range(12): # Para cada coluna
        linha.append(randint(0, 100)) # adiciona o elemento à linha
    M.append(linha) # adiciona a linha à matriz
    
# Exibindo a matriz M
print("Matriz M:")
for linha in range(12): # Para cada linha
    for coluna in range(12): # Para cada coluna
        print(f'{M[linha][coluna]:3d}', end=' ') # Exibe o elemento com 2 dígitos
    print() # pula para a próxima linha
    
# Solicita a operação (Soma ou Média)
operacao = input("Digite 'S' para soma ou 'M' para média: ").upper()
while operacao not in ['S', 'M']:
    operacao = input("Opção inválida. Digite 'S' para soma ou 'M' para média: ").upper()
# Calcula a soma ou média dos elementos abaixo da diagonal principal
soma = 0
contador = 0
for i in range(12):
    for j in range(12):
        if i > j: # verifica se o elemento está abaixo da diagonal principal
            soma += M[i][j] # soma os elementos
            contador += 1 # conta os elementos
# Exibe o resultado
if operacao == 'S':
    print(f'\nSoma dos elementos abaixo da diagonal principal: {soma}')
elif operacao == 'M':
    if contador > 0:
        media = soma / contador
    else:
        media = 0
    print(f'\nMédia dos elementos abaixo da diagonal principal: {media:.2f}')
    