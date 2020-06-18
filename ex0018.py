print('-'*30)
print('{:^30}'.format("Teste de formatação"))
print('-'*30)
#digitar varios valores em um tupla:
#valor= (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),)
#print(valor)

#pesquisar dentro de uma palavra dentro de uma tupla
palava =('nome','teste','thais','vida','morte','felicidade')
for p in palava:
    print('\nNa palavra \033[1;36;40m{}\033[m temos: '.format(p),end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('\033[1;30m{}\033[m'.format(letra),end=' ')
