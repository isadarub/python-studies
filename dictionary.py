dict1={'blue':3,'white':4,'green':6,'black':1}

print(dict1.get('white'))
print(dict1['white'])

dict1['yellow'] = 8

print(dict1)
print(dict1.values())
print(dict1.keys())

dict2=dict({'orange':47,'purple':25,'pink':5})
dict1.update(dict2)
print(dict1)