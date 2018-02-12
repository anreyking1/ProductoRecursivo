def inicio():
	print producto(int(input("producto:\ingrese primer numero: ")), int(input("ingrese segundo numero: " )))
	raw_input("enter para salir")

def producto(numero1, numero2):
	if numero2 == 0:
		return 0
	else:
		return numero1 + producto(numero1, numero2 - 1)
		
inicio()
