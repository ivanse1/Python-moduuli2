import math
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
gramma = leiviskat*20*32*13.3 + naulat*32*13.3 + luodit*13.3
kilo = math.floor(gramma/1000)
print(f"Massa nykymittojen mukaan:")
print(f"{kilo} kilogrammaa ja {gramma-kilo*1000} grammaa.")