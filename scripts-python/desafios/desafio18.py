import math
angulo = float(input("Digite um ângulo: "))
angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print("O seno de {} é: {}".format(angulo, seno))
print("O cosseno de {} é: {}".format(angulo, cosseno))
print("A tangente de {} é: {}".format(angulo, tangente))
