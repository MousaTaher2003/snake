# Call libraries
import pygame
import random
import time
# Initialization Pygame
pygame.init()
# Screen settings
screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
# Name of the game
pygame.display.set_caption('Snake Game')
# Image of snake head
hsnakeImg = pygame.image.load('images/hsnake.png')
# Image of a snake's body
bsnakeImg = pygame.image.load('images/bsnake.png')
# Image of a falcon
pontgreesa = pygame.image.load('images/pngtrees.png')
# Image of a Rabbit
rabbit = pygame.image.load('images/rabbit.png')
# To set your Game Icon
gameIcon = pygame.image.load("images/snake.png")
pygame.display.set_icon(gameIcon)
# Image of a background in start Game Screen
backs = pygame.image.load("images/Mousa.gif")
# Background image on the game screen
backb = pygame.image.load("images/de.jpg")
# Background image in the end-game screen
backd = pygame.image.load("images/bacend.jpg")
# Background image on the game stop screen
backp = pygame.image.load("images/backp.png")
backg = backs
# Background
background_image = pygame.transform.scale(backg, (screen_width, screen_height))
# Definition of sound variables
miot = pygame.image.load("images/Miot.png")
unmiot = pygame.image.load("images/unmiot.png")
# Definition of a sound state variable
speaker = unmiot
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
bright_red = (255,0,0)
bright_green = (0,255,0)
frame_color = (200, 210, 150)  # Frame color
#Health booster color
health_boost_color = (0, 255, 255)  
# Snake settings
snake_block = 25
snake_speed = 10
# Power settings
max_health = 100
health = max_health
# Health booster settings
boost_size = 50
boost_speed = 5
# Fire settings
fire_size = 50
fire_speed = 7
# Font settings
font_style = pygame.font.SysFont(None, 50)
timer_font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()
# Definition of sound variables
pygame.mixer.music.load('sounds/soundBack.mp3')
boost_sound = pygame.mixer.Sound("sounds/bgstart.mp3")
mtab = pygame.mixer.Sound("sounds/huh.mp3")
eat_sound = pygame.mixer.Sound("sounds/hissing.mp3")
fire_sound = pygame.mixer.Sound("sounds/rattles.mp3")
# Game state
pause = False
bump_color = (139, 69, 19)  # The color of the bumps
# Variable sound condition
sound_on = True
def draw_health_bar(health):
    pygame.draw.rect(screen, red, [10, 10, max_health * 2, 20])
    pygame.draw.rect(screen, green, [10, 10, health * 2, 20])
# Scour
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Scour: "+str(count), True, red)
    screen.blit(text,(screen_width-150,0))
# Font settings   
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
# Loss
def crash():
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameLoop()
                if event.key == pygame.K_q:
                    quitgame()
        backg = backd 
        background_image = pygame.transform.scale(backg, (screen_width, screen_height))
        screen.blit(background_image, [0, 0])
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((screen_width/2),(screen_height/2-100))
        screen.blit(TextSurf, TextRect)
        button("Play Again",screen_width/2-150,screen_height/2,100,50,green,bright_green,gameLoop)
        button("Quit",screen_width/2+150,screen_height/2,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)       
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
def unpause():
    global pause
    pause = False
def display_timer(start_time):
    elapsed_time = time.time() - start_time
    timer_text = timer_font.render(f'Time: {int(elapsed_time)}s', True, white)
    screen.blit(timer_text, [10, 50])
def paused():
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                health = max_health
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c or event.key == pygame.K_KP_ENTER:
                    pygame.mixer.music.play(-1,0.0)
                    unpause()
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    health = max_health
                    pygame.quit()
                    quit()
        backg = backp
        background_image = pygame.transform.scale(backg, (screen_width, screen_height))
        screen.blit(background_image, [0, 0])
        button("Continue",screen_width/2-150,screen_height/2,100,50,green,bright_green,unpause)
        button("Quit",screen_width/2+150,screen_height/2,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
def our_snake(snake_block, snake_List):
    # Draw the head of a snake
    screen.blit(hsnakeImg,[snake_List[-1][0], snake_List[-1][1], snake_block, snake_block])
    # Draw the snake's body
    for x in snake_List[:-1]:
        screen.blit(bsnakeImg,[x[0], x[1], snake_block, snake_block])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])
def quitgame():
    pygame.quit()
    quit()
def game_intro():
    pygame.mixer.music.stop()
