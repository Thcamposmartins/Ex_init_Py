#idade, nome, sexo, media , homem mais velho, mulheres <20
cont_m=0
media:float=0
nomeh=''
idademaior=0
for x in range(0,4):
    print('--- Pessoa {} ---'.format(x))
    nome=str(input('Digite seu nome: ')).strip().capitalize()
    sexo=str(input('Digite seu sexo F/M: ')).strip().upper()
    idade=int(input('Digite sua idade: '))
    media+=idade
    if x == 1 and sexo in 'Mm':
        idademaior=idade
    if sexo in 'Mm' and idade>idademaior:
        idademaior=idade
        nomeh=nome
    if sexo == 'F' and idade > 20:
        cont_m+=1

print('\n\nMedia de idade {:.2f}'.format(media/4))
print('Quantas mulheres maiores de 20: {}'.format(cont_m))
print('O homem com a maior idade {} e seu nome é {}'.format(idademaior,nomeh))