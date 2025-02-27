ano = int(input("Em que ano estamos?: "))
ano_nascimento = int(input("digite ano de nascimento: "))

idade = ano - ano_nascimento

if idade >= 18:
    print("Você já pode tirar sua CNH")
else:
    print("Você ainda não pode tirar sua CNH")