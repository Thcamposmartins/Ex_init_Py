#maior/menor
a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor é : {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior é : {}'.format(maior))