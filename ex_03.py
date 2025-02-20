dias = int(input("digite a quantidade de dias: "))
calculoDias = dias * 86400

horas = int(input("digite a quantidade de horas: "))
calculoHoras = horas * 3600

minutos = int(input("digite a quantidade de minutos: "))
calculoMinutos = minutos * 60

segundos = int(input("digite a quantidade de segundos: "))

tempo = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print (f"tempo total foi de {tempo} segundos" )