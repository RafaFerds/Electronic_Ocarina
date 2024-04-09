import serial
import pygame
from instrument import Ocarina
#from pydub import AudioSegment
from menu import Button, Text, IconButton, CicleButton, Mixer
from pydub.playback import play
#AudioSegment.converter = "C:/Users/Casa1/AppData/Local/ffmpegio/ffmpeg-downloader/ffmpeg/bin/ffmpeg.exe"
#AudioSegment.ffmpeg = "C:/Users/Casa1/AppData/Local/ffmpegio/ffmpeg-downloader/ffmpeg/bin/ffmpeg.exe"

#import ffmpeg_downloader as ffdl

#file = "sounds/Zeldarian/C_root/G#.mp3"
#sound = AudioSegment.from_mp3(file)

#sound_beg = sound[:400]
#sound_end = sound[-400:]
#sound_mid = sound[200:800]
#sound_mid_reverse = sound_mid.reverse()

#sound_f = sound[:400] 


#sound_final = sound_mid * 60
#cont = 0

#sound_f = sound_beg
#sound_f = sound_f.append(sound_mid, crossfade = 100)
#for n in range(0,300):
    #sound_f = sound_f.append(sound_mid_reverse,crossfade = 5)
    #sound_f = sound_f.append(sound_mid,crossfade = 16)
    #sound_f.export("C:/Users/Casa1/Desktop/Sounds/"+str(cont) +" - A8.mp3", format = "mp3")
    #sound_f += sound_mid
#sound_f.append(sound_end, crossfade = 7)
#sound_f = sound_f.fade_in(2000).fade_out(3000)
#cont+=1
#sound_f.export("C:/Users/Casa1/Desktop/Sounds/"+str(cont) +" - G#.mp3", format = "mp3")
#+ sound[401:600] *60 + sound[-400:]

#sound_f.export("C:/Users/Casa1/Desktop/Sounds/G#.mp3", format = "mp3")
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

#Ocarina init
Ocarina1 = Ocarina()

#Create buttons 
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 50
BTN_COLOR = pygame.Color('tomato')
BTN_ONCLICK_COLOR = pygame.Color('tomato3')
LIST_WIDTH = SCREEN_WIDTH*0.4
SENSOR_HEIGHT = SCREEN_HEIGHT*0.075
SENSOR_WIDTH = SCREEN_WIDTH*0.1
LIST_HEIGHT = SCREEN_HEIGHT*0.4
POPUP_WIDTH = SCREEN_WIDTH*0.3
POPUP_HEIGHT = SCREEN_WIDTH*0.2

#Create Game Title
TITLE_WIDTH = SCREEN_WIDTH
TITLE_HEIGHT = (SCREEN_HEIGHT-15 - ((BUTTON_HEIGHT+10)*4 ))
TITLE_COLOR = pygame.Color('tomato')
Title_game = Text((SCREEN_WIDTH - TITLE_WIDTH)/2, 0, TITLE_WIDTH, TITLE_HEIGHT)
Title_game.draw(screen)
Title_game.text("Wind Warriors", screen, 150, TITLE_COLOR)


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

