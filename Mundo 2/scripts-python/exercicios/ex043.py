peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / altura ** 2
print("o IMC dessa pessoa é de {:0.2f}".format(imc))
if imc < 18.5:
    print("Você está \033[31mABAIXO DO PESO!\033[m")
elif imc >= 18.5 and imc < 25:
    print("Você está no \033[32mPESO IDEAL!\033[m")
elif imc >= 25 and imc < 30:
    print("Você está com \033[33mSOBREPESO!\033[m")
elif imc >= 30 and imc < 40:
    print("Você está com \033[34mOBESIDADE!\033[m")
else:
    print("Você está com \033[35mOBESIDADE MÓRBIDA!\033[m")
