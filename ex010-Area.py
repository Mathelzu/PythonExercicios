largura = float(input('Largura da parede em Metros: '))
altura = float(input('Altura da parede em Metros: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m²')
print(f'É necessario {tinta} Litros de tinta para pintar a parede.')
