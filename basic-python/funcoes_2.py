def calcula_media(*args, margem):
    # print(args, type(args))
    soma = sum(args)
    media = soma / len(args)
    return media + margem


# calcula_media(10, 8, 9)
print(calcula_media(10, 8, 9, margem=0.3))


def print_info(**kwargs):
    print(kwargs, type(kwargs))


print_info(nome='Pietro', sobrenome='Ribeiro')
