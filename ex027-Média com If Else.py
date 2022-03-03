nota1 = float(input('Nota primeiro Bimestre: '))
nota2 = float(input('Nota segundo Bimestre: '))
nota3 = float(input('Nota terceiro Bimestre: '))
nota4 = float(input('Nota quarto Bimestre: '))
fazMedia = 1
#fazMedia = 1 == true
media = (nota1 + nota2 + nota3 + nota4) / 4
falta = 7 - media
if nota1 > 10 or nota2 > 10 or nota3 >10 or nota4 >10:
    fazMedia = 0
    print('Calma lá, que isso? sua nota ta acima de 10? tem alguma coisa errada!')
elif nota1 < 0 or nota2 < 0 or nota3 <0 or nota4 < 0:
    fazMedia = 0
    print('Oxi, nota negativa? tem alguma coisa errada!')
if fazMedia == 1:
    if media >= 7:
        print(f'Parabéns, passou de ano! sua media foi de {media}') 
    else:
        print(f'Poxa,a quantidade de pontos que faltou para passar foi {falta}')