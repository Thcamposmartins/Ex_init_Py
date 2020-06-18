#estrutura condicional
velocidade=int(input('Digite a sua velocidade: '))

if velocidade <=80:
    print('Voce estava dentro do limite indicado, Parabens!')
else:
    multa:float=(velocidade-80)*7
    print('Voce estava acima do limite de velociade indicado, devera pagar {:.2f} babaca!'.format(multa))