distancia = float(input("Distância a ser percorrida (KM): "))

if distancia <= 200:
    valor = distancia * 0.50
    print(f"valor passagem: R$ {valor: .2f}")
else:
    valor = distancia * 0.45
    print(f"valor passagem: R$ {valor: .2f}")