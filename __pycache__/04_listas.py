#listas

my_list=list()
my_other_list=[]

print(len(my_list))

my_list =[30,20,34,65,27,15,26,30]

print(my_list)
print(len(my_list))


my_other_list = [35 , 1.77 , "brais" , 'moure']

print(type(my_other_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])    
print(my_other_list[-1])
print(len(my_other_list))# el len es para el tama;o de la lista
print(my_other_list.count('brais'))# count sirve para contar algo especifico, en este caso brais
#print(my_other_list[4]) indexError
#print(my_other_list[-5]) indexError

age, heigh, name, surname = my_other_list #si la lista tiene 4 elementos tienes que crear 4 variables, si no da error, mejor evitar
print(name)

name, heigh, age, surname = my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3] # evitar tambien
print(age)

print(my_list + my_other_list) # pega una lista a la otra, no funciona con otros signos

print([1,2,3,4]) # se crea una nueva lista

my_other_list.append('mouredev')
print(my_other_list)

my_other_list.insert(1, 'azul')
print(my_other_list)

my_other_list.remove('azul')
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop() #elimina el ultimo elemento, si pones un numero elimina el contenido de ese numero
print(my_list.pop())#imprime el elemento eliminado
print(my_list)

my_pop_element= my_list.pop(2)#guarda en una variable el valor del pop
print(my_pop_element)
print(my_list)

del my_list[2] #elimina el valor de la posicion que pongas
print(my_list)

my_new_list = my_list.copy()

my_list.clear() #borra las cosas de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #incierte el orden de lista
print(my_new_list)

my_new_list.sort()#orden alfabetico o de menor a mayor en caso de numeros
print(my_new_list)

print(my_new_list[1 : 3])

my_list = 'hola python'
print(my_list)
print(type(my_list))