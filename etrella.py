import turtle

t=turtle.Pen()

def estrella(tamano,n):
    if(n%2==0):
        angulo=(-360/n)+180
    else:
	    angulo=(-(360-n+180)*2)
    for i in range(n):
        t.forward(tamano)
        t.left(angulo)
tamano=int(input("ingrese el tamaño de la estrella"))
n=int(input("Ingrese los lados de la estrella"))



estrella(tamano,n)