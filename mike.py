#conditions
# D depends on V
# Re depends on D and V
# F depends on the value of Re
# hl depends on the value of D V F

import math
# note that
# e = density
# Q = discharge
# L = length
# U = viscousity
# g = gravity which is 9.81

check = str(input("Is the value for D given? "))
if check == 'yes':
    print("Since the value of D is given let's solve for Re")
    e = float(input("Enter the value of e: "))
    U = float(input("Enter the value of U: "))
    D = float(input("Enter the value of D: "))
    Re = (e * D * V) / U
    print("Re = " + str(Re))
    F = 64 / Re
    print("F = " + str(F))
    L = float(input("Enter the value of L: "))
    g = float(input("Enter the value of g: "))
    hL = (F * L * V * V) / (2 * g * D)
    print("hL is " + str(hL))
elif check == 'no':
    print("Since we dont't know the value of D let's find D")
    Q = float(input("Enter the value of Q: "))
    V = float(input("Enter the value of V: "))
    k = (4 * Q) / (math.pi * V)
    D = math.sqrt(k)
    print("D = " + str(D))
    e = float(input("Enter the value of e: "))
    U = float(input("Enter the value of U: "))
    Re = (e * D * V) / U
    print("Re = " + str(Re))
    F = 64 / Re
    print("F = " + str(F))
    L = float(input("Enter the value of L"))
    g = float(input("Enter the value of g"))
    hL = (F * L * V * V) / (2 * g * D)
    print("hL is " + str(hL))
else:
    print("Invalid answer, answer with yes or no")