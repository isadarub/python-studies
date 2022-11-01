vetor=[0,-1,4,6,24,4,15,-3]

def question11(vetor):
  for i in range(len(vetor)):
    aux=vetor[i]
    j=i-1
    while j>=0 and vetor[j]>aux:
      vetor[j+1] = vetor[j]
      j-=1
    vetor[j+1]=aux
  
  return vetor

print(question11(vetor))