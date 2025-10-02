peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura**2

if imc < 18.5:
    print("Você tem {:0.2f}kg, {:0.2f}m e um IMC de {:0.2f} e está \033[31mABAIXO DO PESO!\033[m".format(peso, altura, imc))
elif imc >= 18.5 and imc < 25:
     print("Você tem {:0.2f}kg, {:0.2f}m e um IMC de {:0.2f} e está no \033[32mPESO IDEAL!\033[".format(peso, altura, imc))
elif imc >= 25 and imc < 30:
      print("Você tem {:0.2f}kg, {:0.2f}m e um IMC de {:0.2f} e está \033[33mSOBREPESO!\033[m".format(peso, altura, imc))
elif imc >= 30 and imc < 40:
      print("Você tem {:0.2f}kg, {:0.2f}m e um IMC de {:0.2f} e está com \033[34mOBESIDADE!\033[m".format(peso, altura, imc))
else:
      print("Você tem {:0.2f}kg, {:0.2f}m e um IMC de {:0.2f} e está com \033[35mOBESIDADE MÓRBIDA!\033[m".format(peso, altura, imc))