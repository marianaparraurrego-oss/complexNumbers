import math

#una tupla (a, b) con a = parte real, b = parte imaginaria
# En polar es una tupla (r, θ) con r = magnitud, θ = fase en radianes

def suma(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def resta(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def producto(c1, c2):
    a, b = c1
    d, e = c2
    return (a*d - b*e, a*e + b*d)

def division(z1, z2):
    a, b = z1
    d, e = z2
    denominador = d**2 + e**2
    if denominador == 0:
        print("No se puede dividir por 0")
    return ((a*d + b*e)/denominador, (b*d - a*e)/denominador)

def modulo(c):
    a, b = c
    return math.sqrt(a**2 + b**2)

def conjugado(c):
    a, b = c
    return (a, -b)

def cartesiano_a_polar(c):
    a, b = c
    r = modulo(c)
    theta = math.atan2(b, a)
    return (r, theta)

def polar_a_cartesiano(cp):
    r, theta = cp
    a = r * math.cos(theta)
    b = r * math.sin(theta)
    return (a, b)

def fase(c):
    return math.atan2(c[1], c[0])
