#import pyserial
import pygame
from menu import Button, Text
pygame.init()

#Game Window
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED) # Allows to Maximize or Minimize
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Ocarina For Rehabilitation")


#Create buttons for menu
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 50
BTN_COLOR = pygame.Color('tomato')
BTN_ONCLICK_COLOR = pygame.Color('tomato3')
Connect_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*4 ), BUTTON_WIDTH, BUTTON_HEIGHT)
Calibration_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*3 ), BUTTON_WIDTH, BUTTON_HEIGHT)
StartTherapy_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*2 ), BUTTON_WIDTH, BUTTON_HEIGHT)
FreePlay_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*1 ), BUTTON_WIDTH, BUTTON_HEIGHT)
Connect_btn.draw(screen, BTN_COLOR)
Calibration_btn.draw(screen, BTN_COLOR)
StartTherapy_btn.draw(screen, BTN_COLOR)
FreePlay_btn.draw(screen, BTN_COLOR)
Connect_btn.text("Connect Device", screen, 35)
Calibration_btn.text("Calibration", screen, 35)
StartTherapy_btn.text("Therapy Start",screen, 35)
FreePlay_btn.text("Free Play", screen, 35)


#Create Game Title
TITLE_WIDTH = SCREEN_WIDTH
TITLE_HEIGHT = (SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*4 ))
TITLE_COLOR = pygame.Color('tomato')
Title_game = Text((SCREEN_WIDTH - TITLE_WIDTH)/2, 0, TITLE_WIDTH, TITLE_HEIGHT)
Title_game.draw(screen)
Title_game.text("Brief Hero", screen, TITLE_COLOR , 150)

#Game Loop
run = True
while run:

    
    
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LCTRL] == True and key[pygame.K_m] == True :
        pygame.display.toggle_fullscreen() # The command "Ctrl + M" allows to toggle the window to fullscreen or not

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Events for Click on Mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Event for Connect Button
            if Connect_btn.rect.collidepoint(event.pos):
                Connect_btn.draw(screen, BTN_ONCLICK_COLOR)
                Connect_btn.text("Connect Device", screen, 35)
                Connect_btn.active = not Connect_btn.active
            else:
                Connect_btn.active = False


            # Event for Calibration Button
            if Calibration_btn.rect.collidepoint(event.pos):
                Calibration_btn.draw(screen, BTN_ONCLICK_COLOR)
                Calibration_btn.text("Calibration", screen, 35)
                Calibration_btn.active = not Calibration_btn.active
            else:
                Calibration_btn.active = False


            # Event for Therapy Start Button
            if StartTherapy_btn.rect.collidepoint(event.pos):
                StartTherapy_btn.draw(screen, BTN_ONCLICK_COLOR)
                StartTherapy_btn.text("Therapy Start", screen, 35)
                StartTherapy_btn.active = not StartTherapy_btn.active
            else:
                StartTherapy_btn.active = False


            # Event for Free Play Button
            if FreePlay_btn.rect.collidepoint(event.pos):
                FreePlay_btn.draw(screen, BTN_ONCLICK_COLOR)
                FreePlay_btn.text("Free Play", screen, 35)
                FreePlay_btn.active = not FreePlay_btn.active
            else:
                FreePlay_btn.active = False

        # Events for Click off Mouse
        elif event.type == pygame.MOUSEBUTTONUP:

            # Event for Connect Button
            if Connect_btn.rect.collidepoint(event.pos):
                Connect_btn.draw(screen, BTN_COLOR)
                Connect_btn.text("Connect Device", screen, 35)
                Connect_btn.active = False
            else:
                Connect_btn.draw(screen, BTN_COLOR)
                Connect_btn.text("Connect Device", screen, 35)
                Connect_btn.active = False


            # Event for Calibration Button
            if Calibration_btn.rect.collidepoint(event.pos):
                Calibration_btn.draw(screen, BTN_COLOR)
                Calibration_btn.text("Calibration", screen, 35)
                Calibration_btn.active = False
            else:
                Calibration_btn.draw(screen, BTN_COLOR)
                Calibration_btn.text("Calibration", screen, 35)
                Calibration_btn.active = False


            # Event for Therapy Start Button
            if StartTherapy_btn.rect.collidepoint(event.pos):
                StartTherapy_btn.draw(screen, BTN_COLOR)
                StartTherapy_btn.text("Therapy Start", screen, 35)
                StartTherapy_btn.active = False
            else:
                StartTherapy_btn.draw(screen, BTN_COLOR)
                StartTherapy_btn.text("Therapy Start", screen, 35)
                StartTherapy_btn.active = False  


            # Event for Free Play Button
            if FreePlay_btn.rect.collidepoint(event.pos):
                FreePlay_btn.draw(screen, BTN_COLOR)
                FreePlay_btn.text("Free Play", screen, 35)
                FreePlay_btn.active = False
            else:
                FreePlay_btn.draw(screen, BTN_COLOR)
                FreePlay_btn.text("Free Play", screen, 35)
                FreePlay_btn.active = False            

        #if event.type == pygame.WINDOWMAXIMIZED:
        #    screen.blit(screen, screen.get_rect().center)

    pygame.display.update()
        


#Finish game
pygame.quit()
