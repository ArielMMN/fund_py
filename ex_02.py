km = int(input("Digite a quantidade de quilometros percorridos:"))
dias = int(input("Digite a quantidade de dias: "))

calculoKm = km * 0.15
calculoDias = dias * 60


preco =  calculoKm + calculoDias

print ("Total a pagar: %.2f" % preco)
