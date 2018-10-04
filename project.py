import pygame
import random
import time
pygame.init()
white=(255,255,255)
black=(0,0,0)
display_width=300
display_height=600
xx=0
yy=0
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game')
clock=pygame.time.Clock()#สร้างวัตถุเพื่อช่วยติดตามเวลา
carImg=pygame.image.load('Untitled.png')
bgImg=pygame.image.load('Bg.jpg')
car_width =40
thingImg=pygame.image.load('Untitled2.png')
thing_width=40
car_height=80
green=(62,255,33)
red=(176,4,4)
bright_green =(127,252,0)
bright_red =(255,0,0)
score =0
life = 3

#-------------------------------------------------------
def bg(bg,xx,yy):
    bg= pygame.image.load("1.jpg")
    gameDisplay.blit(bg, (xx,yy))

#---------------------------------------------------------
def crash(life,score):
    if  life==2:
        message_display('Life = 2')
        time.sleep(2)
        game(life,score)
    elif life==1:
        message_display('Life = 1')
        time.sleep(2)
        game(life,score)
    else:
        message_display('Game Over')
        time.sleep(2)
        life = 3
        score = 0
        game(life,score)
        
    
    
#------------------------------------------------------------
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#-----------------------------------------------------
def message_display(text):

    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
#------------------------------------------------------------    
def my_life(life):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Life: "+str(life), True, black)
    gameDisplay.blit(text,(80,0))        
        
#------------------------------------------------------------
def my_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, black)
    gameDisplay.blit(text,(0,0))
    
#-----------------------------------car control---------------------------------------------
def car(x,y):
    gameDisplay.blit(carImg,(x,y))#.bit ใช้รูปมันเป็นสิ่งเล็กๆน้อยๆ

        
#--------------------------------object------------------
def things(thingx,thingy,thingImg):
    gameDisplay.blit(thingImg,(thingx,thingy))
        
#--------------------------------object------------------
def game(life,score):
        x=(display_width*0.45)
        y=(display_height*0.8)
        gameExit = False
        
        x_change = 0
        car_speed = 0
        thing_startx = random.randrange(0,display_width)
        thing_starty = -600
        thing_speed =10
        thing_height =80 
        thing_width=60
        car_height=80
        
        
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()#exitกากบาท
                                quit()
                ############################
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        x_change = -5
                                elif event.key == pygame.K_RIGHT:
                                        x_change = 5
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                        x_change = 0
                
            
                x += x_change
                
      
                bg(bg,xx,yy)
                things(thing_startx,thing_starty,thingImg)
                thing_starty += thing_speed
                car(x,y)
                my_score(score)
                my_life(life)

##############ส่วนขอบ#######################################
                if x>display_width-car_width or x<0:
                        x_change = 0
                        
                        life -=1
                        if  life==0:
                            gameDisplay.blit(bgImg, (xx,yy))
                            time.sleep(1)
                        crash(life,score)
                        
#--------------------------------object------------------
                if thing_starty > display_height:
                    thing_starty = 0 - thing_height
                    thing_startx = random.randrange(0,display_width)
                    score += 1
                    thing_speed += 1
                    
 #--------------------------------crash------------------
                
            
                if y < thing_starty+thing_height:
                    print('y')
                    
                    if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                        print('x')
                        
                        life -=1
                        if  life==0:
                            gameDisplay.blit(bgImg, (xx,yy))
                            time.sleep(1)
                        crash(life,score)
                
#-------------------------------------------------------------------------------------------------------------------------------------------------
                pygame.display.update()#อัพเดตส่วนของหน้าจอเพื่อแสดงซอฟต์แวร์
                clock.tick(30)#เลขข้างในเป็นจำนวนเฟรม/วินาที
                
#----------------------------------------------------------------------------------------------	

game(life,score)
pygame.quit()#exitกากบาท
quit()