# CALIBRATION PAGE
#Description_List =  Text((SCREEN_WIDTH - TITLE_WIDTH)/2, SCREEN_HEIGHT/2 - BUTTON_HEIGHT*2, TITLE_WIDTH, BUTTON_HEIGHT)
StartCalib_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, SCREEN_HEIGHT-15 - (BUTTON_HEIGHT+10) , BUTTON_WIDTH, BUTTON_HEIGHT)
Press_sens = Text((SCREEN_WIDTH - SENSOR_WIDTH)/2-SENSOR_WIDTH, SCREEN_HEIGHT-150 - (BUTTON_HEIGHT+ SENSOR_HEIGHT +10), SENSOR_WIDTH, SENSOR_HEIGHT)
Press_sens_val = Text((SCREEN_WIDTH - SENSOR_WIDTH)/2, SCREEN_HEIGHT-150 - (BUTTON_HEIGHT+ SENSOR_HEIGHT +10), SENSOR_WIDTH, SENSOR_HEIGHT)
Press_sens_unit = Text((SCREEN_WIDTH - SENSOR_WIDTH)/2+SENSOR_WIDTH, SCREEN_HEIGHT-150 - (BUTTON_HEIGHT+ SENSOR_HEIGHT +10), SENSOR_WIDTH, SENSOR_HEIGHT)
Calib_flag = False
#Refresh_btn = IconButton(SCREEN_WIDTH/2 + LIST_WIDTH/2 + 15, SCREEN_HEIGHT-30 - (BUTTON_HEIGHT+ LIST_HEIGHT +10), 40, 40)
#COM_Devices = []
#Error_msg = Text((SCREEN_WIDTH - POPUP_WIDTH)/2, (SCREEN_HEIGHT - POPUP_HEIGHT)/2, POPUP_WIDTH, POPUP_HEIGHT)
#Error_msg_btn = Button((SCREEN_WIDTH - BUTTON_WIDTH)/2, (SCREEN_HEIGHT)/2 + 50 , BUTTON_WIDTH, BUTTON_HEIGHT)

# FREE PLAY PAGE
FREEPLAY_BUTTON_SIZE = 100
Red_btn = CicleButton(SCREEN_WIDTH*0.35, SCREEN_HEIGHT*0.55, FREEPLAY_BUTTON_SIZE, FREEPLAY_BUTTON_SIZE)
Yellow_btn = CicleButton(SCREEN_WIDTH*0.6, SCREEN_HEIGHT*0.55, FREEPLAY_BUTTON_SIZE, FREEPLAY_BUTTON_SIZE)
Blue_btn = CicleButton(SCREEN_WIDTH*0.35, SCREEN_HEIGHT*0.8, FREEPLAY_BUTTON_SIZE, FREEPLAY_BUTTON_SIZE)
White_btn = CicleButton(SCREEN_WIDTH*0.6, SCREEN_HEIGHT*0.8, FREEPLAY_BUTTON_SIZE, FREEPLAY_BUTTON_SIZE)


# Game sound mixer
FREQUENCY_CHANNEL = 44100
Mixer_game = Mixer()
Mixer_game.mixer.init(FREQUENCY_CHANNEL)
#Sound scale
snd_G = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/G.mp3")
snd_Ab = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/G#.mp3")
snd_A = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/A.mp3")
snd_Bb = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/A#.mp3")
snd_B = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/B.mp3")
snd_C = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/C.mp3")
snd_D = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/D.mp3")
snd_E = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/E.mp3")
snd_F = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/F.mp3")
snd_Gb8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/F#.mp3")
snd_G8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/G8.mp3")
snd_Ab8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/G8#.mp3")
snd_A8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/A8.mp3")
snd_Bb8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/A8#.mp3")
snd_B8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/B8.mp3")
snd_C8 = Mixer_game.mixer.Sound("sounds/Zeldarian/C_root/C8.mp3")

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

#Function for read serial

def read_serial(serial):
    val = serial.readline()
    value = val.decode("utf-8")
    #print(value)
    yellow = int(value[(value.find("AMARELO: ") + 9):(value.find(" - BRANCO: "))])
    white = int(value[(value.find(" - BRANCO: ") + 11):(value.find(" - VERMELHO: "))])
    red = int(value[(value.find(" - VERMELHO: ") + 13):(value.find(" - AZUL: "))])
    blue = int(value[(value.find(" - AZUL: ") + 9):(value.find(" - PRETO: "))])
    black = int(value[(value.find(" - PRETO: ") + 10):(value.find(" - F: "))])
    air_flag = int(value[(value.find(" - F: ") + 6):(value.find(" - PRESSAO: "))])
    press = float(value[(value.find(" - PRESSAO: ") + 12):(value.find(" ."))])
    
    

    #return value
    return yellow, white, red, blue, black, air_flag, press

