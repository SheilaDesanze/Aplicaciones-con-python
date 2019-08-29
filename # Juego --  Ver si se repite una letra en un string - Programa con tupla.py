#!/usr/bin/env python
# coding: utf-8

# # Se repite una letra en un string - Programa con tupla

# Vamos a construir un programa que nos permita encontrar el primer carácter que no se repite en un string. Por ejemplo: si tenemos el string "mimamameama" el primer caracter que no se repite es la i.

# https://platzi.com/clases/1104-python/7107-ejemplo-con-tupl-3/

# In[2]:


"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    #creo la variable seen_leeters y la inicializo como un diccionario vacio
    seen_letters = {}
    
    #itero a lo largo de toda la secuencia de caracteres, obteniendo el indice y cada una de las letras dentro de la secuencia de caracteres
    for idx, letter in enumerate(char_sequence):
        #una vez que se tiene el indice y la letra lo primero que se quiere evaluar es si la letra ya se vio antes 
        if letter not in seen_letters:  
            seen_letters[letter] = (idx, 1)   #se utiliza a la letra como la llave para el diccionario. como valor utilizaremos a una tupla, ya que es una estructura de datos ligera util para guardar valores. Guardaremos ahi al indice y cuantas veces se ha visto la letra (1 por ser la primera vez que la vemos)
        else: #si ya habiamos visto la letra
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)  #modificamos la tupla que esta dentro de la llave con esa letra y obtenemos el primer valor de esa tupla accediendo a traves de indices. En el segundo espacio pondremos la funcion asignada al segundo valor, llamando con el indice 1, es decir llamo a cuantas veces se ha visto, y se le sumará 1. 

    #resumen: seen_letters se vería como un dicionario con dos valores: (con el indice de la primera vez que se vio, y con cuantas veces se vio esa letra). Es un diccionario que va de una letra a una tupla 
    
    
    
    
    #el objetivo ahora es limpiar ese diccionario descripto en el resumen de lo hecho anteriormente y quedarse unicamente con las letras que nada mas se vieron una sola vez       
    #creo una variable que almacenara una tupla que diga que letra se vio una sola vez nada mas y en que indice se encuentra 
    final_letters = []
    #itero, para llaves y valores con el metodo de iterar los items
    for key, value in seen_letters.items():
        if value[1] == 1:  #en el valor 1 se tiene almacenado cuantas veces se vio, entonces si la cantidad de veces que se vio es == 1 
            final_letters.append( (key, value[0]) )  #si se vio una vez se incluira una nueva tupla dentro de final_letters, con los valores: letra, y el indice donde se encuentra dicha letra.
                                                     #si se vio mas de una vez, ignorarla

    #resumen: Se obtiene una lista de tuplas que almacena la letra y el indice donde se vio por primera vez            
                
                
   #se ordena la lista de tuplas: se define ese orden con el indice de la primera letra que no se vio              
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])  #para ordenarla se usa el metodo sorted, que recibe una secuencia: como primer parametro la lista final_letters, como segundo parametro recibe una llave para indicar como ordenarlo y para eso se usa una lambda (una funcion de una linea que recibe el valor tupla y regresara el segundo valor de la secuencia, o sea conforme al indice)

    
    

    if not_repeated_letters:                #si notrepeatedletters tiene algo
        return not_repeated_letters[0][0]   #se regresara el primer valor -el 0- de la lista(que es una tupla), y el primer valor -el 0- de esa tupla (que es la letra)
    else:                                   #si notrepeatedletters no tiene nada y esta vacia la lista
        return '_'                          #se regresara "_"


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))


# In[3]:


"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    #creo la variable seen_leeters y la inicializo como un diccionario vacio
    seen_letters = {}
    
    #itero a lo largo de toda la secuencia de caracteres, obteniendo el indice y cada una de las letras dentro de la secuencia de caracteres
    for idx, letter in enumerate(char_sequence):
        #una vez que se tiene el indice y la letra lo primero que se quiere evaluar es si la letra ya se vio antes 
        if letter not in seen_letters:  
            seen_letters[letter] = (idx, 1)   #se utiliza a la letra como la llave para el diccionario. como valor utilizaremos a una tupla, ya que es una estructura de datos ligera util para guardar valores. Guardaremos ahi al indice y cuantas veces se ha visto la letra (1 por ser la primera vez que la vemos)
        else: #si ya habiamos visto la letra
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)  #modificamos la tupla que esta dentro de la llave con esa letra y obtenemos el primer valor de esa tupla accediendo a traves de indices. En el segundo espacio pondremos la funcion asignada al segundo valor, llamando con el indice 1, es decir llamo a cuantas veces se ha visto, y se le sumará 1. 

    #resumen: seen_letters se vería como un dicionario con dos valores: (con el indice de la primera vez que se vio, y con cuantas veces se vio esa letra). Es un diccionario que va de una letra a una tupla 
    
    
    
    
    #el objetivo ahora es limpiar ese diccionario descripto en el resumen de lo hecho anteriormente y quedarse unicamente con las letras que nada mas se vieron una sola vez       
    #creo una variable que almacenara una tupla que diga que letra se vio una sola vez nada mas y en que indice se encuentra 
    final_letters = []
    #itero, para llaves y valores con el metodo de iterar los items
    for key, value in seen_letters.items():
        if value[1] == 1:  #en el valor 1 se tiene almacenado cuantas veces se vio, entonces si la cantidad de veces que se vio es == 1 
            final_letters.append( (key, value[0]) )  #si se vio una vez se incluira una nueva tupla dentro de final_letters, con los valores: letra, y el indice donde se encuentra dicha letra.
                                                     #si se vio mas de una vez, ignorarla

    #resumen: Se obtiene una lista de tuplas que almacena la letra y el indice donde se vio por primera vez            
                
                
   #se ordena la lista de tuplas: se define ese orden con el indice de la primera letra que no se vio              
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])  #para ordenarla se usa el metodo sorted, que recibe una secuencia: como primer parametro la lista final_letters, como segundo parametro recibe una llave para indicar como ordenarlo y para eso se usa una lambda (una funcion de una linea que recibe el valor tupla y regresara el segundo valor de la secuencia, o sea conforme al indice)

    
    

    if not_repeated_letters:                #si notrepeatedletters tiene algo
        return not_repeated_letters[0][0]   #se regresara el primer valor -el 0- de la lista(que es una tupla), y el primer valor -el 0- de esa tupla (que es la letra)
    else:                                   #si notrepeatedletters no tiene nada y esta vacia la lista
        return '_'                          #se regresara "_"


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))


# In[ ]:




