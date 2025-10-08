#Strings 

my_string= "mi string"
my_other_string ="mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_strig="Este es un string\ncon tabulacion"
print(my_new_line_strig)

my_tab_string="\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string="\\tEste es un string \\n escapado"
print(my_scape_string)


#fornateo

name,surname,edad ="Cesar","Exposito",22

print("mi nombre es {} {} y mi edad es {}".format(name,surname,edad)) #si se usa format se usan {}
print("mi nombre es %s %s y mi edad es %d" %(name,surname,edad)) #si no se usa %s para string, %d para enteros, %f para float
print(f"Mi nombre es {name} {surname} y mi edad es {edad}") #tambien se puede hacer asi, a;adiendo la f al inicio, sin la f no salen los datos de las variables, 
                                                            #sino las lalves con la palabra dentro


#desempaqueado de caracteres

language = "python"
a,b,c,d,e,f=language
print(a)
print(b)


#division

language_slice=language[1:3]
print(language_slice)

language_slice=language[1:]
print(language_slice)

language_slice=language[-2]
print(language_slice)

language_slice=language[0:6:2]
print(language_slice)

#Reverse

reversed_language=language[::-1]
print(reversed_language)

#Funciones del sistema

print(language.capitalize())#pone la primera letra en mayuscula
print(language.upper())#pone toda en mayusculas
print(language.count("t"))#cuenta todos lo los caracteres que busques
print(language.isnumeric())#comprobar si es numerico
print("1".isnumeric())
print(language.lower())#pone todo en minusculas
print(language.upper().isupper())#comprueba que sea mayuscula, lo mismo con islower
print(language.startswith("py"))#pregunta si la palabra empieza por la palabra o conjunto de letras que pones, importa si esta en mayuscula  o minuscula


