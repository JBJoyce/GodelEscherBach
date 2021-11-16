import pygame
import numpy
from math import pi, sin, cos, sqrt

WIDTH, HEIGHT = 900, 600
WHITE =(255,255,255) 
BLUE = (202,228,241)
BLACK =(0,0,0)
LT_GRAY = (192,192,192)
DK_GRAY = (150,150,150)
FPS = 30

pygame.init()

ITER_FONT = pygame.font.SysFont('sanserif', 25)
BUT_FONT = pygame.font.SysFont('sanserif', 15)
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Starts Upper left hand corner
GUI = pygame.Surface((WIDTH - HEIGHT, HEIGHT)) 
IMAGE = pygame.Surface((HEIGHT, HEIGHT))
pygame.display.set_caption("Koch Fractals")
ICON = pygame.image.load("fractal.png") # image courtesy Freepik
pygame.display.set_icon(ICON)

##TODO: Add comments

class Koch:
	str_curve = "F"
	str_snowflake = "F--F--F--"
	theta = 0
	
	def __init__(self): 
		self.string = ''
		self.depth = 0
		self.sp = (0,0)
		self.width = 0
		
	def inc_depth(self):
		if self.depth <= 9:
			self.depth += 1	
		
	def dec_depth(self):
		if self.depth >= 1:
			self.depth -= 1	
		
	def lindenmeyer(self):
		for i in range(0, self.depth):	
			self.string = self.string.replace("F", "F+F--F+F")	
			
	def draw_curve(self):
		temp_image = pygame.Surface((HEIGHT, HEIGHT))
		temp_image.fill(WHITE)
		self.lindenmeyer()
		increment = self.width * (1/3) ** self.depth
		for char in self.string:
			if char == "F":
				ep = (self.sp[0] + (increment * cos(self.theta)), self.sp[1] - (increment * sin(self.theta)))
				pygame.draw.line(temp_image, BLACK, self.sp, ep)
				self.sp = ep
			if char == "+":
				self.theta += pi/3
			if char == "-":
				self.theta -= pi/3	
		return temp_image							
		print("DRAWN")		
				
					
class Button:
	def __init__(self, color, x, y, width, height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		
	def draw(self, win, outline=None):
		if outline:
			pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
		
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height),0)
		
		if self.text != '':
			text = BUT_FONT.render(self.text, 1, (0,0,0))
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
			
	def isOver(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		
		return False					 	

koch = Koch()
curve_button = Button(LT_GRAY, 110, 100, 100, 30, "Draw Koch Curve")
flake_button = Button(LT_GRAY, 110, 150, 100, 30, "Draw Snowflake")
plus_button = Button(LT_GRAY, 110, 250, 45, 30, "+")
minus_button = Button(LT_GRAY, 160, 250, 45, 30, "-")

WIN.fill(WHITE)
GUI.fill(DK_GRAY)
IMAGE.fill(WHITE)
curve_button.draw(GUI, outline=True)
flake_button.draw(GUI, outline=True)
plus_button.draw(GUI, outline=True)
minus_button.draw(GUI, outline=True)

WIN.blit(GUI, (0,0))
WIN.blit(IMAGE, (300,0))

def main():
	clock = pygame.time.Clock()
	
	running = True
	
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				running = False
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				if curve_button.isOver(pos):
					koch.string = koch.str_curve
					koch.sp = (0,300)
					koch.width = 600
					IMAGE.blit(koch.draw_curve(), (0,0))	
					
				if flake_button.isOver(pos):
					koch.string = koch.str_snowflake
					koch.sp = (200,200)
					koch.width = 200
					IMAGE.blit(koch.draw_curve(), (0,0))
					
				if plus_button.isOver(pos):
					koch.inc_depth()
					print(koch.__dict__)
					drawing = True
					
				if minus_button.isOver(pos):
					koch.dec_depth()
					print(koch.__dict__)
					drawing = True
					
		WIN.blit(IMAGE, (300,0))			
		pygame.display.update()			

	pygame.quit()




if __name__ == "__main__":
	main()
