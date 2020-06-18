
import random

#print(':' * 20)
#nome = str(['Thais', 'Joao', 'William'])
#print('O ganhador foi:', nome[random.randrange(len(aluno))])
#print(':' * 20)

print(':' * 20)
a1: str = input('Digite um nome')
a2: str = input('Digite um nome')
a3: str = input('Digite um nome')
a4: str = input('Digite um nome')
a5: str = input('Digite um nome')
lista = [a1, a2, a3, a4, a5]
sorteio = random.choice(lista)
print('O aluno sorteado foi: ', sorteio)
print(':' * 20)
