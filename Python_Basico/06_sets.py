#sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"brais", "moure" , 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("mouredev")
print(my_other_set)#un set no es una estructura ordenada

my_other_set.add("mouredev")# un set no admite repetidos
print(my_other_set)

print('moure' in my_other_set)# podemos analizar busquedas
print('mouri' in my_other_set)

my_other_set.remove("moure")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set
#print(my_other_set)

my_set = {"brais", "moure" , 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'kotlin' , 'swift' ,'python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"javascript" , " c#"}))

print(my_new_set.difference(my_set))