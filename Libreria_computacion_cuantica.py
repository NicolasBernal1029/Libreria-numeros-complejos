import math

def suma_cplx(c1,c2):
    ladoizq = c1[0] + c2[0]
    ladoder = c1[1] + c2[1]

    return ladoizq, ladoder


def multplx(c1,c2):
    parteA = c1[0] * c2[0]
    parteB = c1[1] * c2[1]
    parteC = c1[0] * c2[1]
    parteD = c1[1] * c2[0]

    izq = parteA - parteB
    der = parteC - parteD

    return izq, der



def divplx(c1,c2):

    parteA = (c1[0] * c2[0]) + (c1[1] * c2[1])
    parteB = (c2[0] * 2) + (c2[1] * 2)
    parteC = (c2[0] * c1[1]) - (c1[0]*c2[1])

    parteI = parteA / parteB
    parteD = parteC / parteB

    return parteI,parteD

def modul_cplx(c1):
    parteG = c1[0]**2
    parteH = c1[1]**2
    parteII = parteG + parteH
    parteJ = parteII**0.5
    return (parteJ)

def conjugado_cplx(c1):
    a, b = c1
    conjugado_a = a
    conjugado_b = -b
    return conjugado_a, conjugado_b

def fase_cplx(c1):
    parteZ = c1[1] / c1[0]
    parteZZ = math.atan(parteZ)
    return (parteZZ)

def polar_cplx(c1):
    parteA = modul_cplx(c1)
    parteB = fase_cplx(c1)
    parteC = parteA * math.cos(parteB) + parteA * math.sin(parteB)
    return (parteC)

print(suma_cplx((3, 2),(-5,5.2)))
print(multplx((3, 2),(-5,5.2)))
print(divplx((3, 2),(-5,5.2)))
print(modul_cplx((3, 2)))
print(conjugado_cplx((3, 2)))
print(fase_cplx((4,5)))
print(polar_cplx((4,5)))



