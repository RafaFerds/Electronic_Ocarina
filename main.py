import serial
import pygame
from menu import Button, Text, IconButton
from serial_connect import SerialCOM
pygame.init()

#info
ver = "0.1"
author = "Rafael Santos"


#Game Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED) # Allows to Maximize or Minimize
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Ocarina For Rehabilitation")

#List COM Devices
ser = serial.Serial()
Connection = False
COM_list = SerialCOM()


#Create buttons 
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 50
BTN_COLOR = pygame.Color('tomato')
BTN_ONCLICK_COLOR = pygame.Color('tomato3')
LIST_WIDTH = SCREEN_WIDTH*0.4
LIST_HEIGHT = SCREEN_HEIGHT*0.4
POPUP_WIDTH = SCREEN_WIDTH*0.3
POPUP_HEIGHT = SCREEN_WIDTH*0.2

#Create Game Title
TITLE_WIDTH = SCREEN_WIDTH
TITLE_HEIGHT = (SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*4 ))
TITLE_COLOR = pygame.Color('tomato')
Title_game = Text((SCREEN_WIDTH - TITLE_WIDTH)/2, 0, TITLE_WIDTH, TITLE_HEIGHT)
Title_game.draw(screen)
Title_game.text("Brief Hero", screen, 150, TITLE_COLOR)


# MENU PAGE
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

# CONNECT PAGE
Back_btn = IconButton(15, 15, 40, 40)
Description_List =  Text((SCREEN_WIDTH - TITLE_WIDTH)/2, SCREEN_HEIGHT/2 - BUTTON_HEIGHT*2, TITLE_WIDTH, BUTTON_HEIGHT)
Connection_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, SCREEN_HEIGHT-15 - (BUTTON_HEIGHT+10) , BUTTON_WIDTH, BUTTON_HEIGHT)
Bg_list = Text((SCREEN_WIDTH - LIST_WIDTH)/2, SCREEN_HEIGHT-30 - (BUTTON_HEIGHT+ LIST_HEIGHT +10), LIST_WIDTH, LIST_HEIGHT)
Refresh_btn = IconButton(SCREEN_WIDTH/2 + LIST_WIDTH/2 + 15, SCREEN_HEIGHT-30 - (BUTTON_HEIGHT+ LIST_HEIGHT +10), 40, 40)
COM_Devices = []
Error_msg = Text((SCREEN_WIDTH - POPUP_WIDTH)/2, (SCREEN_HEIGHT - POPUP_HEIGHT)/2, POPUP_WIDTH, POPUP_HEIGHT)
Error_msg_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, (SCREEN_HEIGHT)/2 + 50 , BUTTON_WIDTH, BUTTON_HEIGHT)



#Create Game Version Info
VER_WIDTH = 200
VER_HEIGHT = 30
VER_COLOR = pygame.Color('tomato')
Version_game = Text(SCREEN_WIDTH - 10 - VER_WIDTH, SCREEN_HEIGHT - 10 - VER_HEIGHT, VER_WIDTH, VER_HEIGHT)
Version_game.draw(screen)
Version_game.text("Version: " + ver, screen, 25, VER_COLOR)
Author_game = Text(10, SCREEN_HEIGHT - 10 - VER_HEIGHT, VER_WIDTH, VER_HEIGHT)
Author_game.draw(screen)
Author_game.text("Dev: " + author, screen, 25, VER_COLOR)



