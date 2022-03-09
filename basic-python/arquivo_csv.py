import csv

#
# with open('cases-brazil-total.csv', 'r', encoding='utf-8') as arquivo_csv:
#     leitor = csv.reader(arquivo_csv)
#     header = next(leitor)
#     for linha in leitor:
#         if float(linha[2]) > 130000:
#             print(linha)

# with open('cases-brazil-total.csv', 'r') as csv_file:
#     linhas = csv_file.read()
#     linhas = linhas.split('\n')
#     for linha in linhas:
#         linha = linha.split(',')
#         print(linha)

# with open('users.csv', 'w', encoding='utf-8') as arquivo_users:
#     escritor = csv.writer(arquivo_users)
#     escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
#     escritor.writerow(['Pietro', 'Ribeiro', 'pietro@email.com', 'Masculino'])

header = ['nome', 'sobrenome']
dados = []
opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opt != '0':
    nome = input('Qual seu nome? ')
    sobrenome = input('Qual seu sobrenome? ')
    dados.append([nome, sobrenome])
    opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerow(dados)

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
