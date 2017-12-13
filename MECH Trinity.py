#Mech Trinity
from game_lib import *

pygame.init()
gameDisp = pygame.display.set_mode((disp_width, disp_height), 0, 32)
gameDisp.fill((WHITE))
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
g_menu = menu(disp_width, disp_height)
g_menu.render(gameDisp)
gClock = pygame.time.Clock()

#Menu loop
menu = True
while menu:
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
    if click == "play":
        menu = False
        break
    if click == "instructions":
        g_menu.instructions()
    pygame.display.flip()
    gClock.tick(FPS)

#Game loop
#testServer = Server(10, 30)
#print(testServer.myInfo())
#while True:
    #testServer.work()
    #conns = testServer.myConns()
    #if len(conns) > 0:
        #print(conns)
        #for person in conns:
            #msg = testServer.recieve(person)
            #print(msg)
        #testServer.broadcast(msg)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_W:
                pass
            if event.key == pygame.K_S:
                pass
            if event.key == pygame.K_A:
                pass
            if event.key == pygame.K_D:
                pass

    gameDisp.fill(BLACK)
    pygame.display.flip()
    gClock.tick(FPS)
