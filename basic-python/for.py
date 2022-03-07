nomes_cidades = ['São Paulo', 'Lodres', 'Tóquio', 'Paris']

for nome in nomes_cidades:
    print(nome)

print('-' * 15)
nomes_paises = 'Brasil', 'Argentina', 'China', 'Canadá', 'Japão'

for nome in nomes_paises:
    print(nome)

print('-' * 15)
cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes': 12.2
}

# for chave in cidade:
#     print(f'{chave}: {cidade[chave]}')

for key, value in cidade.items():
    print(f'{key}: {value}')

print('-' * 15)
for posicao in range(len(nomes_cidades)):
    print(posicao)

print('-' * 15)
for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Rio de Janeiro'

print(nomes_cidades)

print('-' * 15)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))
