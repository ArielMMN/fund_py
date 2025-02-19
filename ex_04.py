valorHora = int(input("Digite o valor da hora de trabalho: "))
numHora = int(input("Digite o número de horas trabalhadas no mês: "))

salarioBruto = valorHora * numHora
impostoRenda = salarioBruto * (11 / 100)
INSS = salarioBruto * (8/100)
sindicato = salarioBruto * (5/100)
salarioLiquido = salarioBruto - impostoRenda - INSS - sindicato

print("+ Salário Bruto: R$ %.2f" % salarioBruto)
print("- IR (11%): R$ %.2f" % impostoRenda)
print("- INSS (8%): R$ %.2f" % INSS)
print("- Sindicato (%5): R$ %.2f" % sindicato)
print("+ Salário liquido: R$ %.2f" % salarioLiquido)