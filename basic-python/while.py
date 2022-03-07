# contador = 0
#
# while contador < 10:
#     if contador == 1:
#         print(contador, 'Item limpo')
#     else:
#         print(contador, 'Itens limpos')
#     contador += 1
#
# print('Fim da repetição do bloco while')

# contador = 0
#
# while True:
#     if contador < 10:
#         contador += 1
#         if contador == 1:
#             print(contador, 'Item limpo')
#         else:
#             print(contador, 'Itens limpos')
#     else:
#         break
#
# print('Fim da repetição do bloco while')

# texto = str(input('Digite a sua senha: '))
#
# while texto != 'LetsCode':
#     texto = str(input('Senha inválida! Tente novamente.'))
#
# print('Acesso permitido')

contador = 0

while contador < 10:
    contador += 1
    if contador == 1:
        continue
    print(contador, 'Itens limpos')
print('Fim da repetição do bloco while')
