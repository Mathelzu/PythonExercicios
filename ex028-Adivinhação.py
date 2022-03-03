import random
num = random.randint(0,5)
fazChute = True
chute = int(input('Chute um número de 0 a 5: '))
if chute > 5:
    fazChute = False
    print('Oxi, é números de 0 a 5 só!')
elif chute < 0:
    fazChute = False
    print('Sem números negativos, só de 0 a 5')
if fazChute == True:
    if chute == num:
        print('Parabéns, você acertou!')
    else: 
        print('Puts amigão, você errou!')