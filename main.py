import fd3de
import curses
import atexit
import wall_mover as WM
import os
import time
import random


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)

atexit.register(curses.endwin)
WM.main()

nave = fd3de.load("Modelos/nave.fd3de")


fd3de.rotate("y", 180, nave)
fd3de.rotate("x", -10, nave)

fd3de.move("z", -150, nave)
fd3de.move("y", -100, nave)


laseres = []
piedras = []
last_shot = 0

def render():
	fd3de.render(nave, fd3de.RED, 0.9)
	fd3de.update()

	fd3de.clear_object(nave, 0.9)

	for l in laseres:
		fd3de.clear_object(l)

	for p in piedras:
		fd3de.clear_object(p,0.3)




def shoot():
	nuevo_laser = fd3de.load("Modelos/laser.fd3de")
	fd3de.move("x", nave["position"][0] - nuevo_laser["position"][0], nuevo_laser)
	fd3de.move("y", nave["position"][1] - nuevo_laser["position"][1], nuevo_laser)
	fd3de.move("z", nave["position"][2] - nuevo_laser["position"][2] + 50, nuevo_laser)
	laseres.append(nuevo_laser)


	

while True:

	# Detectar entradas de teclado
	#-----------------------------
	key = stdscr.getch()

	if key == curses.KEY_RIGHT and nave["position"][0] < 180:	
		fd3de.move("x", 10, nave)
		nave["rotation"][2] = -15
		


		curses.flushinp()

	elif key == curses.KEY_LEFT and nave["position"][0] > -180:
		fd3de.move("x", -10, nave)
		nave["rotation"][2] = 15
		
		curses.flushinp()

	elif key == 32:
		if time.time() - last_shot > 0.2:
			last_shot = time.time()
			shoot()
	
		curses.flushinp()

	else:
		fd3de.rotate("z", nave["rotation"][2]*-1, nave)




	# Generar y mover piedras
	#-------------------------
	if len(piedras) < 5:
		random_rot = random.randint(0,90)
		while True:
			random_z = random.randint(-150,150)
			random_x = random.randint(-180,180)
			ok = True
			
			for p in piedras:
				if abs(random_x - p["position"][0]) < 100 and abs(random_z - p["position"][2]) < 150:
					ok = False
					break

			if ok:
				break 	


		piedra = fd3de.load("Modelos/cubo.fd3de")
		fd3de.move("z", 600 + random_z, piedra)
		fd3de.move("y", -100, piedra)
		fd3de.move("x", random_x, piedra)
		
		fd3de.rotate("y", random_rot, piedra)
		fd3de.rotate("x", random_rot, piedra)

		piedras.append(piedra)


	for p in range(len(piedras)-1, -1, -1):
		fd3de.move("z", -3, piedras[p])
		fd3de.render(piedras[p], fd3de.GREEN, 0.3)

		if piedras[p]["position"][2] < -100:
			fd3de.clear_object(piedras[p], 0.3)
			del piedras[p]
			print("Has perdido")
			exit()




	# Mover y eliminar láseres
	#--------------------------
	for n in range(len(laseres)-1, -1, -1):
		fd3de.move("z", 20, laseres[n])
		fd3de.render(laseres[n], fd3de.WHITE)

		if laseres[n]["position"][2] > 800:
			fd3de.clear_object(laseres[n])
			del laseres[n]

	# Colision de los láseres
	#-------------------------
	for n in range(len(laseres)-1, -1, -1):
		for i in range(len(piedras)-1, -1, -1):
			if abs(laseres[n]["position"][0] - piedras[i]["position"][0]) < 30 and abs(laseres[n]["position"][2] - piedras[i]["position"][2]) < 30:
				fd3de.clear_object(piedras[i],0.3)
				fd3de.clear_object(laseres[n])
				del piedras[i]
				del laseres[n]
				break


	render()