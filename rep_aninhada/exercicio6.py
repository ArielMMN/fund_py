# Exercício 6
# Crie um progama que leia um número natural positivo N e determine quantos dígitos possui o número.
# Entrada: O programa recebe um número inteiro, N, maior que zero. 
# Saída: O programa deve imprimir a quantidade de dígitos do número N.

n = int(input("num: "))
d = 0
while n > 0:
    n = n//10
    d = d + 1
    print(n)
print(f"o numero tem {d} digitos")