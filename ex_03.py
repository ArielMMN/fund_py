dias = int(input("digite a quantidade de dias: "))
calculoDias = dias * 86400

horas = int(input("digite a quantidade de horas: "))
calculoHoras = horas * 3600

minutos = int(input("digite a quantidade de minutos: "))
calculoMinutos = minutos * 60

segundos = int(input("digite a quantidade de segundos: "))


tempoTotal = calculoDias + calculoHoras + calculoMinutos + segundos

print ("tempo total foi de %d segundos" % tempoTotal)