km = float(input('Qual a distância em KM da sua viagem? '))
calculoPassagem = True
passagem = km * 0.50
passagemLonga = km *0.45
if km < 0:
    calculoPassagem = False
    print('Apenas valores Positivos!')
if calculoPassagem ==True:
    if km <= 200:
        print(f'Sua passagem ficou no valor de R${passagem:.2f}')
    elif km > 200:
        print(f'Sua passagem ficou no valor de R${passagemLonga:.2f}')