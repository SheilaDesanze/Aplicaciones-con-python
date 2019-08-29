#!/usr/bin/env python
# coding: utf-8

# # Juego - Encriptar mensajes usando diccionarios

# Encriptar un mensaje es modificarlo de forma que si alguien que no conoce la clave e intenta leerlo no va a poder hacerlo.
# La criptografía se usa desde hace miles de años, un gran ejemplo es cuándo Julio Cesar por ejemplo encriptaba mensajes simplemente modificando el orden de las letras.
# 
# El siguiente script es un ejemplo de encriptación de mensajes sencillo, pensar en él más como un juego que como una forma real de cifrar mensajes en la actualidad. Hay API’s de cifrado de mensajes mas especializadas y complejas de mucha mas utilidad.

# In[7]:


#primer paso: defino a un diccionario con el alfabeto como llave, en mayuscula y minuscula
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}




#segundo paso: defino a una funcion para cifrar (para encriptar)
def cypher(message):
    #separamos la oracion a cifrar a traves de espacios y recorremos cada palabra donde se evaluara letra por letra si la letra esta dentro del diccionario y se obtendran los valores de tal manera que se construya al final el mensaje cifrado
    words = message.split(' ') #cada vez que se encuentre un espacio se generara una nueva palabra
    cypher_message = [] #se genera otra variable, como una lista vacia 

    #iteramos a lo largo de las palabras
    for word in words:
        cypher_word = '' #declaramo una variable vacia
        for letter in word: #y por cada letra en la palabra se agarra el cypherword y se construira letra por letra el mensaje cifrado
            cypher_word += KEYS[letter]  #se accede al mapa de llave y cada letra servirá como una llave. Regresará el valor y ese valor se asignara al cypherword. Una vez terminada esta iteracion se añadirá la palabra cifrada a la variable cypher message

        cypher_message.append(cypher_word)

        
        #por ultimo se recontruira el mensaje, y para eso se utilizara el metodo join, generando un string que diga que para cada espacio junte el mensaje cifrado.
    return ' '.join(cypher_message)
    
    #Resumen de cifrado: se descontruyo el mensaje en cada una de sus letras, primero diviendolo por espacios y luego las palabras en letras. Las letras las utilizamos como llaves dentro del diccionario y se obtuvo el valor que sera la palabra cifrada. Se recontruye el string de nuevo y se regresa como un mensaje cifrado.
    

    
    
#tercer paso: defino a una funcion para descifrar (para desencriptar)
def decipher(message):
    #para descifrar hay que recorrer el diccionario pero en sentido contrario, teniendo los valores hay que reconstruir el mensaje original. 
    words = message.split(' ') #dividir el mensaje por espacios
    decipher_message = []   #genero variable inicializada como una lista vacia
    
    for word in words:        # se itera, por cada palabra dentro de las palabras
        decipher_word = ''    # se declarara una variable de descifrado como una string vacia
        
        for letter in word:  #iterar por cada una de las letras, por cada letra en las palabra
            #como no se puede acceder directamente al diccionario a traves de su valor, se iterara a lo largo de todas las llaves, y si se encuentra el valor entonces se podra obtener la llave.
            for key, value in KEYS.items():    #por cada llave y cada valor en las llaves se evalua:
                if value == letter:                #si el valor es igual a la letra, lo encontramos
                    decipher_word += key         #se utilizara la llave, asignandola a la variable decipher_word y se ira concatenando cada letra
            
        #se añadira cada palabra dentro del mensaje para formar la oracion
        decipher_message.append(decipher_word)   
            
            
    return ' '.join(decipher_message)      #se reconstruye la oracion con el mensaje de cifrado
                             
   #Resumen del descifrado: se recibe el mensaje, se divide en espacios, se tiene una lista de palabras. Se declara una variable en donde se guardaran las palabras que se han descifrado (En una lista que se reconstruira al final). Se itera cada palabra, se divide en letras, se evalua si cada letra se encuentra dentro del diccionario, y si se encuentra significa que se ha encontrado su llave a traves del valor, entonces esta llave se mete en la palabra descifrada. Se va reconstruyendo y cuando se termina de reconstruir la palabra se mete en la lista de palabras y por ultimo se une con un espacio y se regresa el mensaje. 
            
          
        
        
def run():

    while True:
        
        #cuarto paso: comando interactivo para saber que quiere hacer el usuario
        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            #quinto paso: implementar el cifrado
            message = str(input('Escribe tu mensaje para cifrar: '))
            cypher_message = cypher(message)
            print(cypher_message)  #esto llama a la funcion de cifrado del segundo paso
                     
            
        elif command == 'd':
            #sexto paso: implementar el descifrado
            message = str(input('Escribe tu mensaje cifrado: '))   #obtener un mesaje
            decypher_message = decipher(message) #una vez que se tiene el mensaje se llama a la funcion para descifrar con el mensaje como parametro, el resultado se almacenara en la variable decypher_message
            print(decypher_message)     #esto llama a la funcion de descifrado del tercer paso
            
            
        elif command == 's':
            print('Juego finalizado')
            break
            
        else:
            print('¡Comando no encontrado!')


            
            
if __name__ == '__main__':
    print('J U E G O   D E   M E N S A J E S   C I F R A D O S')
    run()

