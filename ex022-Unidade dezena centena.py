num = int(input('Coloque um valor de 0 a 9999: '))
unid = num // 1 % 10
deze = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print (f'Unidade: {unid}\nDezena: {deze}\nCentena: {cent}\nMilhar {mil}')
