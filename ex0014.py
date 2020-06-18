#farse palindromo
frase=str(input("Digite sua frase: ")).strip().upper()
palavra= frase.split()
junto=''.join(palavra)
pali =''
for x in range(len(junto)-1,-1,-1):
    pali+=junto[x]
if pali==junto:
    print('Essa frase é um Palindromo!!')
else:
    print("Não é Palindromo!")
print('A frase inversa é: {}'.format(pali))