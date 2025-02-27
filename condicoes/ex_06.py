n1 = int(input("Digite 1° nota: "))
n2 = int(input("Digite 2° nota: "))
n3 = int(input("Digite 3° nota: "))
n4 = int(input("Digite 4° nota: "))

media = (n1 + n2 + n3 + n4) /4

print(f"sua media {media:.2f}")

if media > 5:
    print("Aprovado")