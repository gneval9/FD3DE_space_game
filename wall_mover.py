import fd3de
import time
import os

walls_r = []
walls_l = []


def render(color):
	for n in range(len(walls_r)):
		fd3de.render(walls_r[n], color)
		fd3de.update()
	

	for n in range(len(walls_l)):
		fd3de.render(walls_l[n], color)
		fd3de.update()



def main():
	global walls_l, walls_r

	walls_r = []
	walls_l = []

	for n in range(0,3):
		walls_r.append(fd3de.load("Modelos/wall.fd3de"))
		walls_l.append(fd3de.load("Modelos/wall.fd3de"))


	for n in range(len(walls_r)):
		fd3de.move("y", -100, walls_r[n])
		fd3de.move("x", -360, walls_r[n])

	for n in range(len(walls_l)):
		fd3de.move("y", -100, walls_l[n])
		fd3de.move("x", 360, walls_l[n])

	for n in range(len(walls_r)):
		fd3de.move("z", 400*n, walls_r[n])
		fd3de.move("z", 400*n, walls_l[n])


	render(fd3de.YELLOW)