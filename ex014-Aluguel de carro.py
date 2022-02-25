dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
diaCarro = dia * 60
#diaCarro = quantidade de dias q o carro foi alugado
kmCarro = km * 0.15
#kmCarro = quantudade de km q o carro rodou quando foi alugado
valorFinal = diaCarro + kmCarro
# OU valorFinal = (dia * 60) + (km * 0.15)
print(f'O total a apagar é R${valorFinal:.2f}')