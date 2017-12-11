#Mech Trinity
from game_lib import *

pygame.init()
gameDisp = pygame.display.set_mode((disp_width, disp_height), 0, 32)
gameDisp.fill((WHITE))
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
g_menu = menu(disp_width, disp_height)
g_menu.render(gameDisp)


#Menu loop
while True:
    mouse = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    gameDisp.fill(BLACK)
    g_menu.render(gameDisp)
    click = g_menu.handle_mouse(mouse)
    if len(click) > 0:
        print(click)
    pygame.display.flip()

#Game loop
