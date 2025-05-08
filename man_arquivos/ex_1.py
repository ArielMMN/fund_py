arquivo_pares = open("pares.txt", "w")
arquivo_impares= open("impares.txt", "w")


with open("pares.txt", "r") as arquivos_pares, open("impares.txt", "r") as arquivos_impares:
    for i in range(0,1000):
        if i %2 == 0:
            arquivo_pares.write(f"{i}\n")
        else:
            arquivo_impares.write(f"{i}\n")

