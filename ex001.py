algo = input('Digite Algo: ')
print('Você escreveu "',algo,'"')
print('Você escreveu o tipo: ', type(algo))
print('Ele é do tipo alfanúmerico? ', algo.isalnum())
print('Ele é do tipo númerico? ', algo.isnumeric())
print('Ele é do tipo alfabético? ', algo.isalpha())
print('Ele é do tipo espaço?', algo.isspace())
print('Ele é do tipo capitalizado?', algo.istitle())