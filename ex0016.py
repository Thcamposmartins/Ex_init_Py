tupla = (
'1', 'um', '2', 'dois', '3', 'tres', '4', 'quatro', '5', 'cinco', '6', 'seis', '7', 'sete', '8', 'oito', '9', 'nove',
'10', 'dez')
num = int(input('Digite um numero: '))
pos=(num+num)-1
if num <= 10:
    print(f'O numero digitado foi o : {tupla[pos]}')
