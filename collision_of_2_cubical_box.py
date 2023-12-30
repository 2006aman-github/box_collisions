import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


# screen dimensions
screenwid = screen.get_width()
screenht = screen.get_height()

# font
font = pygame.font.Font('freesansbold.ttf', 28)
font_small = pygame.font.Font('freesansbold.ttf', 18)


# physical vars
E = 1

# platform
PLATFORM_OFFSET = 0.75
platformy = screenht*(PLATFORM_OFFSET)
platformx = 0


# box1
box1ht = 150
box1wid = box1ht
box1_pos_y = platformy-box1ht
box1_pos_x = screenwid/2
box1mass = 1400
box1vel = 0

# box2
box2wid = 80
box2ht = box2wid
box2_pos_y = platformy-box2ht
box2_pos_x = screenwid/4
box2mass = 1
box2vel = 0

no_of_collisions = 0

text = font.render('Mass: '+str(box1mass), True, "white")
box2mass_text = font_small.render('Mass: '+str(box2mass), True, "white")


textRect = text.get_rect()
box2masstextRect = box2mass_text.get_rect()


while running:
    # poll for events
    dt = clock.tick(600)/1000
    if (no_of_collisions == 0):
        box1vel = 300*(-dt)
    collision_text = font.render(
        "# Collisons: "+str(no_of_collisions), True, "white")
    collisionRect = collision_text.get_rect()
    collisionRect.center = (screenwid/2, screenht*.1)

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # platform rendering
    pygame.draw.rect(screen, "white", (platformx, platformy,
                     screenwid, screenht*(1-PLATFORM_OFFSET)))
# box rendering
    pygame.draw.rect(screen, "blue", (box1_pos_x,
                     box1_pos_y, box1wid, box1ht))
    pygame.draw.rect(screen, "orange", (box2_pos_x,
                     box2_pos_y, box2wid, box2ht))
    # text rendering
    textRect.center = (box1_pos_x+80, box1_pos_y-20)
    box2masstextRect.center = (box2_pos_x+35, box2_pos_y-20)

    screen.blit(collision_text, collisionRect)
    screen.blit(text, textRect)
    screen.blit(box2mass_text, box2masstextRect)

# moving boxes
    if (box1_pos_x <= 0):
        box1vel = - box1vel
        pass


# collision detector
    if (box1_pos_x <= box2_pos_x+box2wid):
        no_of_collisions += 1
        temp = box2vel
        box2vel = (((2*box1mass)/(box1mass + box2mass))*box1vel -
                   ((box1mass - box2mass)/(box1mass + box2mass))*box2vel)

        box1vel = (((box1mass - box2mass)/(box1mass + box2mass)) *
                   box1vel + ((2*box2mass)/(box1mass + box2mass))*temp)
        collision_detected = True
    elif (box2_pos_x+box2wid >= box1_pos_x):
        no_of_collisions += 1
        temp = box2vel
        box2vel = (((2*box1mass)/(box1mass + box2mass))*box1vel -
                   ((box1mass - box2mass)/(box1mass + box2mass))*box2vel)

        box1vel = (((box1mass - box2mass)/(box1mass + box2mass)) *
                   box1vel + ((2*box2mass)/(box1mass + box2mass))*temp)
        collision_detected = True

    if ((box2_pos_x+box2vel <= 0)):
        no_of_collisions += 1
        box2vel = -box2vel
        box2_pos_x += box2vel

    else:
        box2_pos_x += box2vel
        # box 1 move logic

    box1_pos_x += box1vel

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos_y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos_y += 300 * dt
    if keys[pygame.K_a]:
        box1_pos_x -= 300 * dt
    if keys[pygame.K_d]:
        box1_pos_x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(600)

    # limits FPS to 60
pygame.quit()