#Flag for game pages
page = "Menu"

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

            # Events for Menu Page
            if page == "Menu":
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

            # Events for Connection Page
            elif page == "Connect":
                if Back_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Back_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    Back_btn.active = not Back_btn.active
                else:
                    Back_btn.active = False


                if Connection_btn.rect.collidepoint(event.pos) and Error_msg.active == False and Connection == False:
                    Connection_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Connection_btn.text("Connect", screen, 35)
                    Connection_btn.active = not Connection_btn.active
                    
                else:
                    Connection_btn.active = False    

                
                if Refresh_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Refresh_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Refresh_btn.icon('images/refresh_button.png', 35, 35, screen)
                    Refresh_btn.active = not Refresh_btn.active
                else:
                    Refresh_btn.active = False

                for n in range(len(COM_Devices)):
                    if COM_Devices[n].rect.collidepoint(event.pos) and Error_msg.active == False and Connection == False:
                        for x in range(len(COM_Devices)):
                            COM_Devices[x].draw(screen, pygame.Color('gray50'))
                            COM_Devices[x].text(str(COM_list.result[x]), screen, 30, pygame.Color("black"))
                            COM_Devices[x].active = False
                        COM_Devices[n].draw(screen, pygame.Color('gray30'))
                        COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("black"))
                        COM_Devices[n].active = True
            
                if Error_msg_btn.rect.collidepoint(event.pos) and Error_msg.active == True:
                    Error_msg_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))
                    Error_msg_btn.active = not Error_msg_btn.active
                else:
                    Error_msg_btn.active = False

            # Events for Calibration Page
            elif page == "Calibration":
                #TO DO, Page for Device Calibration
                True

            # Events for Therapy Page
            elif page == "Therapy":
                #TO DO, Page for Therapy Protocol
                True

            # Events for Free Play Page
            elif page == "Free":
                #TO DO, Page for Free Play the game
                True

            else:
                run = False
                
        # Events for Click off Mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            # Events for Menu Page
            if page == "Menu":
                # Event for Connect Button
                if Connect_btn.rect.collidepoint(event.pos) and Connect_btn.active == True:
                    Connect_btn.draw(screen, BTN_COLOR)
                    Connect_btn.text("Connect Device", screen, 35)
                    Connect_btn.active = False
                    screen.fill((0, 0, 0))
                    Title_game.draw(screen)
                    Title_game.text("Connection Page", screen, 125, TITLE_COLOR, False)
                    Description_List.draw(screen)
                    Description_List.text("Please click on the refresh button and\nselect a COM port to connect:", screen, 30, pygame.Color("white"), False)
                    Back_btn.draw(screen, BTN_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    if Connection:
                        Connection_btn.draw(screen, pygame.Color('gray50'))
                        Connection_btn.text("Connect", screen, 35, pygame.Color('white'))
                    else:             
                        Connection_btn.draw(screen, BTN_COLOR)
                        Connection_btn.text("Connect", screen, 35)
                    Bg_list.draw(screen, pygame.Color('gray73') )
                    Refresh_btn.draw(screen, BTN_COLOR)
                    Refresh_btn.icon('images/refresh_button.png', 35, 35, screen)
                    
                    page = "Connect"
                    break
                else:
                    Connect_btn.draw(screen, BTN_COLOR)
                    Connect_btn.text("Connect Device", screen, 35)
                    Connect_btn.active = False


                # Event for Calibration Button
                if Calibration_btn.rect.collidepoint(event.pos) and Calibration_btn.active == True:
                    Calibration_btn.draw(screen, BTN_COLOR)
                    Calibration_btn.text("Calibration", screen, 35)
                    Calibration_btn.active = False
                else:
                    Calibration_btn.draw(screen, BTN_COLOR)
                    Calibration_btn.text("Calibration", screen, 35)
                    Calibration_btn.active = False


                # Event for Therapy Start Button
                if StartTherapy_btn.rect.collidepoint(event.pos) and StartTherapy_btn.active == True:
                    StartTherapy_btn.draw(screen, BTN_COLOR)
                    StartTherapy_btn.text("Therapy Start", screen, 35)
                    StartTherapy_btn.active = False
                else:
                    StartTherapy_btn.draw(screen, BTN_COLOR)
                    StartTherapy_btn.text("Therapy Start", screen, 35)
                    StartTherapy_btn.active = False  


                # Event for Free Play Button
                if FreePlay_btn.rect.collidepoint(event.pos) and FreePlay_btn.active == True:
                    FreePlay_btn.draw(screen, BTN_COLOR)
                    FreePlay_btn.text("Free Play", screen, 35)
                    FreePlay_btn.active = False
                else:
                    FreePlay_btn.draw(screen, BTN_COLOR)
                    FreePlay_btn.text("Free Play", screen, 35)
                    FreePlay_btn.active = False

            # Events for Connection Page
            elif page == "Connect":
                if Back_btn.rect.collidepoint(event.pos) and Back_btn.active == True and Error_msg.active == False:
                    Back_btn.draw(screen, BTN_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    Back_btn.active = False
                    screen.fill((0, 0, 0))
                    Connect_btn.draw(screen, BTN_COLOR)
                    Calibration_btn.draw(screen, BTN_COLOR)
                    StartTherapy_btn.draw(screen, BTN_COLOR)
                    FreePlay_btn.draw(screen, BTN_COLOR)
                    Connect_btn.text("Connect Device", screen, 35)
                    Calibration_btn.text("Calibration", screen, 35)
                    StartTherapy_btn.text("Therapy Start",screen, 35)
                    FreePlay_btn.text("Free Play", screen, 35)
                    Title_game.draw(screen)
                    Title_game.text("Brief Hero", screen, 150, TITLE_COLOR)
                    Author_game.draw(screen)
                    Author_game.text("Dev: " + author, screen, 25, VER_COLOR)
                    Version_game.draw(screen)
                    Version_game.text("Version: " + ver, screen, 25, VER_COLOR)
                    page = "Menu"
                    break
                else:
                    Back_btn.draw(screen, BTN_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    Back_btn.active = False
                    

                if Connection_btn.rect.collidepoint(event.pos) and  Connection_btn.active == True and Error_msg.active == False:
                    Connection_btn.draw(screen, BTN_COLOR)
                    Connection_btn.text("Connect", screen, 35)
                    Connection_btn.active = False
                    
                    for n in range(len(COM_Devices)):
                        try: 
                            if COM_Devices[n].active:
                                ser.port = str(COM_list.result[n])
                                ser.open()   

                        except:
                            
                            Error_msg.draw(screen, pygame.Color('red4') )
                            msg = "Connection Error,\n please try again or try another port."
                            Error_msg.text(msg, screen, 30, pygame.Color('white'), False)
                            Error_msg.active = True
                            Error_msg_btn.draw(screen, BTN_COLOR )
                            Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))
                        
                            
                                   
                    if ser.port == None:
                        Error_msg.draw(screen, pygame.Color('red4') )
                        msg = "Please select a COM port before\n connection."
                        Error_msg.text(msg, screen, 30, pygame.Color('white'), False)
                        Error_msg.active = True
                        Error_msg_btn.draw(screen, BTN_COLOR )
                        Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))

                    if ser.is_open:
                        Bg_list.draw(screen, pygame.Color('gray73') )
                        COM_Devices.clear()
                        for n in range(len(COM_list.result)):
                            if ser.port == str(COM_list.result[n]):
                                COM_Devices.append(Text((SCREEN_WIDTH - LIST_WIDTH)/2 + 5, SCREEN_HEIGHT-25 - (BUTTON_HEIGHT+ LIST_HEIGHT +10) + ((LIST_HEIGHT*0.14 + 5)*n), LIST_WIDTH-10, LIST_HEIGHT*0.14))
                                COM_Devices[n].draw(screen, pygame.Color('gray50'))
                                COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("green"))
                                Connection = True
                                Connection_btn.draw(screen, pygame.Color('gray50'))
                                Connection_btn.text("Connect", screen, 35, pygame.Color('white'))
                                Connection_btn.active = False
                            else:
                                COM_Devices.append(Text((SCREEN_WIDTH - LIST_WIDTH)/2 + 5, SCREEN_HEIGHT-25 - (BUTTON_HEIGHT+ LIST_HEIGHT +10) + ((LIST_HEIGHT*0.14 + 5)*n), LIST_WIDTH-10, LIST_HEIGHT*0.14))
                                COM_Devices[n].draw(screen, pygame.Color('gray50'))
                                COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("black"))

                else:
                    if Connection:
                        Connection_btn.draw(screen, pygame.Color('gray50'))
                        Connection_btn.text("Connect", screen, 35, pygame.Color('white'))
                    else:             
                        Connection_btn.draw(screen, BTN_COLOR)
                        Connection_btn.text("Connect", screen, 35)

                

                if Refresh_btn.rect.collidepoint(event.pos) and  Refresh_btn.active == True and Error_msg.active == False:
                    Refresh_btn.draw(screen, BTN_COLOR)
                    Refresh_btn.icon('images/refresh_button.png', 35, 35, screen)
                    Refresh_btn.active = False
                    Bg_list.draw(screen, pygame.Color('gray73') )
                    COM_Devices.clear()
                    COM_list.result.append("COM3")
                    for n in range(len(COM_list.result)):
                        if ser.port == str(COM_list.result[n]):
                            COM_Devices.append(Text((SCREEN_WIDTH - LIST_WIDTH)/2 + 5, SCREEN_HEIGHT-25 - (BUTTON_HEIGHT+ LIST_HEIGHT +10) + ((LIST_HEIGHT*0.14 + 5)*n), LIST_WIDTH-10, LIST_HEIGHT*0.14))
                            COM_Devices[n].draw(screen, pygame.Color('gray50'))
                            COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("green"))
                            if Connection:
                                Connection_btn.draw(screen, pygame.Color('gray50'))
                                Connection_btn.text("Connect", screen, 35, pygame.Color('white'))
                            else:             
                                Connection_btn.draw(screen, BTN_COLOR)
                                Connection_btn.text("Connect", screen, 35)
                        else:
                            COM_Devices.append(Text((SCREEN_WIDTH - LIST_WIDTH)/2 + 5, SCREEN_HEIGHT-25 - (BUTTON_HEIGHT+ LIST_HEIGHT +10) + ((LIST_HEIGHT*0.14 + 5)*n), LIST_WIDTH-10, LIST_HEIGHT*0.14))
                            COM_Devices[n].draw(screen, pygame.Color('gray50'))
                            COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("black"))
                else:
                    Refresh_btn.draw(screen, BTN_COLOR)
                    Refresh_btn.icon('images/refresh_button.png', 35, 35, screen)
                    Refresh_btn.active = False


                #OK button event when POPUP
                if Error_msg.active:
                    if Error_msg_btn.rect.collidepoint(event.pos) and  Error_msg_btn.active == True:
                        screen.fill((0,0,0))
                        Title_game.draw(screen)
                        Title_game.text("Connection Page", screen, 125, TITLE_COLOR, False)
                        Description_List.draw(screen)
                        Description_List.text("Please click on the refresh button and\nselect a COM port to connect:", screen, 30, pygame.Color("white"), False)
                        Back_btn.draw(screen, BTN_COLOR)
                        Back_btn.icon('images/back_button.png', 37, 35, screen)
                        Connection_btn.draw(screen, BTN_COLOR)
                        Connection_btn.text("Connect", screen, 35)
                        Bg_list.draw(screen, pygame.Color('gray73') )
                        Refresh_btn.draw(screen, BTN_COLOR)
                        Refresh_btn.icon('images/refresh_button.png', 35, 35, screen)
                        Refresh_btn.active = False
                        Bg_list.draw(screen, pygame.Color('gray73') )
                        COM_Devices.clear()
                        ser.port = None
                        Error_msg.active = False
                        for n in range(len(COM_list.result)):
                            if ser.port == str(COM_list.result[n]):
                                COM_Devices.append(Text((SCREEN_WIDTH - LIST_WIDTH)/2 + 5, SCREEN_HEIGHT-25 - (BUTTON_HEIGHT+ LIST_HEIGHT +10) + ((LIST_HEIGHT*0.14 + 5)*n), LIST_WIDTH-10, LIST_HEIGHT*0.14))
                                COM_Devices[n].draw(screen, pygame.Color('gray50'))
                                COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("green"))
                            else:
                                COM_Devices.append(Text((SCREEN_WIDTH - LIST_WIDTH)/2 + 5, SCREEN_HEIGHT-25 - (BUTTON_HEIGHT+ LIST_HEIGHT +10) + ((LIST_HEIGHT*0.14 + 5)*n), LIST_WIDTH-10, LIST_HEIGHT*0.14))
                                COM_Devices[n].draw(screen, pygame.Color('gray50'))
                                COM_Devices[n].text(str(COM_list.result[n]), screen, 30, pygame.Color("black"))
                    else:
                        Error_msg_btn.active = False  
                        Error_msg_btn.draw(screen, BTN_COLOR )
                        Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))
                        

            # Events for Calibration Page
            elif page == "Calibration":
                #TO DO, Page for Device Calibration
                True

            # Events for Therapy Page
            elif page == "Therapy":
                #TO DO, Page for Therapy Protocol
                True

            # Events for Free Play Page
            elif page == "Free":
                #TO DO, Page for Free Play the game
                True

            else:
                run = False

                        

        #if event.type == pygame.WINDOWMAXIMIZED:
        #    screen.blit(screen, screen.get_rect().center)

    pygame.display.update()
        


#Finish game
pygame.quit()
