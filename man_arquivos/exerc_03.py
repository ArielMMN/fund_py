from random import randint

def main():
    gerar_numeros("numeros.txt")


def gerar_numeros(arquivo):
    with open("numeros.txt", "w") as arquivo:
        for numero in range(1,101):
            arquivo.write(f"{randint(1,101)}")

def ler_numeros(arquivo):
    with open(arquivo, "r") as arq:
        numeros = arq.readlines()

        lista = []
        for numero in numeros:
            lista.append(int(numero.strip()))
    return lista

def numeros_unicos(lista):
    num_unicos = []
    for numero in lista:
        if numero not in num_unicos:
            num_unicos.append(numero)
    return num_unicos
