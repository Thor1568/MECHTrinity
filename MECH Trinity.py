#Mech Trinity
#yayuz
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

text_temp = """Welcome to MECH Trinity, the game designed by Thor1568 as a replacement to the original started in Scratch 2. This game pits humanity against an alien enemy."""
#length is 157

#text_box1 = DialogueBox(disp_width, 450)
#text_box1.add_text(text_temp, 20)
#Thread keeps getting error: TypeError: display_text_th() argument after * must be an iterable, not int
#thread_worker(text_box1.display_text_th, 10)
my_game = Game(800, 600, 0)

while True:
    gameDisp.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            #Miscellaneous keydown events
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            #Movement keydown events
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_d:
                pass
    #Screen updates
    my_game.render(gameDisp)
    pygame.display.flip()
    gClock.tick(FPS)
