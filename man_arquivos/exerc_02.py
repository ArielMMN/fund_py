from random import randint

with open("numeros.txt", "w") as arquivo:
    for numero in range(1,101):
        arquivo.write(f"{randint(1,101)}")

