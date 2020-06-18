num=int(input('Digite um numero: '))
#n:str=num;
#print('O valor digitado é de {} unidades'.format(n[3]))
#print('O valor digitado é de {} dezenas'.format(n[2]))
#print('O valor digitado é de {} centenas'.format(n[1]))
#print('O valor digitado é de {} milhares'.format(n[0]))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('O valor digitado é de {} unidades'.format(u))
print('O valor digitado é de {} dezenas'.format(d))
print('O valor digitado é de {} centenas'.format(c))
print('O valor digitado é de {} milhares'.format(m))