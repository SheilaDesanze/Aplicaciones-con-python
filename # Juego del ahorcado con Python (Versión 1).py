#!/usr/bin/env python
# coding: utf-8

# # Juego del ahorcado con Python (Versión 1)

# In[ ]:


#ganando


# In[1]:


import random  #modulo importado, necesario para el cuarto paso


# primer paso: defino a IMAGES, lo hago en mayuscula para denotar que es una constante
IMAGES = ['''




      +---+
      |   |
          |
          |
          |
          |
          |
          =======''','''

      +---+
      |   |
      O   |
          |
          |
          |
          |
          =======''','''





      +---+
      |   |
      O   |
      |   |
          |
          |
          |      
          =======''','''



      +---+
      |   |
      O   |
     /|   |
          |
          |
          |
          =======''','''



      +---+
      |   |
      O   |
     /|\  |
          |
          |
          |
          =======''','''



      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
          |
          =======''','''



      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
          |
          =======''','''
''']


#segundo paso: defino una lista de palabras, en mayuscula para denotar que es una constante
WORD = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]




#del quinto paso: defino a la funcion con sus parametros
def display_board(hidden_word, tries):
    print(IMAGES[tries])    # imprimo las imagenes con el indice "tries"
    print('')               # espacio (visual)
    print(hidden_word)      # imprimo la palabra escondida de manera tal que el usuario puede ir viendo como van sus intentos
    print('')               # espacio (visual)



    
    
    
#cuarto paso: defino la funcion que escoga de manera aleatoria una palabra de la lista de palabras
def random_word(): 
    
    #objetivo: entrar a la lista generando un "indice aleatorio", para ingresar de manera aleatoria a la lista de palabras.
    #          el numero aleatorio generado estara entre 0 y la longitud real (longitud -1) que sea de la lista de palabras; ese numero sera el indice
    idx = random.randint(0, len(WORD) -1)

    #para que se regrese la palabra:
    return WORD[idx]






#tercer paso: defino el punto de acceso al programa que llama a la funcion run y da la bienvenida a los usuarios
def run():
    word = random_word()   #defino a la variable word que llame a una funcion que escoga de manera aleatoria una palabra de la lista de palabras
    
    #genero una variable para que se muestre un tablero, multiplicando una lista que contenga solo a "-" por la cantidad de veces que tenga una letra la palabra aleatoria seleccionada por el algoritmo:       
    hidden_word = ['-'] * len(word)
    
    #genero una variable para guardar cuantas veces se tuvieron errores, y en base a este numero que va aumentando se va pudiendo acceder a la lista de imagenes (a traves del indice)
    tries = 0
    
    #quinto paso: comienzo un loop para mostrar el tablero todo el tiempo ("infinitamente")
    while True:
        display_board(hidden_word, tries)  #del parametro tries depende la imagen que se va a mostrar 
        current_letter = str(input('Escoge una letra: '))  #seccion interactiva, donde se pide una letra al usuario
        
        #sexto paso: declaro una nueva variable con una lista vacia donde se evaluara si la letra que introdujo el usuario se encuentra en la palabra; se obtendra el indice de la letra y se almacenara en esta variable para utilizarla despues.
        letter_indexes = []
        for idx in list(range(len(word))):   #se itera a lo largo de la longitud de la palabra
            if word[idx] == current_letter:  #donde evaluamos si el indice idx de la palabra, de va desde 0 hasta finalizarla, es igual a la letra que introdujo el usuario. se recorren todos los indices para ver cuantas veces coincide con la letra
                letter_indexes.append(idx)   #si son iguales se agregara el/los indice/s de la variable en el letter indexes con el metodo append
    
        if len(letter_indexes) == 0: #si la longitud es igual a 0, o sea si el intento por encontrar la letra no fue exitoso
            tries +=1             # entonces mostrar una imagen (cada vez que no se acierte se mostrara la siguiente imagen)  
            
            #limito a 7 intentos (ya que maximo son 7 imagenes)
            if tries == 7:
                display_board(hidden_word, tries)
                print('')               # espacio (visual)
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break   #salgo del loop

        
        else:                        #si fue exitoso, reemplazar la letra dentro de la palabra escondida hidden word 
            for idx in letter_indexes:    #itero y reemplazo el indice en la palabra escondida
                hidden_word[idx] = current_letter  #se reemplazara la letra por "-" accediendo a los indices
            
            #importante: vaciar la variable donde estoy contando los indices
            letter_indexes = [] #le asigno espacio vacio
            
        
        #Si ya se reemplazaron todos los "-" es porque ya se adivinaron todas las letras y se gano el juego.
        #si se encuentra un errorse manejara con try y except:
        try:
            hidden_word.index('-') #se utliza la funcion index para cuestionar si se encuentra un elemento dentro de una lista
        except ValueError:  #este error demuestra que ganaste
            print('')               # espacio (visual)
            print('¡Felicidades, ganaste! La palabra es {}'.format(word))
            break
 
        
       
