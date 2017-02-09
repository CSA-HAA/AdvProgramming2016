"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>

Creates PyGame with a Quit button, a Save button, and a cat that will move around.
When someone clicks on the screen, there should is a sound effect, the object should move to where they clicked unless they click the save/quit buttons.
When they do click Quit/Save, it should change the button in some way so that it looks like it was clicked.
Clicking on quit closes the program, clicking on save saves the last location of the object to a .txt file called location.

Version .4
Author: Hamzah Ahmed
"""

import pygame, sys, time
from pygame.locals import *

# MAKE IT SAVE AND ADD SOUND EFFECT

pygame.init()

FPS = 50  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)

# Loads images, sounds and sets default place
catImg = pygame.image.load('cat.png')
catx = 10
caty = 145
direction = 'right'
mousex = 0
mousey = 0
exitImg = pygame.image.load('exit.png')
exitx = 10
exity = 10
clickedExit = pygame.image.load('clickedexit.png')
saveImg = pygame.image.load('save.png')
savex = 355
savey = 10
clickedSave = pygame.image.load('clickedsave.png')
loadImg = pygame.image.load('load.png')
loadx = 185
loady=10
clickedLoad = pygame.image.load('clickedload.png')
soundObj = pygame.mixer.Sound('siren.wav')
#Opens ball image and starts the ball location in ballx and bally
ballImg = pygame.image.load('smallball.png')
ballx = 420
bally = 430

def save(): #Save cat position
    with open("location.txt", "w") as file:
        file.write(str(catx) + "\n" + str(caty) + "\n" + str(ballx) + "\n" +str(bally))

def load(): #Loads cat position
    try:
        with open("location.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ['10\n', '145\n','420\n', '430\n']

def play(): #Plays siren sound
    soundObj.play()
    soundObj.stop()


while True:  # the main game loop
    DISPLAYSURF.fill(WHITE)
    # Adds cat, ball, exit, and save images
    DISPLAYSURF.blit(ballImg, (ballx, bally))
    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(exitImg, (exitx, exity))
    DISPLAYSURF.blit(saveImg, (savex, savey))
    DISPLAYSURF.blit(loadImg, (loadx, loady))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:  # If clicked
            mousex, mousey = event.pos
            if mousex >= 353 and mousey <= 135:  # Saves if clicked after flashing red
                save()
                DISPLAYSURF.blit(clickedSave, (savex, savey))
                pygame.display.update()
                pygame.time.wait(100)
                DISPLAYSURF.blit(saveImg, (savex, savey))
                pygame.display.update()
            elif mousex <= 128 and mousey <= 135:  # Quits game if exit is clicked after flashing red
                DISPLAYSURF.blit(clickedExit, (exitx, exity))
                pygame.display.update()
                pygame.time.wait(100)
                DISPLAYSURF.blit(exitImg, (exitx, exity))
                pygame.display.update()
                pygame.quit()
                sys.exit()
            elif mousex>= 185 and mousex<=313 and mousey <= 135: #Loads saved position and moves cat to it
                DISPLAYSURF.blit(clickedLoad, (loadx, loady))
                pygame.display.update()
                pygame.time.wait(100)
                DISPLAYSURF.blit(loadImg, (loadx, loady))
                pygame.display.update()
                position = load() #pulls position
                catx = int(position[0]) #sets position to x and y
                caty = int(position[1])
                ballx = int(position[2])
                bally = int(position[3])

                pygame.display.update()
                # key movements

            else:
                # Changes cats position and make sure it doesn't go anywhere it shouldn't
                catx, caty = event.pos
                catx -= 50
                caty -= 30
                if catx >= 370:
                    catx = 370
                elif catx < 10:
                    catx = 10
                if caty >= 410:
                    caty = 410
                elif caty < 145:
                    caty = 145
                play()
        elif event.type == KEYUP: #These events take place when a button is pressed
            if event.key in (K_LEFT, K_a):  #CAT LEFT
                catx-=20
                play()
            elif event.key in (K_UP, K_w):  #CAT UP
                caty-=20
                play()
            elif event.key in (K_DOWN, K_s):  #CAT DOWN
                caty+=20
                play()
            elif event.key in (K_RIGHT, K_d):  #CAT RIGHT
                catx+=20
                play()
            #Stops from leacing window boundaries
            if catx >= 370:
                catx = 370
            elif catx < 10:
                catx = 10
            if caty >= 410:
                caty = 410
            elif caty < 145:
                caty = 145

            if event.key in (K_LEFT, K_j):  #BALL LEFT
                ballx-=20
                play()
            elif event.key in (K_UP, K_i):  #BALL UP
                bally-=20
                play()
            elif event.key in (K_DOWN, K_k):  #BALL DOWN
                bally+=20
                play()
            elif event.key in (K_RIGHT, K_l):  #BALL RIGHT
                ballx+=20
                play()
            #Stops from leacing window boundaries
            if ballx >= 420:
                ballx = 420
            elif ballx < 10:
                ballx = 10
            if bally >= 430:
                bally = 430
            elif bally < 145:
                bally = 145

    pygame.display.update()
    fpsClock.tick(FPS)
