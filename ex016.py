import math
catOp = float(input('Valor Cateto Oposto: '))
catAd = float (input('Valor Cateto adjacente: '))
hip = (catOp**2) + (catAd**2)
# ou hip = math.hypot (catOp , catAd)
hip2 = math.sqrt(hip)
print (f'O valor da hipotenusa é de {hip2:.2f}')
