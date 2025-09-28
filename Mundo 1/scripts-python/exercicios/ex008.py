metros = float(input("Distância em metros: "))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print("A media de {} m corresponde a\n {} km\n {} hm\n {} dam\n {} dm\n {} cm\n {} mm\n".format(metros, km, hm, dam, dm, cm, mm))