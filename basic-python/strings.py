empresa = "Let's Code"
print(empresa)

frase = "O professor Pietro da Let's Code disse: \"Hoje a pizza por minha conta\""
print(frase)

empresa = 'Google'
print(empresa)
print(empresa[0])
print(empresa[:3])

nomes_cidades = 'São Paulo, Belo Horizonte, Rio de Janeiro, Brasíliaa'
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

cabecalho = '     MENU PRINCIPAL    '
print(cabecalho.strip())

nome_cidade = 'rIo De jaNeirO'
print(nome_cidade.title())
print(nome_cidade.capitalize())
print(nome_cidade.lower())
print(nome_cidade.upper())

name_city = str(input('Que cidade do Brasil é conhecida como \"Cidade Maravilhoda\"? ')).strip()

while name_city.lower() != 'rio de janeiro':
    print('Tenta de novo, vai')
    name_city = str(input('Que cidade do Brasil é conhecida como \"Cidade Maravilhoda\"? '))

print('Booa, campeão!')

mensagem = 'Você viu o que o Pietro disse na sala ontem?'
fui_citado = 'Pietro' in mensagem
print(fui_citado)
