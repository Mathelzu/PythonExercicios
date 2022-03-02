frase = str(input('Escreva uma frase: ')).strip().upper()
letraA = frase.count('A')
primeira = frase.find('A')
ultima = frase.rfind('A') - frase.count(' ')
print(f'A quantidade de vezes q aparece a letra A na frase é de: {letraA} ')
print(f'A primeira vez que a letra A aparece é na posição {primeira +1}')
print(f'A última vez que a letra A aparece é na posição {ultima +1}')


