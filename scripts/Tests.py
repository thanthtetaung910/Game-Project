import pygame,sys,scripts.menu
import mysql.connector
import sqlite3
from pygame.locals import*
from scripts.button import Button
from scripts.inputbox import *


pygame.init()

next1=False
next2=False
next3=False


clock=pygame.time.Clock()
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
COLOR_INACTIVE = pygame.Color('grey')
COLOR_ACTIVE = pygame.Color('black')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font('River Adventurer.ttf', 150)
def get_next(next1,next2,next3):
    return next1,next2,next3
def get_font(size):
    #return pygame.font.Font("font.ttf", size)
    return pygame.font.SysFont('Times New Roman',size)
'''def draw_text(text,font,color,surface,x,y):#menu text
    textobj=font.render(text,1,color) #font.render to create an image (Surface) of the text,then blit this image onto another Surface
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)'''

def login():
    global next1,next2,next3
    
    con=sqlite3.connect("mydatabase.db")
    mycursor=con.cursor()
    
    
    

    mycursor.execute("UPDATE account SET who=0 WHERE id=1")
    mycursor.execute("UPDATE account SET who=0 WHERE id=2")
    mycursor.execute("UPDATE account SET who=0 WHERE id=3")
    con.commit()

    mycursor.execute("SELECT status,name FROM account Where id=1")
    myresult1 = mycursor.fetchone()
    
    mycursor.execute("SELECT status,name FROM account Where id=2")
    myresult2 = mycursor.fetchone()

    mycursor.execute("SELECT status,name FROM account Where id=3")
    myresult3 = mycursor.fetchone()

    if myresult1[0]:
        next1=True
        bt1=myresult1[1]
    else:
        next1=False
        bt1="New Player"
    
    if myresult2[0]:
        next2=True
        bt2=myresult2[1]
    else:
        next2=False  
        bt2="New Player" 
    
    if myresult3[0]:
        next3=True
        bt3=myresult3[1]
    else:
        next3=False
        bt3="New Player"
    
    Running,Pause=0,1

    pygame.font.SysFont('Times New Roman',40)
    
    state=Running
    done=True
    active1=False
    active2=False
    active3=False

    bt1_stat=False
    bt2_stat=False
    bt3_stat=False

    delete1=False
    delete2=False
    delete3=False
    
    bt="New Player"

    delete_img=pygame.image.load('image/bin.png')
    delete_img1=pygame.transform.scale(delete_img,(70,70))
    quit_img = pygame.transform.scale(pygame.image.load('image/powerbutton.png'),(50,50))
    button_img=pygame.image.load('image/Play Rect.png')
    button_img1=pygame.transform.scale(button_img,(200,70))

    button_1=Button(image=button_img1, pos=(250, 750),text_input=bt1, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
    button_2=Button(image=button_img1, pos=(750, 750),text_input=bt2, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
    button_3=Button(image=button_img1, pos=(1250, 750), text_input=bt3, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
        
        
    delete_1=Button(image=delete_img1, pos=(385, 750),text_input="", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
    delete_2=Button(image=delete_img1, pos=(885, 750),text_input="", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
    delete_3=Button(image=delete_img1, pos=(1385, 750),text_input="", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
    
    quit_1=Button(image=quit_img, pos=(screen.get_width()-50, 50),text_input="", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
    
    input_box1=InputBox(570,270,200,50,'')
    input_box2=InputBox(570,270,200,50,'')
    input_box3=InputBox(570,270,200,50,'')
    #inputbox=[input_box1,input_box2,input_box3]
    BG = pygame.image.load("image/menu_bg.jpg")
    BG1=pygame.transform.scale(BG,screen.get_size())

    MENU_TEXT = FONT.render("Artifact Adventure", True, "#DC143C")
    MENU_RECT = MENU_TEXT.get_rect(center=(screen.get_width()/2, 250))
    

    MENU_TEXT1 = FONT.render("Running Fighter", True, "crimson")
    MENU_RECT1 = MENU_TEXT1.get_rect(center=(screen.get_width()/2, 400))
    while done:

        MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(BG1, (0, 0))
        screen.blit(MENU_TEXT,MENU_RECT)
        screen.blit(MENU_TEXT1,MENU_RECT1)
        
        for button in [button_1, button_2, button_3,delete_1, delete_2, delete_3,quit_1]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit() 
            if event.type== MOUSEBUTTONDOWN:
                if input_box1.rect.collidepoint(MOUSE_POS):
                    active1 = not active1
                else:
                    active1 = False
                input_box1.color = COLOR_ACTIVE if active1 else COLOR_INACTIVE
                if input_box2.rect.collidepoint(MOUSE_POS):
                    active2 = not active2
                else:
                    active2 = False
                input_box2.color = COLOR_ACTIVE if active2 else COLOR_INACTIVE
                if input_box3.rect.collidepoint(MOUSE_POS):
                    active3 = not active3
                else:
                    active3 = False
                input_box3.color = COLOR_ACTIVE if active3 else COLOR_INACTIVE
                
            if event.type == pygame.KEYDOWN:
                if active1 and bt1_stat:
                    if event.key == pygame.K_RETURN:
                        #print(self.text)
                        input_box1.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_box1.text = input_box1.text[:-1]
                    else:
                        input_box1.text += event.unicode
                            # Re-render the text.
                    input_box1.txt_surface = get_font(40).render(input_box1.text, True, input_box1.color)
                    
            if event.type == pygame.KEYDOWN:
                if active2 and bt2_stat:
                    if event.key == pygame.K_RETURN:
                        #print(self.text)
                        input_box2.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_box2.text = input_box2.text[:-1]
                    else:
                        input_box2.text += event.unicode
                            # Re-render the text.
                    input_box2.txt_surface = get_font(40).render(input_box2.text, True, input_box2.color)
                
            if event.type == pygame.KEYDOWN:
                if active3 and bt3_stat:
                    if event.key == pygame.K_RETURN:
                                #print(self.text)
                        input_box3.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_box3.text = input_box3.text[:-1]
                    else:
                        input_box3.text += event.unicode
                            # Re-render the text.
                    input_box3.txt_surface = get_font(40).render(input_box3.text, True, input_box3.color)
        
            if state==Running:
                mycursor.execute("SELECT status,name FROM account Where id=1")
                myresult1 = mycursor.fetchone()
                
                
                mycursor.execute("SELECT status,name FROM account Where id=2")
                myresult2 = mycursor.fetchone()

                mycursor.execute("SELECT status,name FROM account Where id=3")
                myresult3 = mycursor.fetchone()

                if myresult1[0]:
                    next1=True
                    bt1=myresult1[1]
                else:
                    next1=False
                    bt1="New Player"
                
                if myresult2[0]:
                    next2=True
                    bt2=myresult2[1]
                else:
                    next2=False  
                    bt2="New Player" 
                
                if myresult3[0]:
                    next3=True
                    bt3=myresult3[1]
                else:
                    next3=False
                    bt3="New Player"
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.checkForInput(MOUSE_POS):
                        if next1:
                            mycursor.execute("UPDATE account SET who=1 WHERE id=1")
                            con.commit()
                            scripts.menu.main_menu()
                            
                        else:
                            state=Pause 
                            bt1_stat=True
                    else:
                        bt1_stat=False
                    
                    if button_2.checkForInput(MOUSE_POS):
                        if next2:
                            mycursor.execute("UPDATE account SET who=1 WHERE id=2")
                            con.commit()
                            scripts.menu.main_menu()
                            
                        else:
                            state=Pause 
                            bt2_stat=True
                    else:
                        bt2_stat=False
                    
                    if button_3.checkForInput(MOUSE_POS):
                        if next3:
                            mycursor.execute("UPDATE account SET who=1 WHERE id=3")
                            con.commit()
                            scripts.menu.main_menu()
                            
                        else:
                            state=Pause 
                            bt3_stat=True 
                    else:
                        bt3_stat=False
                    if next1:
                        if delete_1.checkForInput(MOUSE_POS):
                            state=Pause
                            delete1=True
                            
                    if next2:    
                        if delete_2.checkForInput(MOUSE_POS):
                            state=Pause
                            delete2=True
                    if next3:
                        if delete_3.checkForInput(MOUSE_POS):
                            state=Pause
                            delete3=True
                    if quit_1.checkForInput(MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        
        else:                
            if state==Pause:
                button_img=pygame.image.load('image/Play Rect.png')
                pop_img1=pygame.transform.scale(button_img,(500,300))
                screen.blit(pop_img1,(550,250))
                button_Yes=Button(image=pygame.transform.scale(button_img,(100,70)), pos=(700, 500),text_input="Yes", font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
                button_No=Button(image=pygame.transform.scale(button_img,(100,70)), pos=(900, 500),text_input="No", font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
                if delete1:
                    TEXT = get_font(45).render("Are you sure to delete?", True, "black")
                    RECT = TEXT.get_rect(center=(screen.get_width()/2+40, 350))
                    screen.blit(TEXT,RECT)
                if delete2:
                    TEXT = get_font(45).render("Are you sure to delete?", True, "black")
                    RECT = TEXT.get_rect(center=(screen.get_width()/2+40, 350))
                    screen.blit(TEXT,RECT)
                if delete3:
                    TEXT = get_font(45).render("Are you sure to delete?", True, "black")
                    RECT = TEXT.get_rect(center=(screen.get_width()/2+40, 350))
                    screen.blit(TEXT,RECT)

                for button in [button_Yes, button_No]:
                    button.changeColor(MOUSE_POS)
                    button.update(screen)
                if bt1_stat:
                    
                    input_box1.update()
                    input_box1.draw(screen)
                if bt2_stat:
                    input_box2.update()
                    input_box2.draw(screen)
                if bt3_stat:
                    input_box3.update()
                    input_box3.draw(screen)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_Yes.checkForInput(MOUSE_POS):
                        if delete1:
                            mycursor.execute("UPDATE account SET status=0,name=NULL,level=1,money=0 WHERE id=1")
                            con.commit()
                            button_1=Button(image=button_img1, pos=(250, 750),text_input=bt, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
                            state=Running
                            delete1=False
                        else:    
                            if bt1_stat:
                                button_1=Button(image=button_img1, pos=(250, 750),text_input=input_box1.text, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
                                val1=(input_box1.text,)
                                mycursor.execute("UPDATE account SET name=? WHERE id=1",val1)
                                mycursor.execute("UPDATE account SET status=1 WHERE id=1") 
                                con.commit()
                                state=Running
                                next1=True  
                        if delete2:
                            mycursor.execute("UPDATE account SET status=0,name=NULL,level=1,money=0 WHERE id=2")
                            con.commit()
                            button_2=Button(image=button_img1, pos=(750, 750),text_input=bt, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
    
                            
                            state=Running
                            delete2=False
                        else:    
                            if bt2_stat:
                                button_2=Button(image=button_img1, pos=(750, 750),text_input=input_box2.text, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")                                
                                val2=(input_box2.text,)
                                mycursor.execute("UPDATE account SET name=? WHERE id=2",val2)
                                mycursor.execute("UPDATE account SET status=1 WHERE id=2 ") 
                                con.commit()
                                state=Running
                                next2=True 
                        if delete3:
                            #bt3="New Player"
                            mycursor.execute("UPDATE account SET status=0,name=NULL,level=1,money=0 WHERE id=3")
                            con.commit()
                            button_3=Button(image=button_img1, pos=(1250, 750), text_input=bt, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
                            
                            state=Running
                            delete3=False
                        else:    
                            if bt3_stat:
                                button_3=Button(image=button_img1, pos=(1250, 750), text_input=input_box3.text, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
                                val3=(input_box3.text,)
                                mycursor.execute("UPDATE account SET name=? WHERE id=3",val3)
                                mycursor.execute("UPDATE account SET status=1 WHERE id=3 ") 
                                con.commit()
                                state=Running
                                next3=True    
                        
                    if button_No.checkForInput(MOUSE_POS):
                        state=Running   
                
            pygame.display.flip()#pygame.display.flip() fully update existing screen 
            clock.tick(60)            
if __name__ =='__main__':
    login()