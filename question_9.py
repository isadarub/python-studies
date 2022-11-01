vetor=[0,-1,4,6,24,4,15,-3]
x=-2

def question9(vetor,x):
  resultado=-1
  print(vetor)
  for i in range(len(vetor)):
    verify=vetor[i]==x
    if verify:
      resultado=i
      
  return resultado

print(question9(vetor,x))