# This is for the First Screen
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                health = max_health
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g or event.key == pygame.K_KP_ENTER:
                        health = max_health
                        gameLoop()
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        health = max_health
                        quitgame() 
        screen.blit(background_image, [0, 0])
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("", largeText)
        TextRect.center = ((screen_width/2),(screen_height/2-100))
        screen.blit(TextSurf, TextRect)
        button("GO!",screen_width/2-150,screen_height/2,100,50,green,bright_green,gameLoop)
        button("Quit",screen_width/2+150,screen_height/2,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
def gameLoop():
    
    pygame.mixer.music.play(-1,0.0)
    global health,pause,speaker,sound_on
    health = max_health
    speaker = unmiot
    game_over = False
    start_time = time.time()
    food = pygame.image.load('images/food.png')
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    dodged = 0
    snake_List = []
    Length_of_snake = 1
    snake_speed = 7
    # Health booster settings
    foodx = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
    fires = []
    boosts = []
    # Bump settings
    bump_length = snake_block
    bumps = []
    for _ in range(5):  # Add 5 bumps
        bump_x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
        bump_y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
        bumps.append([bump_x, bump_y])
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.mixer.music.stop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_width-100<= mouse[0] <= screen_width-50 and 50  <= mouse[1] <= 100:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                        speaker = miot
                    else :
                        pygame.mixer.music.play(-1,0.0)
                        speaker = unmiot
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        game_over = True
                        pygame.mixer.music.stop()
                if event.key == pygame.K_r:
                        game_intro()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_m:  # Activate pause and play sound when pressing M
                    if sound_on:
                        pygame.mixer.music.stop()
                        speaker = miot
                    else:
                        pygame.mixer.music.play(-1,0.0)
                        speaker= unmiot
                    sound_on = not sound_on
        mouse = pygame.mouse.get_pos()
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:  
            crash()
        x1 += x1_change
        y1 += y1_change
        backg = backb
        background_image = pygame.transform.scale(backg, (screen_width, screen_height))
        screen.blit(background_image, [0, 0])
        screen.blit(food,[foodx, foody, snake_block, snake_block])
        screen.blit(speaker, pygame.draw.rect(screen,(127,127,127),[screen_width-100,50,50,50]))
        #pygame.draw.rect(screen, frame_color, [0, 0, screen_width, screen_height], 10)  # The frame is 10 pixels thick
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                crash()
        # 2% probability of adding a new fire every frame
        if random.randint(1, 100) <= 2:  
            fire_x = random.randint(0, screen_width - fire_size)
            # Fire starts from the top of the screen
            fire_y = 0  
            fires.append([fire_x, fire_y])
        # Move the fire
        for fire in fires:
            fire[1] += fire_speed
            screen.blit(pontgreesa, [fire[0], fire[1], fire_size, fire_size])
            #pygame.draw.rect(screen, fire_color, [fire[0], fire[1], fire_size, fire_size])
            if fire[1] > screen_height:
                fires.remove(fire)
        # Check collision between fire and snake
            if x1 < fire[0] < x1 + snake_block or x1 < fire[0] + fire_size < x1 + snake_block:
                if y1 < fire[1] < y1 + snake_block or y1 < fire[1] + fire_size < y1 + snake_block:
                    health -= 10
                    fires.remove(fire)
                    if health <= 0:
                         crash()
            # Add health boosters randomly
            if random.randint(1, 200) <= 1:  # Possibility of adding a new health booster
                boost_x = random.randint(0, screen_width - boost_size)
                boost_y = 0  # The health boost starts at the top of the screen
                boosts.append([boost_x, boost_y])
            # Move the health booster
            for boost in boosts:
                boost[1] += boost_speed
                screen.blit(rabbit, [boost[0], boost[1], boost_size, boost_size])
                #pygame.draw.rect(screen, health_boost_color, [boost[0], boost[1], boost_size, boost_size])
                if boost[1] > screen_height:
                    boosts.remove(boost)
            # Check collision between health booster and snake
                if x1 < boost[0] < x1 + snake_block or x1 < boost[0] + boost_size < x1 + snake_block:
                    if y1 < boost[1] < y1 + snake_block or y1 < boost[1] + boost_size < y1 + snake_block:
                        health += 20
                        boost_sound.play()
                        time.sleep(0.2)
                        if health > max_health:
                            health = max_health
                        boosts.remove(boost)
        # Draw the bumps
        for bump in bumps:
            pygame.draw.rect(screen, bump_color, [bump[0], bump[1], bump_length, snake_block])
            # Check collision between snake and bumps
            if x1 == bump[0] and y1 == bump[1]:
                health-=10
                mtab.play()  # Play sound when the snake hits a bump 
                time.sleep(0.2)
                if health <= 0:
                    crash()
            mtab.stop()
        our_snake(snake_block, snake_List)
        draw_health_bar(health)  # Show power bar
        things_dodged(dodged)
        display_timer(start_time)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            eat_sound.play()  # Play sound when snake eats food
            time.sleep(0.2)
            foodx = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            if dodged <= 5:
                dodged +=1
                snake_speed = 7
            elif dodged > 5 and dodged <= 10 :
                dodged += 2 
                snake_speed = snake_speed * 1.1
            elif dodged > 10 and dodged <= 20 :
                dodged += 3
                snake_speed = snake_speed * 1.3
            elif dodged > 20 and dodged <= 30 :
                dodged += 4
                snake_speed = snake_speed * 1.5
            elif dodged > 30 and dodged <=50 :
                dodged += 5
                snake_speed = snake_speed * 1.7
            else:
                dodged += 6
                snake_speed = dodged/40
        clock.tick(snake_speed) 
        eat_sound.stop() # Stop sound    
game_intro()
gameLoop()
pygame.quit()
quit()