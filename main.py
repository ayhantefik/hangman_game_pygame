import pygame
import pygame_gui
import sys
import random
mainClock = pygame.time.Clock()
from pygame.locals import *

# https://www.geeksforgeeks.org/hangman-game-in-python/?ref=rp

pygame.init()
WIDTH, HEIGHT = 780, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
background = pygame.image.load("backgroundimage.jpg")
icon = pygame.image.load("hangmanicon.png")
pygame.display.set_icon(icon)
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((420, 80), (150, 35)), manager = MANAGER, object_id = "#main_text_entry")

# Fonts
font = pygame.font.SysFont(None, 30)
btn_font = pygame.font.SysFont('arial', 30)
letter_font = pygame.font.SysFont('arial', 60)
game_font = pygame.font.SysFont('arial', 80)

b1 = False
b2 = False
b3 = False
chosen_word = ""
GUESSED = []


def readHighScore():
    with open("score.txt", "r") as f:
        return f.read()

def getHighScore():
    line = readHighScore()
    val = line.split(" ")
    d = val[1]
    return d

def getHighScorePlayer():
    line = readHighScore()
    val = line.split(" ")
    d = val[0]
    return d

def status_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def display_guess():
    display_word = ''

    for letter in chosen_word:
        if letter in GUESSED:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    text = letter_font.render(display_word, True, BLACK)
    screen.blit(text, (270, 115))

# Buttons

WHITE = (255,255,255)
BLACK = (0,0,0)

ROWS = 2
COLS = 13
GAP = 12
SIZE = 28
BOXES = []

for row in range(ROWS):
    for col in range(COLS):
        x = ((GAP * col) + GAP) + (SIZE * col) + 240
        y = ((GAP * row) + GAP) + (SIZE * row) + 240
        box = pygame.Rect(x,y,SIZE,SIZE)
        BOXES.append(box)

A = 65
BUTTONS = []

for ind, box in enumerate(BOXES):
    letter = chr(A+ind)
    button = ([box, letter])
    BUTTONS.append(button)

def draw_btns(BUTTONS):
    for button,letter in BUTTONS:
        btn_text = btn_font.render(letter, True, BLACK)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, BLACK, button, 2)
        screen.blit(btn_text, btn_text_rect)

