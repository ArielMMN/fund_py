valorHora = float(input("Digite o valor da hora de trabalho: "))
numHora = int(input("Digite o número de horas trabalhadas no mês: "))

salarioBruto = valorHora * numHora
impostoRenda = salarioBruto * (11 / 100)
INSS = salarioBruto * (8/100)
sindicato = salarioBruto * (5/100)
salarioLiquido = salarioBruto - impostoRenda - INSS - sindicato

print(f"+ Salário Bruto: R$ {salarioBruto:.2f}")
print(f"- IR (11%): R$ {impostoRenda:.2f}")
print(f"- INSS (8%): R$ {INSS:.2f}")
print(f"- Sindicato (%5): R$ {sindicato:.2f}")
print(f"+ Salário liquido: R$ {salarioLiquido:.2f}")