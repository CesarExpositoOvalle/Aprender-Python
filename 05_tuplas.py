#tuplas 

my_tuple = tuple()
my_other_tuple= ()

my_tuple = (35, 1.77, 'brais', 'moure','brais')
my_other_tuple = (43,23,12,63,12,42)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-4]) indexError
#print(my_tuple[-6]) indexError

print(len(my_tuple))

print(my_tuple.count('brais'))# como en las listas cuenta el valor buscado
print(my_tuple.index('moure'))# dice el index de lo que buscas

#my_tuple[1]=1.80 #las tuplas son lists invariables, puedes guardar datos pero no puedes a;adir ni editar los datos una vez creada

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3 : 6])

my_tuple=list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "mouredev"
my_tuple.insert(1,'azul')
print(tuple(my_tuple))

del my_tuple  #del se carga la variabel, no vacia la tupla o lista, la elimina por completo
#print(my_tuple)
