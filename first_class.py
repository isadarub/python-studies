# #verificando se um número é par
# number=0
# while number!='Sair':
#   number = input(print("Entre com um número inteiro: "))
#   # testa/transforma o número para inteiro
# try:
#   number=int(number)
#   if isinstance(number,int):
#     rest=number%2
#     if rest==0:
#       print('The number {} is even.'.format(number))
#     else:
#       print('The number {} is odd'.format(number))

# except:
#     print('You must input an int number')

#utilizando a função range
vetor=range(5)
print(list(vetor))
vetor=range(3,5)
print(list(vetor))
vetor=range(1,10,2)
print(list(vetor))

#verificando se um número é primo
def is_prime(n):
  for i in range(2,n):  #encontra todos os números no intervalor
    print('Divider: ',i)
    if (n%i) == 0:      #verifica se, pelo menos, um dos números no intervalo, além do valor final (n) é um divisor
      print('Divide: ',n)
      return False
    else:
      print('Dont divide: ',n)
  return True

print(is_prime(10))
print(is_prime(15))
print(is_prime(131))