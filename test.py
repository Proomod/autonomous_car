import pygame
pygame.init()
print("Joysticks", pygame.joystick.get_count())
myJoystick = pygame.joystick.Joystick(0)
myJoystick.init()
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        print(myJoystick.get_axis(0), myJoystick.get_axis(1),
              myJoystick.get_axis(2), myJoystick.get_axis(3))
        clock.tick(40)
pygame.quit()