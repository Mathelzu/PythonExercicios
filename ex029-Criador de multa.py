km = float(input('Quantos km o carro está: '))
multa = (km-80) * 7
calculoMulta = True
if km < 0:
    calculoMulta = False
    print('Como assim km negativo?ta andando de ré?')
if calculoMulta == True:
    if km > 80:
        print(f'Você esta acima da velocidade, receberá uma multa de R${multa:.2f}')
    elif km <= 80:
        print('Você esta no na velocidade permitida!')