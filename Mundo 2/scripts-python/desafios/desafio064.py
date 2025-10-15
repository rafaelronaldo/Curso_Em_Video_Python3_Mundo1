quantidade_numero = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input("Digite um número (999 para parar): "))
    if numero != 999:
        quantidade_numero += 1
        soma = soma + quantidade_numero
print("Foram digitados {} numeros e a soma entre elas foram de {}".format(quantidade_numero, soma))