#Variables

my_string_variable="my string variable"
print(my_string_variable)

my_int_variable=3
print(my_int_variable)

my_boolean_variable=True
print(my_boolean_variable)  

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


#concatenacion de variables
print(my_string_variable, my_int_variable, my_boolean_variable)
print("Este es el valor de:" , my_boolean_variable)


print(my_string_variable, my_int_variable, my_boolean_variable)
print(type(print((my_string_variable), (my_int_variable), (my_boolean_variable))))


#Algunas funciones del sistema
print(len(my_string_variable))
print(len(my_int_to_str_variable))


#Variables en una sola linea
name, surname, age = "John", "Doe", 35
print("Mi nombre es: ",name,", mi apellido es: ",surname," y mi edad es: ",age)


#inputs
"""
name = input("Cual es tu nombre?: ")
age = input("Cual es tu edad?: ")
print(name)
print(age)
"""


#cambiar su tipo
name=35
age="John"
print(name)
print(age)


#Forzar tipo de variable
address:str = "mi direccion"
address=32
address=True
address=3.5
print(type(address))