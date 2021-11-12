import pygame
import numpy
from math import pi, sin, cos, sqrt

width=600
height=600
Color_screen=(255,255,255) #(50,200,255)
Color_line=(0,0,0)
str_curve="F"
str_snowflake="F-F-F-F-F-F-"

pygame.init()

screen = pygame.display.set_mode((width,height)) #Starts Upper left hand corner
pygame.display.set_caption("Koch Fractals")
icon = pygame.image.load("fractal.png") # image courtesy Freepik
pygame.display.set_icon(icon)


## TODO write a class
def lindenmeyer(string, depth):
		for i in range(0, depth):	
			string = string.replace("F", "F+F--F+F")
		return string
			

def draw_curve(depth=0, string=str_curve, sp=(0,(height/2)), width=width, theta=0):
		increment = width * (1/3) ** depth
		for char in string:
			if char == "F":
				ep = (sp[0] + (increment * cos(theta)), sp[1] - (increment * sin(theta)))
				pygame.draw.line(screen, Color_line, sp, ep)
				sp = ep
			if char == "+":
				theta += pi/3
			if char == "-":
				theta -= pi/3

def draw_snowflake(depth=0, string=str_snowflake, sp=(300-100, 300-(200*sqrt(3)/2)), width=200, theta=0):
		increment = width * (1/3) ** depth
		for char in string:
			if char == "F":
				ep = (sp[0] + (increment * cos(theta)), sp[1] - (increment * sin(theta)))
				pygame.draw.line(screen, Color_line, sp, ep)
				sp = ep
			if char == "+":
				theta += pi/3
			if char == "-":
				theta -= pi/3						

running = True
while running:
	screen.fill(Color_screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	draw_snowflake(depth=0, string=lindenmeyer(str_snowflake, depth =0))			
	draw_snowflake(depth=1, string=lindenmeyer(str_snowflake, depth =1))
	draw_snowflake(depth=2, string=lindenmeyer(str_snowflake, depth =2))
	draw_snowflake(depth=3, string=lindenmeyer(str_snowflake, depth =3))
	draw_snowflake(depth=4, string=lindenmeyer(str_snowflake, depth =4))
	#draw_curve(depth=4, string=lindenmeyer("F", depth =4))
	pygame.display.update()