if __name__ == '__main__':
    print('B I E N V E N I D O S  A L  A H O R C A D O')
    run()


# In[ ]:


#perdiendo: 


# In[2]:


import random  #modulo importado, necesario para el cuarto paso


# primer paso: defino a IMAGES, lo hago en mayuscula para denotar que es una constante
IMAGES = ['''




      +---+
      |   |
          |
          |
          |
          |
          |
          =======''','''

      +---+
      |   |
      O   |
          |
          |
          |
          |
          =======''','''





      +---+
      |   |
      O   |
      |   |
          |
          |
          |      
          =======''','''



      +---+
      |   |
      O   |
     /|   |
          |
          |
          |
          =======''','''



      +---+
      |   |
      O   |
     /|\  |
          |
          |
          |
          =======''','''



      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
          |
          =======''','''



      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
          |
          =======''','''
''']


#segundo paso: defino una lista de palabras, en mayuscula para denotar que es una constante
WORD = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]




#del quinto paso: defino a la funcion con sus parametros
def display_board(hidden_word, tries):
    print(IMAGES[tries])    # imprimo las imagenes con el indice "tries"
    print('')               # espacio (visual)
    print(hidden_word)      # imprimo la palabra escondida de manera tal que el usuario puede ir viendo como van sus intentos
    print('')               # espacio (visual)



    
    
    
#cuarto paso: defino la funcion que escoga de manera aleatoria una palabra de la lista de palabras
def random_word(): 
    
    #objetivo: entrar a la lista generando un "indice aleatorio", para ingresar de manera aleatoria a la lista de palabras.
    #          el numero aleatorio generado estara entre 0 y la longitud real (longitud -1) que sea de la lista de palabras; ese numero sera el indice
    idx = random.randint(0, len(WORD) -1)

    #para que se regrese la palabra:
    return WORD[idx]






#tercer paso: defino el punto de acceso al programa que llama a la funcion run y da la bienvenida a los usuarios
def run():
    word = random_word()   #defino a la variable word que llame a una funcion que escoga de manera aleatoria una palabra de la lista de palabras
    
    #genero una variable para que se muestre un tablero, multiplicando una lista que contenga solo a "-" por la cantidad de veces que tenga una letra la palabra aleatoria seleccionada por el algoritmo:       
    hidden_word = ['-'] * len(word)
    
    #genero una variable para guardar cuantas veces se tuvieron errores, y en base a este numero que va aumentando se va pudiendo acceder a la lista de imagenes (a traves del indice)
    tries = 0
    
    #quinto paso: comienzo un loop para mostrar el tablero todo el tiempo ("infinitamente")
    while True:
        display_board(hidden_word, tries)  #del parametro tries depende la imagen que se va a mostrar 
        current_letter = str(input('Escoge una letra: '))  #seccion interactiva, donde se pide una letra al usuario
        
        #sexto paso: declaro una nueva variable con una lista vacia donde se evaluara si la letra que introdujo el usuario se encuentra en la palabra; se obtendra el indice de la letra y se almacenara en esta variable para utilizarla despues.
        letter_indexes = []
        for idx in list(range(len(word))):   #se itera a lo largo de la longitud de la palabra
            if word[idx] == current_letter:  #donde evaluamos si el indice idx de la palabra, de va desde 0 hasta finalizarla, es igual a la letra que introdujo el usuario. se recorren todos los indices para ver cuantas veces coincide con la letra
                letter_indexes.append(idx)   #si son iguales se agregara el/los indice/s de la variable en el letter indexes con el metodo append
    
        if len(letter_indexes) == 0: #si la longitud es igual a 0, o sea si el intento por encontrar la letra no fue exitoso
            tries +=1             # entonces mostrar una imagen (cada vez que no se acierte se mostrara la siguiente imagen)  
            
            #limito a 7 intentos (ya que maximo son 7 imagenes)
            if tries == 7:
                display_board(hidden_word, tries)
                print('')               # espacio (visual)
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break   #salgo del loop

        
        else:                        #si fue exitoso, reemplazar la letra dentro de la palabra escondida hidden word 
            for idx in letter_indexes:    #itero y reemplazo el indice en la palabra escondida
                hidden_word[idx] = current_letter  #se reemplazara la letra por "-" accediendo a los indices
            
            #importante: vaciar la variable donde estoy contando los indices
            letter_indexes = [] #le asigno espacio vacio
            
        
        #Si ya se reemplazaron todos los "-" es porque ya se adivinaron todas las letras y se gano el juego.
        #si se encuentra un errorse manejara con try y except:
        try:
            hidden_word.index('-') #se utliza la funcion index para cuestionar si se encuentra un elemento dentro de una lista
        except ValueError:  #este error demuestra que ganaste
            print('')               # espacio (visual)
            print('¡Felicidades, ganaste! La palabra es {}'.format(word))
            break
 
        
       
if __name__ == '__main__':
    print('B I E N V E N I D O S  A L  A H O R C A D O')
    run()

