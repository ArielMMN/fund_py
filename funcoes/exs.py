from math import sqrt 

def cal(a,b,c):
    res = sqrt(a) + sqrt(b) + sqrt(c) + (a + b)/2 + (b + c)/2 + (a + c)/2
    return res

a = int(input("N1°: "))
b = int(input("N2°: "))
c = int(input("N3°: "))

print(f"resultado:{cal(a,b,c):.2f}")