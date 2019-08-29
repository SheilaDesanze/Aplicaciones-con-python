#!/usr/bin/env python
# coding: utf-8

# # Juego del ahorcado con Python (Versión 2)

# In[ ]:


import turtle
import random

wn = turtle.Screen()
flash = turtle.Turtle()

def draw_scenary():
    # Estructura
	flash.forward(50)
	flash.left(90)
	flash.forward(120)
	flash.left(90)
	flash.forward(50)
	flash.left(90)
	flash.forward(20)


def draw_stick(tries, should_draw):
	if not should_draw:
		return

	if tries == 1:
		# Cabeza
		flash.penup()
		flash.setposition(0, 100)
		flash.setheading(180)
		flash.pendown()
		flash.circle(10)
	elif tries == 2:
		# Cuerpo #1
		flash.penup()
		flash.setposition(0, 80)
		flash.setheading(270)
		flash.pendown()
		flash.forward(20)
	elif tries == 3:
		# Brazo derecho
		flash.penup()
		flash.setposition(0, 70)
		flash.setheading(-45)
		flash.pendown()
		flash.forward(20)
	elif tries == 4:
		# Brazo izquierdo
		flash.penup()
		flash.setposition(0, 70)
		flash.setheading(225)
		flash.pendown()
		flash.forward(20)
	elif tries == 5:
		# Cuerpo #2
		flash.penup()
		flash.setposition(0, 58)
		flash.setheading(270)
		flash.pendown()
		flash.forward(18)
	elif tries == 6:
		# Pierna derecha
		flash.penup()
		flash.setposition(0, 40)
		flash.setheading(-45)
		flash.pendown()
		flash.forward(20)
	elif tries == 7:
		# Pierna izquierda
		flash.penup()
		flash.setposition(0, 40)
		flash.setheading(225)
		flash.pendown()
		flash.forward(20)


WORDS = [
	'lavadora',
	'secadora',
	'sofa',
	'gobierno',
	'diputado',
	'democracia',
	'computadora',
	'teclado'
]


def random_word():
    # Se obtiene una palabra random
	return WORDS[random.randint(0, len(WORDS) - 1)]


def display_board(hidden_word, tries, should_draw):
	draw_stick(tries, should_draw)
	print('')
	print(hidden_word)


def run():
	# Preparativos
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	# Primero se dibuja el escenario
	draw_scenary()

	# Indica si se debe dibujar
	should_draw = False

	# Inicio del juego
	while True:
		display_board(hidden_word, tries, should_draw)
		current_letter = str(input("Escoge una letra: "))

		should_draw = False
		letter_indexes = []

		for i in range(len(word)):
			if word[i] == current_letter:
				letter_indexes.append(i)

		if len(letter_indexes) == 0:
			tries += 1
			should_draw = True

			if tries == 7:
				display_board(hidden_word, tries, should_draw)
				print('')
				print('¡Perdiste! La palabra correcta era {}'.format(word))
				draw_stick(7, should_draw)
				break
		else:
			for i in letter_indexes:
				hidden_word[i] = current_letter


		try:
			hidden_word.index('-')
		except ValueError:
			print('')
			print('¡Felicidades! Ganaste. La palabra es {}'.format(word))
			break



if __name__ == "__main__":
    print('B I E N V E N I D O S   AL   A H O R A C A D O')
    run()

