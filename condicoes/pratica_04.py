salario = float(input("Digite seu salario:"))

if salario > 1250.00:
    novo_salario = salario * 1.10
    print(f"novo salario: R$: {novo_salario: .2f}")
else:
    novo_salario = salario * 1.15
    print(f"novo salario: R$: {novo_salario: .2f}")