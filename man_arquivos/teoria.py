"""
open e a função para abrir o arquivo
close é para fechar, como se fosse crtl + s
\n e para mandar o cursos para a proxima linha
"""

arquivo = open("teste.txt", "w")

for linha in range(1, 11):
    arquivo.write(f"Linha {linha} \n")
arquivo.close()