def read_sens(serial):
    val = serial.readline()
    value = val.decode("utf-8")
    
    if(value.find("- OK")!=-1):
        state = False
        pass
    else:
        state = True
        if(value.find("AMARELO")==-1):
            Ocarina1.calib_press = float(value[(value.find("PRESSAO: ") + 9):(value.find(" ."))])
            
    
    print(value)

    #return value
    return state

#Flag for game pages
page = "Menu"

#Flag for what note is playing
G_Play = False
Ab_Play = False
A_Play = False
Bb_Play = False
B_Play = False
C_Play = False
D_Play = False
E_Play = False
F_Play = False
Gb8_Play = False
G8_Play = False
Ab8_Play = False
A8_Play = False
Bb8_Play = False
B8_Play = False
C8_Play = False
#Flag for buttons
cond_yellow = False
cond_white = False
cond_red = False
cond_blue = False
cond_black = False
cond_air = False

#Game Loop
run = True
while run:
    
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LCTRL] == True and key[pygame.K_m] == True :
        pygame.display.toggle_fullscreen() # The command "Ctrl + M" allows to toggle the window to fullscreen or not
    if page == "Calibration":
        if Calib_flag:
            Calib_flag = read_sens(ser)
            StartCalib_btn.draw(screen, pygame.Color('gray50'))
            StartCalib_btn.text("Start Calibration", screen, 35, pygame.Color('white'))
            StartCalib_btn.active = False
            Press_sens_val.draw(screen, pygame.Color('gray73') )
            Press_sens_val.text(str(Ocarina1.calib_press),screen, 35, pygame.Color('black'))
            if not Calib_flag:
                StartCalib_btn.draw(screen, BTN_COLOR)
                StartCalib_btn.text("Start Calibration", screen, 35)

        

        
        
        

        

    if page == "Free":
        Ocarina1.yellow, Ocarina1.white, Ocarina1.red, Ocarina1.blue, Ocarina1.black, Ocarina1.airf, Ocarina1.press = read_serial(ser)
        
        cond_yellow = key[pygame.K_KP_9] or Ocarina1.yellow
        cond_white = key[pygame.K_KP_3]  or Ocarina1.white
        cond_red = key[pygame.K_KP_7] or Ocarina1.red
        cond_blue = key[pygame.K_KP_1] or Ocarina1.blue
        cond_black = Ocarina1.black
        cond_air = key[pygame.K_KP_0] or Ocarina1.airf


        if cond_blue:
            Blue_btn.draw(screen, pygame.Color('darkblue'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
        else:
            Blue_btn.draw(screen, pygame.Color('blue'),(FREEPLAY_BUTTON_SIZE/2)*0.8)

        if cond_white:
            White_btn.draw(screen, pygame.Color('gray40'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
        else:
            White_btn.draw(screen, pygame.Color('white'),(FREEPLAY_BUTTON_SIZE/2)*0.8)

        if cond_red:
            Red_btn.draw(screen, pygame.Color('darkred'), (FREEPLAY_BUTTON_SIZE/2)*0.8)
        else:
            Red_btn.draw(screen, pygame.Color('red'), (FREEPLAY_BUTTON_SIZE/2)*0.8)
        
        if cond_yellow:
            Yellow_btn.draw(screen, pygame.Color('gold4'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
        else:
            Yellow_btn.draw(screen, pygame.Color('yellow'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
        
        # Command for G
        if (not cond_blue) and (cond_white) and (not cond_red) and (cond_yellow) and  (cond_air):
            if not G_Play:
                snd_G.play(fade_ms=50)
                G_Play=True          
        else:
            snd_G.fadeout(100)
            G_Play=False 

        # Command for Ab or G#
        if (not cond_blue) and (not cond_white) and (cond_red) and (not cond_yellow) and  (cond_air):
            if not Ab_Play:
                snd_Ab.play(fade_ms=50)
                Ab_Play=True      
        else:
            snd_Ab.fadeout(100)
            Ab_Play=False   

        # Command for A
        if (not cond_blue) and (cond_white) and (cond_red) and (not cond_yellow) and  (cond_air):
            if not A_Play:
                snd_A.play(fade_ms=50) 
                A_Play=True           
        else:
            snd_A.fadeout(100)
            A_Play=False  

        # Command for Bb or A#
        if (not cond_blue) and (not cond_white) and (cond_red) and (cond_yellow) and  (cond_air):
            if not Bb_Play:
                snd_Bb.play(fade_ms=50)
                Bb_Play=True           
        else:
            snd_Bb.fadeout(100)
            Bb_Play=False

        # Command for B
        if (not cond_blue) and (cond_white) and (cond_red) and (cond_yellow) and  (cond_air):
            if not B_Play:
                snd_B.play(fade_ms=50)
                B_Play=True            
        else:
            snd_B.fadeout(100) 
            B_Play=False

        # Command for C
        if (cond_blue) and (cond_white) and (cond_red) and (cond_yellow) and  (cond_air):
            if not C_Play:
                snd_C.play(fade_ms=50)
                C_Play=True            
        else:
            snd_C.fadeout(100)
            C_Play=False

        # Command for D
        if (cond_blue) and (cond_white) and (cond_red) and (not cond_yellow) and  (cond_air):
            if not D_Play:
                snd_D.play(fade_ms=50)
                D_Play=True
        else:
            snd_D.fadeout(100)
            D_Play=False
            
        # Command for E
        if (cond_blue) and (not cond_white) and (cond_red) and (cond_yellow) and  (cond_air):
            if not E_Play:
                snd_E.play(fade_ms=50)
                E_Play=True

        else:
            snd_E.fadeout(100)
            E_Play=False

        # Command for F
        if (cond_blue) and (not cond_white) and (cond_red) and (not cond_yellow) and  (cond_air):
            if not F_Play:
                snd_F.play(fade_ms=50)
                F_Play=True         
        else:
            snd_F.fadeout(100)
            F_Play=False

        # Command for Gb8 or F#
        if (cond_blue) and (cond_white) and (not cond_red) and (cond_yellow) and  (cond_air):
            if not Gb8_Play:
                snd_Gb8.play(fade_ms=50)
                Gb8_Play=True         
        else:
            snd_Gb8.fadeout(100)
            Gb8_Play=False

        # Command for G8
        if (cond_blue) and (cond_white) and (not cond_red) and (not cond_yellow) and  (cond_air):
            if not G8_Play:
                snd_G8.play(fade_ms=50)     
                G8_Play=True       
        else:
            snd_G8.fadeout(100)
            G8_Play=False

        # Command for Ab8 or G8#
        if (cond_blue) and (not cond_white) and (not cond_red) and (cond_yellow) and  (cond_air):
            if not Ab8_Play:
                snd_Ab8.play(fade_ms=50)
                Ab8_Play=True           
        else:
            snd_Ab8.fadeout(100)
            Ab8_Play=False 

        # Command for A8
        if (cond_blue) and (not cond_white) and (not cond_red) and (not cond_yellow) and  (cond_air):
            if not A8_Play:
                snd_A8.play(fade_ms=50)
                A8_Play=True            
        else:
            snd_A8.fadeout(100)
            A8_Play=False 


        # Command for Bb8 or A8#
        if (not cond_blue) and (cond_white) and (not cond_red) and (not cond_yellow) and  (cond_air): 
            if not Bb8_Play:
                snd_Bb8.play(fade_ms=50)
                Bb8_Play=True         
        else:
            snd_Bb8.fadeout(100)
            Bb8_Play=False

        # Command for B8
        if (not cond_blue) and (not cond_white) and (not cond_red) and (cond_yellow) and  (cond_air):
            if not B8_Play:
                snd_B8.play(fade_ms=50)
                B8_Play=True            
        else:
            snd_B8.fadeout(100)
            B8_Play=False

        # Command for C8
        if (not cond_blue) and (not cond_white) and (not cond_red) and (not cond_yellow) and  (cond_air):
            if not C8_Play:
                snd_C8.play(fade_ms=50)
                C8_Play=True           
        else:
            snd_C8.fadeout(100)
            C8_Play=False
                
        

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            try:
                ser.close()
            except:
                continue
        # Events for Click on Mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Events for Menu Page
            if page == "Menu":
                # Event for Connect Button
                if Connect_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Connect_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Connect_btn.text("Connect Device", screen, 35)
                    Connect_btn.active = not Connect_btn.active
                else:
                    Connect_btn.active = False


                # Event for Calibration Button
                if Calibration_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Calibration_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Calibration_btn.text("Calibration", screen, 35)
                    Calibration_btn.active = not Calibration_btn.active
                else:
                    Calibration_btn.active = False


                # Event for Therapy Start Button
                if StartTherapy_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    StartTherapy_btn.draw(screen, BTN_ONCLICK_COLOR)
                    StartTherapy_btn.text("Therapy Start", screen, 35)
                    StartTherapy_btn.active = not StartTherapy_btn.active
                else:
                    StartTherapy_btn.active = False


                # Event for Free Play Button
                if FreePlay_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    FreePlay_btn.draw(screen, BTN_ONCLICK_COLOR)
                    FreePlay_btn.text("Free Play", screen, 35)
                    FreePlay_btn.active = not FreePlay_btn.active
                else:
                    FreePlay_btn.active = False

                if Error_msg_btn.rect.collidepoint(event.pos) and Error_msg.active == True:
                    Error_msg_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))
                    Error_msg_btn.active = not Error_msg_btn.active
                else:
                    Error_msg_btn.active = False    

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
                if Back_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Back_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    Back_btn.active = not Back_btn.active
                else:
                    Back_btn.active = False

                if StartCalib_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    if Calib_flag:
                        StartCalib_btn.draw(screen, pygame.Color('gray50'))
                        StartCalib_btn.text("Start Calibration", screen, 35, pygame.Color('white'))
                    else:
                        StartCalib_btn.draw(screen, BTN_ONCLICK_COLOR)
                        StartCalib_btn.text("Start Calibration", screen, 35)
                        StartCalib_btn.active = not StartCalib_btn.active
                else:
                    StartCalib_btn.active = False
                

            # Events for Therapy Page
            elif page == "Therapy":
                if Back_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Back_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    Back_btn.active = not Back_btn.active
                else:
                    Back_btn.active = False

            # Events for Free Play Page
            elif page == "Free":
                if Back_btn.rect.collidepoint(event.pos) and Error_msg.active == False:
                    Back_btn.draw(screen, BTN_ONCLICK_COLOR)
                    Back_btn.icon('images/back_button.png', 37, 35, screen)
                    Back_btn.active = not Back_btn.active
                else:
                    Back_btn.active = False

            else:
                run = False
                
        # Events for Click off Mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            # Events for Menu Page
            if page == "Menu":
                # Event for Connect Button
                if Connect_btn.rect.collidepoint(event.pos) and Connect_btn.active == True and Error_msg.active == False:
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
                if Calibration_btn.rect.collidepoint(event.pos) and Calibration_btn.active == True and Error_msg.active == False:
                    Calibration_btn.draw(screen, BTN_COLOR)
                    Calibration_btn.text("Calibration", screen, 35)
                    Calibration_btn.active = False
                    if Connection:
                        screen.fill((0, 0, 0))
                        Title_game.draw(screen)
                        Title_game.text("Calibration Page", screen, 125, TITLE_COLOR, False)
                        Description_List.draw(screen)
                        Description_List.text("Press the black button of your Ocarina first, then click on the button start", screen, 30, pygame.Color("white"), False)
                        Back_btn.draw(screen, BTN_COLOR)
                        Back_btn.icon('images/back_button.png', 37, 35, screen)
                        Press_sens.draw(screen)
                        Press_sens.text('Pressure: ',screen, 35, TITLE_COLOR)
                        Press_sens_val.draw(screen, pygame.Color('gray73') )
                        Press_sens_val.text(str(Ocarina1.calib_press),screen, 35, pygame.Color('black'))
                        Press_sens_unit.draw(screen)
                        Press_sens_unit.text('mmH2O',screen, 35, TITLE_COLOR)
                        StartCalib_btn.draw(screen, BTN_COLOR)
                        StartCalib_btn.text("Start Calibration", screen, 35)
                        page = "Calibration"
                        break
                    else:
                        Error_msg.draw(screen, pygame.Color('red4') )
                        msg = "Please connect a Device first,\n then try to calibrate."
                        Error_msg.text(msg, screen, 30, pygame.Color('white'), False)
                        Error_msg.active = True
                        Error_msg_btn.draw(screen, BTN_COLOR )
                        Error_msg_btn.text("Connect", screen, 35)
                else:
                    Calibration_btn.draw(screen, BTN_COLOR)
                    Calibration_btn.text("Calibration", screen, 35)
                    Calibration_btn.active = False


                # Event for Therapy Start Button
                if StartTherapy_btn.rect.collidepoint(event.pos) and StartTherapy_btn.active == True and Error_msg.active == False:
                    StartTherapy_btn.draw(screen, BTN_COLOR)
                    StartTherapy_btn.text("Therapy Start", screen, 35)
                    StartTherapy_btn.active = False
                    if Connection:
                        screen.fill((0, 0, 0))
                        Title_game.draw(screen)
                        Title_game.text("Therapy Mode", screen, 125, TITLE_COLOR, False)
                        Description_List.draw(screen)
                        Description_List.text("TODO text here:", screen, 30, pygame.Color("white"), False)
                        Back_btn.draw(screen, BTN_COLOR)
                        Back_btn.icon('images/back_button.png', 37, 35, screen)
                        page = "Therapy"
                        break
                    else:
                        Error_msg.draw(screen, pygame.Color('red4') )
                        msg = "Please connect a Device first,\n then start the therapy."
                        Error_msg.text(msg, screen, 30, pygame.Color('white'), False)
                        Error_msg.active = True
                        Error_msg_btn.draw(screen, BTN_COLOR )
                        Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))
                else:
                    StartTherapy_btn.draw(screen, BTN_COLOR)
                    StartTherapy_btn.text("Therapy Start", screen, 35)
                    StartTherapy_btn.active = False  


                # Event for Free Play Button
                if FreePlay_btn.rect.collidepoint(event.pos) and FreePlay_btn.active == True and Error_msg.active == False:
                    FreePlay_btn.draw(screen, BTN_COLOR)
                    FreePlay_btn.text("Free Play", screen, 35)
                    FreePlay_btn.active = False
                    if Connection:
                        screen.fill((0, 0, 0))
                        Title_game.draw(screen)
                        Title_game.text("Free Play Mode", screen, 125, TITLE_COLOR, False)
                        #Description_List.draw(screen)
                        #Description_List.text("TODO text here:", screen, 30, pygame.Color("white"), False)
                        Back_btn.draw(screen, BTN_COLOR)
                        Back_btn.icon('images/back_button.png', 37, 35, screen)
                        Red_btn.draw(screen, pygame.Color('darkred'), FREEPLAY_BUTTON_SIZE/2)
                        White_btn.draw(screen, pygame.Color('gray40'),FREEPLAY_BUTTON_SIZE/2)
                        Blue_btn.draw(screen, pygame.Color('darkblue'),FREEPLAY_BUTTON_SIZE/2)
                        Yellow_btn.draw(screen, pygame.Color('gold4'),FREEPLAY_BUTTON_SIZE/2)
                        Red_btn.draw(screen, pygame.Color('black'), (FREEPLAY_BUTTON_SIZE/2)*0.85)
                        White_btn.draw(screen, pygame.Color('black'),(FREEPLAY_BUTTON_SIZE/2)*0.85)
                        Blue_btn.draw(screen, pygame.Color('black'),(FREEPLAY_BUTTON_SIZE/2)*0.85)
                        Yellow_btn.draw(screen, pygame.Color('black'),(FREEPLAY_BUTTON_SIZE/2)*0.85)
                        Red_btn.draw(screen, pygame.Color('red'), (FREEPLAY_BUTTON_SIZE/2)*0.8)
                        White_btn.draw(screen, pygame.Color('white'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
                        Blue_btn.draw(screen, pygame.Color('blue'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
                        Yellow_btn.draw(screen, pygame.Color('yellow'),(FREEPLAY_BUTTON_SIZE/2)*0.8)
                        ser.write(bytes(b'DATA'))
                        page = "Free"
                        break
                    else:
                        Error_msg.draw(screen, pygame.Color('red4') )
                        msg = "Please connect a Device first,\n then you can start to play."
                        Error_msg.text(msg, screen, 30, pygame.Color('white'), False)
                        Error_msg.active = True
                        Error_msg_btn.draw(screen, BTN_COLOR )
                        Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))
                else:
                    FreePlay_btn.draw(screen, BTN_COLOR)
                    FreePlay_btn.text("Free Play", screen, 35)
                    FreePlay_btn.active = False


                if Error_msg.active:
                    if Error_msg_btn.rect.collidepoint(event.pos) and  Error_msg_btn.active == True:
                        screen.fill((0,0,0))
                        Connect_btn.draw(screen, BTN_COLOR)
                        Calibration_btn.draw(screen, BTN_COLOR)
                        StartTherapy_btn.draw(screen, BTN_COLOR)
                        FreePlay_btn.draw(screen, BTN_COLOR)
                        Connect_btn.text("Connect Device", screen, 35)
                        Calibration_btn.text("Calibration", screen, 35)
                        StartTherapy_btn.text("Therapy Start",screen, 35)
                        FreePlay_btn.text("Free Play", screen, 35)
                        Title_game.draw(screen)
                        Title_game.text("Breathe Hero", screen, 150, TITLE_COLOR)
                        Author_game.draw(screen)
                        Author_game.text("Dev: " + author, screen, 25, VER_COLOR)
                        Version_game.draw(screen)
                        Version_game.text("Version: " + ver, screen, 25, VER_COLOR)
                        Error_msg.active = False
                        Error_msg_btn.active = False
                    else:
                        Error_msg.draw(screen, pygame.Color('red4') )
                        #msg = "Please connect a Device first,\n then try to calibrate."
                        Error_msg.text(msg, screen, 30, pygame.Color('white'), False)
                        Error_msg.active = True
                        Error_msg_btn.active = False
                        Error_msg_btn.draw(screen, BTN_COLOR )
                        Error_msg_btn.text("OK", screen, 30, pygame.Color('white'))   

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
                    Title_game.text("Breathe Hero", screen, 150, TITLE_COLOR)
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
                                ser.baudrate = 74880
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
                    Title_game.text("Breathe Hero", screen, 150, TITLE_COLOR)
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
                
                if StartCalib_btn.rect.collidepoint(event.pos) and StartCalib_btn.active == True and  Error_msg.active == False:
                    StartCalib_btn.draw(screen, BTN_COLOR)
                    StartCalib_btn.text("Start Calibration", screen, 35)
                    StartCalib_btn.active = False
                    Calib_flag = True
                    ser.write(bytes(b'CAL\n'))
                else:
                    if Calib_flag:
                        StartCalib_btn.draw(screen, pygame.Color('gray50'))
                        StartCalib_btn.text("Start Calibration", screen, 35, pygame.Color('white'))
                    else:
                        StartCalib_btn.draw(screen, BTN_COLOR)
                        StartCalib_btn.text("Start Calibration", screen, 35)
                    StartCalib_btn.active = False


            # Events for Therapy Page
            elif page == "Therapy":
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
                    Title_game.text("Breathe Hero", screen, 150, TITLE_COLOR)
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

            # Events for Free Play Page
            elif page == "Free":
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
                    Title_game.text("Breathe Hero", screen, 150, TITLE_COLOR)
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

            else:
                run = False

                        

        #if event.type == pygame.WINDOWMAXIMIZED:
        #    screen.blit(screen, screen.get_rect().center)

    pygame.display.update()
        


#Finish game
pygame.quit()
