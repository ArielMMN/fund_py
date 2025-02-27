data_carro = int(input("Ano de fabricação do seu carro: "))
ano = 2025

idade_carro = ano - data_carro

if idade_carro < 3:
    print("Seu carro é NOVO")
else:
    print("Seu carro é VELHO")