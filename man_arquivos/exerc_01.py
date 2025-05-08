with open("pares.txt", "r") as arquivo:
    linhas = arquivo.readlines()

linhas.reverse()

arquivo = open("invertido.txt", "w")
for linha in linhas:
    arquivo.write(linha)

arquivo.close()