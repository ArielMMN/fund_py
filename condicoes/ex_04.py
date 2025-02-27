salario = float(input("digite o valor do salrio atual: "))
if salario < 1800:
    novo_salario = salario * 1.1
    print("o funcionario tem direito a 10% de aumento")
    print("Novo salario R$ %.2f" % novo_salario)