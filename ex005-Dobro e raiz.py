import math
n1 = float(input('Insira um número: '))
dobro = n1 * 2
triplo= n1 * 3
raiz = math.sqrt(n1)
#ou no lugar d import math, podeia usar a formila ex: raiz = n1 ** (1/2)
print ( 'Dobro:{:.0f} \nTriplo: {:.0f} \nRaiz Quadrada: {:.2f} '.format(dobro , triplo , raiz))