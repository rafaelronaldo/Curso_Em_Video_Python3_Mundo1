primeiro_segmento = float(input("Primeiro segmento: "))
segundo_segmento = float(input("Segundo segmento: "))
terceiro_segmento = float(input("Terceiro segmento: "))

if primeiro_segmento + segundo_segmento > terceiro_segmento and primeiro_segmento + terceiro_segmento > segundo_segmento and segundo_segmento + terceiro_segmento > primeiro_segmento:
    print("Os segmentos podem formar um triângulo ", end="")
    if primeiro_segmento == segundo_segmento == terceiro_segmento:
        print("EQUILÁTERO!")
    if primeiro_segmento != segundo_segmento != terceiro_segmento != primeiro_segmento:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos não podem formar um triângulo!")
