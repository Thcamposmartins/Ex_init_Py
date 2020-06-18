#soma multiplos de 3 0 a 500
soma=0
for i in range (0,500):
    if i % 3 == 0:
        soma+=i
print('A soma dos multiplos de 3 de 0 a 500 é {}'.format(soma))