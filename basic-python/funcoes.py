def hello():
    print('Olá, Mundo!')


hello()


def calculo_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


resultado = calculo_media(9, 10, 8)
print(resultado)

print('Olá', end='')
print(', Pietro')


def calc_media(valor1=0, valor2=0, valor3=0):
    media = (valor1 + valor2 + valor3) / 3
    return media


resultado2 = calc_media()
print(resultado2)
