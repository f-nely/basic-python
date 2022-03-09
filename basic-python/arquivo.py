# arquivo = open('dom_casmurro_resumo.txt', 'r')
# texto = arquivo.read()
# print(texto)
# arquivo.close()

# arquivo = open('dom_casmurro_resumo.txt', 'r')
# linha = arquivo.readline()
# while linha != '':
#     print(linha, end='')
#     linha = arquivo.readline()
# arquivo.close()

# arquivo = open('dom_casmurro_resumo.txt', 'r')
# for linha in arquivo:
#     print(linha, end='')
# arquivo.close()

# with open('dom_casmurro_resumo.txt', 'r') as arquivo:
#     texto = arquivo.read()
#     print(texto)

with open('teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('This line was written by me using Python\n')
    arquivo.write('This second line was written by me using Python\n')

# with open('teste.txt', 'r', encoding='utf-8') as arquivo:
#     print(arquivo.read(), end='')

with open('teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('This third line was written by me using Python\n')

arquivo = open('teste.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()
