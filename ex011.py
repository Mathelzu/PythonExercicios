preco = float(input('Valor sem o desconto: '))
desconto = (preco*5)/100
# ou   --desconto = preco - (preco*5/100)--
novoValor = preco - desconto
print(f'O valor apos receber o desconto é de {novoValor:.2f} Reais')