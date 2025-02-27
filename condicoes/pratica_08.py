from math import  ceil

PI = 3.1415

altura = float(input("Digite a altura: "))
print(f"Altura: {altura: .2f}")
raio = float(input("Digite o raio: "))
print(f"Raio: {raio: .2f}")


area_base = PI * (raio**2)

area_late = 2 * (PI * raio)

area = area_base + area_late
print(f"Área a ser pintada: {area: .2f}")


litros_ness = area / 3
print(f"qtde Litros:{litros_ness: .2f} ")

latas = ceil(litros_ness / 5)
print(f"qtde latas:{latas: .0f} ")

if latas == 1:
    print("Preço unitario R$ 50.00")
if latas == 2:
    print("Preço unitario R$ 48.00")
if latas == 3:
    print("Preço unitario R$ 46.00")
if latas > 3:
    print("Preço unitario R$ 45.00 ")

