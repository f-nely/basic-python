# idade = int(input('Informe a sua idade: '))
# print(idade, type(idade))

a = float('123.25')
print(a, type(a))

b = str(3030)
print(b, type(b))

print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(5))

salario_mensal = float(input('Digite o valor do seu salário mensal: R$ '))
gasto_mensal = float(input('Digite o valor do seu gasto mensal em média: R$ '))

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante = salario_total - gasto_total

print(f'O montante que você pode economizar ao fim do ano é de R${montante}')
