Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Pen()
>>> for x in range(1,9):
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> for x in range(1,38):
	t.forward(100)
	t.left(175)

	
>>> t.reset()
>>> def micuadrado(size):
	for x in range(1,5):
		t.forward(size)
		t.left(90)

		
>>> micuadrado(100)
>>> t.reset()
>>> for x in range(1,9):
	t.forward(100)
	t.left(175)

>>>  t.reset()
SyntaxError: unexpected indent
>>> t.reset()
>>> for x in range(1,9):
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> for x in range(0,9):
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> def estrella(tamaño,n):
	for in range(n):
		
SyntaxError: invalid syntax
>>> ef estrella(tamaño,n):
	for i in range(n):
		
SyntaxError: invalid syntax
>>> def estrella(tamano,n):
	for i in range(n):
		t.forward(tamano)
		t.left(angulo)
tamano=int(input("ingrese el tamaño de la estrella"))
SyntaxError: invalid syntax
>>> 
