# Exercício 1
# Faça um programa que receba uma série de n;umeros naturaus e contabilize quantos desses números são primos. 
# Um número primo x é primo se x > 1 e seus únicos divisores são 1 e x.

numero = int(input("digite a qtd de numero: "))
primos = 0

for i in range(numero):
    n = int(input("DIgite um numero a ser testado: "))
    eh_primo = True
    if n > 1:
        for j in range(2, n):
            if n % j == 0:
                eh_primo = False
    if eh_primo == True:
        print("É primo")
        primos = primos + 1
    else:
        print("não é primo")
print(f"A quantidade é {primos} de {numero}")