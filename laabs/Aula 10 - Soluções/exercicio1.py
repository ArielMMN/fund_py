# Exercício 01
# Crie 3 listas:
# ▶ Inteiros: a primeira lista com 10 números inteiros gerados aleatoriamente
# ▶ Reais: a segunda lista com 5 números reais gerados aleatoriamente
# ▶ Strings: A terceira lista com 7 strings criadas por você.
# Então adicione as 3 listas a uma lista única, chamada
# completa.
# Apague todas as 3 listas originais.
# Acesse e mostre todos os elementos da lista completa

# Use:
# from random import randint, random
# print(randint(0, 10))
# print(random() * 10)




from random import randint, random

# Criando as listas
inteiros = [randint(0, 10) for _ in range(10)]
reais = [random() * 10 for _ in range(5)]
strings = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP', 'Swift']
# Adicionando as listas à lista completa
completa = [inteiros, reais, strings]
# Apagando as listas originais
del inteiros
del reais
del strings

# Acessando e mostrando os elementos da lista completa
print(completa)