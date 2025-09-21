import math
cateto_oposto = float(input("Cateto Oposto: "))
cateto_adjacente = float(input ("Cateto Adjacente: "))

soma_dos_quadrados = cateto_oposto**2 + cateto_adjacente**2

hipotenusa = math.sqrt(soma_dos_quadrados)

print("O comprimento da hopotenusa é: {:0.2f}".format(hipotenusa))