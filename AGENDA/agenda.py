print ("______________________________________________________________")
print (" ██╗  ██╗  █████╗  ██████╗   ██╗ ██ ║  ███████╗  ██████╗      ")
print (" ██║  ██║ ██╔══██╗ ██╔════╝  ██║ ██╔╝  ██╔════╝  ██╔══██╗     ")
print (" ███████║ ███████║ ██║Anonino█████╔╝   █████╗    ██████╔╝     ")
print (" ██╔══██║ ██╔══██║ ██║       ██╔═██╗   ██╔══╝    ██╔══██╗     ")
print (" ██║  ██║ ██║  ██║╚██████╗   ██║ ██╗   ███████╗  ██║  ██║     ")
print (" ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝   ╚═╝ ╚═╝   ╚══════╝  ╚═   ╚═╝     ")
print ("                                                              ")
print ("                     A n o n i m o                            ")

#python_version 3.8.6
print("Bienvenido a Agenda Telefonica")
print("Que operacion decea realizar?")
print(" 1.- Crear contacto nuevo")
print (" 2.- Listar contactos")
opcion = (input("> "))

if opcion == 1 :
	print("Crear contacto nuevo")
	agenda = open ("files/base.csv", 'a')

	nombre = raw_input( "ingrese nombre del contacto: ")
	numero = raw_input ("Ingrese numero de contacto: ")

	agenda.write(nombre)
	agenda.write(" : ")
	agenda.write(numero)
	agenda.write(" : ")
	agenda.write("\n")
	
	print (" GRACIAS ADIOS .. ")
	agenda.close()

elif opcion == 2:
	print("Lista de contacto: ")
	agenda = open ("files/base.csv")
	cantidad = int(raw_input ("Cantidad de contactos a listar: " ))
	for i in range(0, cantidad):
		print(agenda.readline())
	print("RESULTADO ADIOS")
	agenda.close()
else:
	print("Opcion no valida")
