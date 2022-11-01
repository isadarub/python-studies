def denial(p):
    return not p

print("p       a")
print("----------")
for p in [True,False]:
  a=denial(p)
  print(p,a)


# construindo a junção de conjunção
def conjunction(p,q):
  return p and q

print("p      q     a")
print("---------------")
for p in [True,False]:
  for q in [True,False]:
    a= conjunction(p,q)
    print(p,q,a)

#implementando a junção de disjuncao
def disjunction(p,q):
  return p or q

print("p      q     a")
print("---------------")
for p in [True,False]:
  for q in [True,False]:
    a= disjunction(p,q)
    print(p,q,a)

#implementando a função condicional
def conditional(p,q):
  return not(p) or q

print("p      q     a")
print("---------------")
for p in [True,False]:
  for q in [True,False]:
    a= conditional(p,q)
    print(p,q,a)

#definicao da função bicondicional
def biconditional(p,q):
  return ((not p) or q) and ((not q) or p)

print("p      q     a")
print("---------------")
for p in [True,False]:
  for q in [True,False]:
    a= biconditional(p,q)
    print(p,q,a)