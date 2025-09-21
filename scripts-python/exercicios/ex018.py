from math import radians, sin, cos, tan











angulo = float(input("Digite o ângulo que você deseja: "))
angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print("O ângulo de {} tem o SENO de {:0.2f}".format(angulo_radianos, seno))
print("O ângulo de {} tem o COSSENO de {:0.2f}".format(angulo_radianos, cosseno))
print("O ângulo de {} tem a TANGENTE de {:0.2f}".format(angulo_radianos, tangente))
