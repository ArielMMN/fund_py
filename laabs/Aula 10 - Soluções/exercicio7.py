# Exercício 07
# Faça um programa que preencha uma matriz 10 X 3 com as notas
# de 10 alunos com 3 provas (valores gerados de forma aleatória
# entre 0 e 10).
# O programa deverá mostrar:
# ▶ A matriz com todas as notas de cada aluno.
# ▶ Um relatório com o número do aluno (número da linha), a prova em
# que cada aluno obteve a menor nota (número da coluna) e o valor
# da menor nota.
# ▶ O relatório deverá mostrar também qual foi a menor nota obtida
# em cada prova e a quantidade de alunos que obtiveram essa menor
# nota na respectiva prova.

from random import randint

# Criando a matriz de notas
notas = []
for num_aluno in range(10): # Para cada aluno
    aluno = [] # inicializa a linha
    for num_prova in range(3): # Para cada prova
        aluno.append(randint(0, 10)) # adiciona o elemento à linha
    notas.append(aluno) # adiciona a linha à matriz
    
# Exibindo a matriz de notas
print("Matriz de notas:")
for aluno in range(10): # Para cada aluno
    for prova in range(3): # Para cada prova
        print(f'{notas[aluno][prova]:3d}', end=' ') # Exibe o elemento com 2 dígitos
    print() # pula para a próxima linha
    
# Gerando o relatório
print("\nRelatório:")
for aluno in range(len(notas)):
    print(f'Aluno {aluno} | ', end='')
    menor_nota = min(notas[aluno]) # encontra a menor nota do aluno
    print(f'Menor nota: {menor_nota} | ', end=' ')
    menor_prova = notas[aluno].index(menor_nota) # encontra a prova com a menor nota
    print(f'Prova: {menor_prova}')
    
# Calculando a menor nota de cada prova e a quantidade de alunos que obtiveram essa nota
menor_notas = [10, 10, 10] # inicializa a lista com o maior valor possível
quantidade_alunos = [0, 0, 0] # inicializa a lista com 0
for aluno in range(len(notas)):
    for prova in range(3):
        if notas[aluno][prova] < menor_notas[prova]: # verifica se a nota é menor
            menor_notas[prova] = notas[aluno][prova] # atualiza a menor nota
            quantidade_alunos[prova] = 1 # reinicia a contagem
        elif notas[aluno][prova] == menor_notas[prova]: # verifica se a nota é igual
            quantidade_alunos[prova] += 1 # incrementa a contagem
            
# Exibindo o resultado
print("\nMenor nota de cada prova e quantidade de alunos:")
for prova in range(3):
    print(f'Prova {prova} | Menor nota: {menor_notas[prova]} | Quantidade de alunos: {quantidade_alunos[prova]}') 