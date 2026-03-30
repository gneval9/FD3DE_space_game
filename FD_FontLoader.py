# Made and developed by gneval9 Software
# 04-10-2025

import framedirect as FD

FD.init()

def load_font(path):
	global font
	file = open(path)
	font = eval(file.read())

def draw_char(char, x, y, scale, color):
	global font
	for n in range(len(font[char])):
		FD.draw_line((font[char][n][0][0] * scale) + x, (font[char][n][0][1] * scale) + y, (font[char][n][1][0] * scale) + x, (font[char][n][1][1] * scale) + y, color)


def update():
	FD.update()
