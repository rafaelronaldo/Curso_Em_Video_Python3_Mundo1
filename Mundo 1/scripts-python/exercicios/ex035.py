print("-=-"*10)
print("Analisador de Triângulos")
input("-=-"*10)
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
    print("\033[32mOs segmentos acima PODEM FORMAR TRIÂNGULO!\033[m")
else:
    print("\033[31mOs segmentos acima NÃO PODEM FORMAR TRIÂNGULO!\033[m")