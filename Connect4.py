import pygame
import sys
Type = 0
gameIsPlayed = False
########COLOURS######### (R,G,B)
Gray = (128,128,128)
Black = (0,0,0)
White = (225,225,225)
Red = (255,0,0)
Green = (0,225,0)
Blue = (0,0,225)
Yellow = (255,225,0)
########################
(swidth, sheight) = (700, 600) #screen w/h
(bwidth, bheight) = (6,5) #board w/h -1
############################
Rx_pos = 0
Ry_pos = 0
Rwidth = 50
Rheight = 50
##################### All placeholders
Cx_pos = 50
Cy_pos = 50
Radius = 50
Thinkness = 50
Color = White
####################

screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('Connect 4')
screen.fill(Gray) #background color
pygame.display.flip() #lowkey no clue what this does, stack overflow people like it tho
pygame.event.pump()

# make the rectangle variable
rectangle = pygame.Rect(Rx_pos, Ry_pos, Rwidth, Rheight)

################ Basic functions to draw basic shapes###########################
def make_rect():
    pygame.draw.rect(screen, Gray, rectangle)
    pygame.display.update()

def make_circle(Color, Cx_pos, Cy_pos):
    pygame.draw.circle(screen, Color, (Cx_pos, Cy_pos), Radius, Thinkness)  # (Surface, color, Cx_pos, Cy_pos, radius, thinkness)
    pygame.display.update()

def make_circle_color(Color):
    pygame.draw.circle(screen, Color, (Cx_pos, Cy_pos), Radius, Thinkness) #(Surface, color, Cx_pos, Cy_pos, radius, thinkness)
    pygame.display.update()
#################################################################################

def PlacementCheck(ColorInput):
    pygame.event.pump()
    ycheck = 550
    x_pos = -50
    rowinput = 0


    rowinput = int(input("Enter your row input (1-7): "))
    for z in range(rowinput):
        x_pos += 100

    while ycheck > 0:
        check = screen.get_at((x_pos, ycheck))  #grabs color of circle starting at the bottom
        if check == (225,225,225):
            make_circle(ColorInput, x_pos, ycheck)
            break
        else:
            ycheck -= 50
    ycheck = 550
    if ColorInput == Red:
        ColorInput = Yellow
    elif ColorInput == Yellow:
        ColorInput = Red






def Play_Game():
    game = True
    print("Welcome to Connect 4!")
    print("Player 1 Turn")
    while game == True:
        PlacementCheck(Red)
        PlacementCheck(Yellow)



make_circle_color(White)
pygame.display.update()
i = 6
j = 6
for col in range(j):
    for row in range(i):
        Cx_pos += 100
        make_circle_color(White)
    Cx_pos = 50
    make_circle_color(White)
    Cy_pos += 100
Cy_pos = 50
Play_Game()

####################################no clue what any if this does tbh
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
######################################