def mainmenu():
    run = True
    while run:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(370, 35, 200, 50)
        button_2 = pygame.Rect(370, 105, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                category()
        if button_2.collidepoint((mx, my)):
            if click:
                quit()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        status_text('Start game', font, (255, 255, 255), screen, 390, 50)
        status_text('Quit', font, (255, 255, 255), screen, 390, 120)
        pygame.display.update()
        mainClock.tick(60)

def get_wordAnimal():
    with open("wordsAnimals.txt", 'r') as f:
        # Reads each word after splitting
        words1 = f.read().splitlines()
    # Returns any random word
    return random.choice(words1)
def get_wordCities():
    with open("wordsCities.txt", 'r') as f:
        # Reads each word after splitting
        words1 = f.read().splitlines()
    # Returns any random word
    return random.choice(words1)
def get_wordCountries():
    with open("wordsCountries.txt", 'r') as f:
        # Reads each word after splitting
        words1 = f.read().splitlines()
    # Returns any random word
    return random.choice(words1)

def category():
    while True:
        global chosen_word
        global b1, b2, b3
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.fill((255, 255, 255))
        screen.blit(background, (0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(370, 35, 200, 50)
        button_2 = pygame.Rect(370, 105, 200, 50)
        button_3 = pygame.Rect(370, 175, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                b1 = True
                chosen_word = get_wordCountries()
                playername()
        if button_2.collidepoint((mx, my)):
            if click:
                b2 = True
                chosen_word = get_wordCities()
                playername()
        if button_3.collidepoint((mx, my)):
            if click:
                b3 = True
                chosen_word = get_wordAnimal()
                playername()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        status_text('Countries', font, (255, 255, 255), screen, 390, 50)
        status_text('Cities', font, (255, 255, 255), screen, 390, 120)
        status_text('Animals', font, (255, 255, 255), screen, 390, 190)

        mx, my = pygame.mouse.get_pos()
        backimage = pygame.image.load("backimage.png")
        backimage_position = Rect(250, 180, 76, 56)
        screen.blit(backimage, (250, 180))

        if backimage_position.collidepoint((mx, my)):
            if click:
                mainmenu()

        pygame.display.update()
        mainClock.tick(60)

def playername():
    pname = False
    while not pname:
        click = False
        UI_REFRESH_RATE = mainClock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry'):
                game(event.text)
                pname = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            MANAGER.process_events(event)

        MANAGER.update(UI_REFRESH_RATE)

        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        status_text(f'Your name: ', font, (0, 0, 0), screen, 300, 90)

        mx, my = pygame.mouse.get_pos()
        backimage = pygame.image.load("backimage.png")
        #backimage = pygame.transform.scale(backimage, (76, 56))
        backimage_position = Rect(250, 180, 76, 56)
        screen.blit(backimage, (250, 180))

        if backimage_position.collidepoint((mx, my)):
            if click:
                category()

        MANAGER.draw_ui(screen)
        pygame.display.update()

def game(player_name):
    end_of_loop = False
    game_over = False
    global TEXT_INPUT
    global chosen_word
    global b1, b2, b3

    try:
        highScore = int(getHighScore())
    except:
        highScore = 0

    stages = []
    lives = 6
    points = 0
    correct_words = 0
    wordcategory = ""
    highScorePlayer = getHighScorePlayer()

    for i in range(7):
        image = pygame.image.load(f"stages/stage{i}.jpg")
        stages.append(image)
    while not end_of_loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                clicked_pos = event.pos

                for button, letter in BUTTONS:
                    if button.collidepoint(clicked_pos):
                        GUESSED.append(letter)

                        if letter not in chosen_word:
                            lives -= 1
                        else:
                            points += 10
                            if (highScore < points):
                                highScore = points
                                highScorePlayer = player_name

                        if lives == 0:
                            game_over = True

                        BUTTONS.remove([button, letter])

        screen.fill(WHITE)
        screen.blit(stages[lives], (0, 0))
        pygame.draw.rect(screen, BLACK, (250, 5, 180, 60), 3)
        status_text(f'Lives: {lives}', font, (0, 0, 0), screen, WIDTH - 170, 10)
        status_text(f'Player: {player_name}', font, (0, 0, 0), screen, WIDTH - 170, 30)
        status_text(f'Correct words: {correct_words}', font, (0, 0, 0), screen, WIDTH - 170, 50)
        status_text(f'Points: {points}', font, (0, 0, 0), screen, WIDTH - 170, 100)
        status_text(f'High score: {highScore}', font, (0, 0, 0), screen, 260, 10)
        status_text(f'Player: {highScorePlayer}', font, (0, 0, 0), screen, 260, 40)
        if b1 is True:
            wordcategory = "Countries"
        if b2 is True:
            wordcategory = "Cities"
        if b3 is True:
            wordcategory = "Animals"
        status_text(f'- {wordcategory} -', font, (0, 0, 0), screen, WIDTH - 170, 70)
        draw_btns(BUTTONS)
        display_guess()


        won = True
        for letter in chosen_word:
            if letter not in GUESSED:
                won = False

        if won:
            points += 50
            correct_words += 1
            if b1 is True:
                chosen_word = get_wordCountries()
            if b2 is True:
                chosen_word = get_wordCities()
            if b3 is True:
                chosen_word = get_wordAnimal()


            GUESSED.clear()
            lives = 6
            BUTTONS.clear()
            for ind, box in enumerate(BOXES):
                letter = chr(A + ind)
                button = ([box, letter])
                BUTTONS.append(button)

        pygame.display.update()

        if game_over:
            b1 = False
            b2 = False
            b3 = False
            end_of_loop = False
            TEXT_INPUT.clear()
            GUESSED.clear()
            BUTTONS.clear()
            savescore = f"{player_name} {highScore}"
            if (highScore < points):
                highScore = points
            with open("score.txt", "w") as f:
                f.write(str(savescore))
            for ind, box in enumerate(BOXES):
                letter = chr(A + ind)
                button = ([box, letter])
                BUTTONS.append(button)
            gameOver()

def gameOver():
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        gameoverimg = pygame.image.load("gameover.jpg")
        screen.blit(gameoverimg, (260, 50))

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(295, 150, 130, 45)
        button_2 = pygame.Rect(475, 150, 130, 45)
        if button_1.collidepoint((mx, my)):
            if click:
                category()
        if button_2.collidepoint((mx, my)):
            if click:
                quit()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        status_text('Play again', font, (255, 255, 255), screen, 310, 165)
        status_text('Quit', font, (255, 255, 255), screen, 490, 165)

        pygame.display.update()

mainmenu()