string1='this is a string'
print(string1)

#converting types
int_a=12345
print(type(int_a))

string_a=str(int_a)
print(type(string_a))

#tuplas can't be changed, only lists
list1= [1, 9.3, "Person", True]
print(list1)

#sets
empty_set={}
print(empty_set)

list1=[1,2,3,4,5,6]
set1=set(list1)

##checking if there is a certain element in the set
print(1 in set1) #true
print(10 in set1) #false

##operations
set2=set([9,8,7,3])

print(set1-set2)
print(set1|set2)
print(set1&set2)
print(set1^set2)
