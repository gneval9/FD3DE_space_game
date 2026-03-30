import fd3de
import threading
import FD_FontLoader as FL

FL.load_font("VeFont.txt")

nave = fd3de.load("Modelos/nave.fd3de")
cubo = fd3de.load("Modelos/cubo.fd3de")

FL.draw_char("F",100,100,10,fd3de.RED)
FL.draw_char("D",150,100,10,fd3de.RED)
FL.draw_char("3",200,100,10,fd3de.RED)
FL.draw_char("D",250,100,10,fd3de.RED)
FL.draw_char("E",300,100,10,fd3de.RED)

FL.draw_char("S",100,150,7,fd3de.RED)
FL.draw_char("p",130,150,7,fd3de.RED)
FL.draw_char("a",160,150,7,fd3de.RED)
FL.draw_char("c",190,150,7,fd3de.RED)
FL.draw_char("e",220,150,7,fd3de.RED)
FL.draw_char("g",250,150,7,fd3de.RED)
FL.draw_char("a",280,150,7,fd3de.RED)
FL.draw_char("m",310,150,7,fd3de.RED)
FL.draw_char("e",340,150,7,fd3de.RED)


fd3de.move("y", -200, cubo)
fd3de.move("y", -50, nave)
fd3de.move("x", 100, cubo)
fd3de.move("x", 100, nave)
fd3de.move("z", -50, nave)

fd3de.rotate("y", 50, nave)
fd3de.rotate("x", -5, nave)

def render_all():
	fd3de.render(cubo, fd3de.WHITE)
	fd3de.render(nave, fd3de.RED, 2)
	fd3de.update()

	fd3de.clear_object(cubo)
	fd3de.clear_object(nave, 2)




def subir():
	for n in range(50):
		fd3de.move("y", 2, nave)
		render_all()

def rotar_y():
	for n in range(50):
		fd3de.rotate("y", 2, nave)
		render_all()


def rotar_x():
	for n in range(15):
		fd3de.rotate("x", 2, nave)
		render_all()


def irse_a_tomar_por_culo():
	for n in range(60):
		fd3de.move("z", 20, nave)
		fd3de.move("x", -10, nave)
		fd3de.move("y", 5, nave)
		
		fd3de.rotate("z", -0.1, nave)
		render_all()

subir()
rotar_y()
rotar_x()
irse_a_tomar_por_culo()
