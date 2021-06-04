import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))


def keyPressed(keyName):
    pressed = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        pressed = True
    pygame.display.update()

    return pressed


if __name__ == "__main__":
    init()
    while True:
        if (keyPressed('a')):
            print("A is pressed")
        if (keyPressed('b')):
            print("B is pressed")

# import sys,pygame
# pygame.init()

# size=width,height=320,240
# speed=[2,2]
# black =0,0,0
# screen=pygame.display.set_mode(size)
# ball=pygame.image.load('Intro_ball.gif')
# ballrect=ball.get_rect()
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT : sys.exit()
#         ballrect=ballrect.move(speed)
#         if ballrect.left < 0 or ballrect.right >width:
#             speed[0]=-speed[0]
#         if ballrect.top < 0 or ballrect.bottom >height:
#             speed[1]=-speed[1]
#         screen.fill(black)
#         screen.blit(ball,ballrect)
#         pygame.display.flip()
