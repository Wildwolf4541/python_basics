import math
a=int(input("Enter First Numebr= "))
b=int(input("Enter Second Numebr= "))

def HCF(a,b):
    return math.gcd(a,b)
print("HCF/GCD of the two numers= ",HCF(a,b))