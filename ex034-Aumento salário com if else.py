salario = float(input('Qual o salário do funcionário: '))
if salario > 1250:
    valorNovo1 = (salario*10)/100
    aumento1 = salario + valorNovo1
    print(f'Seu novo salário é de R${aumento1:.2f}')
elif salario <= 1250:
    valorNovo2 = (salario *15)/100
    aumento2 = salario + valorNovo2
    print(f' Seu novo salário é de R${aumento2:.2f}')