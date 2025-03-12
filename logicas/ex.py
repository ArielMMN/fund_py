a = int (input ("Lado a: ") )
b = int (input ("Lado b: " ) )
c = int (input ("Lado c: ") )
if a < b + c and b < a + c and c < a + b:
    if (a == b) and ( b == c):
        print ("Triângulo equilatero")
    elif a == b or a == c or b == c:
        print ("Triângulo isosceles")
    elif a != b and a != c and b != c:
        print ("Tri ngulo escaleno")
else:
    print("No triangulo")