nomes_paises = ('Brasil', 'Argentina', 'China', 'Canadá', 'Japão')
print(nomes_paises)

names_countries = 'Brasil', 'Argentina', 'China', 'Canadá', 'Japão'
print(type(names_countries))

nome_estado = 'São Paulo',
print(nome_estado, type(nome_estado))

print(f'Tamanho tupla: {len(names_countries)}')
print(nomes_paises[0])
print(nomes_paises[1:])

b, a, c, ca, j = nomes_paises
print(b, a, j)
print(*nomes_paises)
