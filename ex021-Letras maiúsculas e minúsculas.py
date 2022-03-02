nome = input('Insira o nome completo: ')

maiuscula = nome.upper()
minuscula = nome.lower()
letras = len(nome) - nome.count(' ')
primeiroNome = nome.find(' ')
print(f'Seu nome em maiúsculo é: {maiuscula} \nSeu nome em minúsculo é: {minuscula}') 
print(f'Seu nome tem {letras} letras')
print(f'Seu primeiro nome tem {primeiroNome} letras')