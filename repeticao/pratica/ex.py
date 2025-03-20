soma = 0
qtd = 0

while True:
    entrada = int(input("Digite um numero: "))
    soma = soma + entrada
    qtd = qtd + 1
    
    if qtd < 10:
        break
    
print(f"Soma:{soma} ")
print(qtd)