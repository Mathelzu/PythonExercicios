valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo Valor: '))
valor3 = float(input('Terceiro Valor: '))
if valor1 < valor2 +valor3 and valor2 < valor3 + valor1 and valor3 < valor1 + valor2:
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')
