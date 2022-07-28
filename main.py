from queue import PriorityQueue
from tkinter.font import names
from ast import If
from lib2to3.pgen2.token import MINEQUAL
import sys
from heapq import heapify,heappop,heappush

from certifi import where
import pygame,random,time
pygame.init()0
wrong_image = pygame.image.load(r'E:\dsaproject\sold.png')
old_image=pygame.image.load(r'E:\dsaproject\why.png')
old_image= pygame.transform.scale(old_image, (500,350))

wrong_image = pygame.transform.scale(wrong_image, (25,25))

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 38)
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    global text_ans
                    text_ans=self.text
                    if(self.text!=""):
                        #print(self.text)
                        return
                    
                    self.text = ''
                    
                    #print (a)
                    #pygame.quit()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class button():
    def __init__(self, color, x,y,width,height, text=''):
        global w
        w=width
        global h
        h=height
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            #pygame.draw.rect(win, outline, (self.x,self.y,self.width,self.height),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsansms', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
                
        return False
def textwrite(you_said,cl,f_size,x_co,y_co):
    font = pygame.font.Font('freesansbold.ttf', f_size) 
    texti = font.render(you_said, True, cl) 
    textRect = texti.get_rect()  
    textRect.center = (x_co,y_co) 
    win.blit(texti, textRect) 
"""
# This is used for creating a class called node. this is what defines what the Linked list is made up of.
class node:
    def __init__ (self, travel_points, username, next=None):
        self.travel_points = travel_points
        self.username = username
        self.next = next



# This is the Linked List class. It contains all the useful functions required for the app.
class linkedlist:
    def __init__ (self):
        self.head = None

    def insert(self, travel_points, username):            
        newnode=node(travel_points, username)
        if(self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        else:
            self.head = newnode

    def checking(self):
        for i in range (len(names)):
            current = self.head
            while current:
                if names[i] == current.username:
                    L2.insert (current.travel_points, names[i])
                    current = current.next
                    if(i<=4):
                        i+=1
                    break
                elif (current.username != names):
                    current = current.next

# Linked List 1 is User database and 2 is the users booking the tickets.
L1 = linkedlist()
L2 = linkedlist()
"""
names = ['Shubham', 'Josh', 'John']
points = [1500, 452, 278, 4113, 100]
name_database = ["Shubham", "Shrey", "Sara", "Josh", "Emily"]
"""
# This sorts the array that contains the points of all the travelers in database into ascending order.
for i in range(0, len(points)):
    for j in range (i+1, len(points)):
        if (points[i] < points[j]):
            temp = points[i]
            points[i] = points[j]
            points[j] = temp

for i in range (0, len(name_database)):
    L1.insert(points[i], name_database[i])
L1.checking()
"""
#sleep(10)
#Initialization

user_list=[[23,'m','suresh',0,''],[43,'f','tanishka',0,''],[12,'m','mukesh',0,''],[78,'m','satish',0,''],[32,'f','surbha',0,''],[25,'f','tanu',0,''],[45,'m','munna',0,'']]
q=[]
q1=[]
s=0

run=True
input_box1 = InputBox(200, 275, 200, 50)
input_box2 = InputBox(200, 375, 200, 50)
input_box3 = InputBox(400, 400, 200, 50)
input_box4 = InputBox(400, 400, 200, 50)
input_box5 = InputBox(400, 600, 200, 50)
input_box6 = InputBox(400, 400, 200, 50)


text_ans=""

#Input Boxes for Passengers
input_box_pass_1_name = InputBox(100, 150, 900, 50)
input_box_pass_1_age = InputBox(200, 350, 250, 50)
input_box_pass_1_gender = InputBox(300,550, 200, 50)


pass_case=False
saved_users=['a','b','c']
saved_pass=['123','123','123']
username_by_user=[]
password_by_user=[]


a=True
b=True
c=True
d=True
e=True
f=True
g=True
h=True
p=True
qo=True
x=True
y=True
num=0

ticket_all_user=[]
while run==True:
    win=pygame.display.set_mode((1100,700))
    win.fill((255,255,255))
    while a==True:
        
        textwrite(" | The RailWay Ticket Management System |  ",(0, 0, 128),45,550,100)
        textwrite(" | An initiative by Shrey, Shubham and Hisham |  ",(0, 0, 128),35,550,180)
        win.blit((old_image), (50,300))
        pygame.display.update()
        
        time.sleep(5)
        a=False

    #time.sle
    #Number of persons
    while y==True:
        text_ans=""
        win.fill((255,200,255))
        textwrite(" | The RailWay Ticket Management System |  ",(0, 0, 128),45,550,100)
        textwrite(" Destination  ",(0, 0, 128),45,550,200)
        for event in pygame.event.get():
                        
            input_box6.handle_event(event)
        dest=text_ans
        input_box6.draw(win)
        pygame.display.update()
            
        if(len(text_ans)>0):
            y=False

    while b==True:
        text_ans="0"
        win.fill((255,180,255))
        textwrite(" | The RailWay Ticket Management System |  ",(0, 0, 128),45,550,100)
        textwrite("Number of Passengers : ",(0, 0, 128),30,500,300)
        for event in pygame.event.get():
                        
            input_box3.handle_event(event)
        
        input_box3.draw(win)
        pygame.display.flip()
        
        pygame.display.update()
        
        if(int(text_ans)>0):
            
            number_of_passengers=int(text_ans)
            num=1
            b=False

    #print(number_of_passengers)
    
    while c==True:
        win.fill((255,180,255))
        for event in pygame.event.get():
                        
            input_box_pass_1_name.handle_event(event)
            
        textwrite(" NAMES  ",(0, 0, 128),30,600,50)
        #textwrite(" AGES : ",(0, 0, 128),30,600,250)
        #textwrite(" GENDER : ",(0, 0, 128),30,600,500)

        input_box_pass_1_name.draw(win)
        pygame.display.flip()
        passenger_name_list=text_ans.split(",")
        
        pygame.display.update()
        #textwrite(passenger_name_list[1],(0, 0, 128),30,800,500)
        if(len(passenger_name_list)==number_of_passengers):
            print(passenger_name_list)
            c=False
    text_ans=""
    while d==True:
        win.fill((255,180,255))
        for event in pygame.event.get():
                        
            input_box_pass_1_age.handle_event(event)
        #pygame.display.update()
        textwrite(" NAMES  ",(0, 0, 128),30,600,50)
        j=100
        for i in passenger_name_list:

            textwrite(str(i),(0, 0, 128),30,100+j,140)
            j+=200
        textwrite(" AGES : ",(0, 0, 128),30,600,250)
        #textwrite(" GENDER : ",(0, 0, 128),30,600,500)

        input_box_pass_1_age.draw(win)
        pygame.display.flip()
        passenger_age_list=text_ans.split(",")
        
        pygame.display.update()
        #textwrite(passenger_name_list[1],(0, 0, 128),30,800,500)
        if(len(passenger_age_list)==number_of_passengers):
            print(passenger_age_list)
            d=False
    text_ans=""
    while e==True:
        win.fill((255,180,255))
        for event in pygame.event.get():
                        
            input_box_pass_1_gender.handle_event(event)
            
        textwrite(" NAMES  ",(0, 0, 128),30,600,50)
        j=100
        for i in passenger_name_list:


            textwrite(str(i),(0, 0, 128),30,100+j,140)
            j+=200
        j=140
        textwrite(" AGES : ",(0, 0, 128),30,600,250)
        for i in passenger_age_list:

            textwrite(str(i),(0, 0, 128),30,200+j,290)
            j+=100

        textwrite(" GENDER : ",(0, 0, 128),30,600,500)

        input_box_pass_1_gender.draw(win)
        passenger_gender_list=text_ans.split(",")
        #pygame.display.flip()
        pygame.display.update()
        #textwrite(passenger_name_list[1],(0, 0, 128),30,800,500)
        if(len(passenger_gender_list)==number_of_passengers):
            print(passenger_gender_list)
            e=False

    #user_list=[[23,'male','suresh',0],[43,'female','tanishka',0],[12,'male','mukesh',0],[78,'male','satish',0],
    # [32,'female','surbha',0],[25,'female','tanu',0]]
    new_passenger_list=[]
    for i in range(0,len(passenger_name_list)):
        new_passenger_list.append([int(passenger_age_list[i]),passenger_gender_list[i],passenger_name_list[i],0,''])
        user_list.append([int(passenger_age_list[i]),passenger_gender_list[i],passenger_name_list[i],0,''])
    seat_image = pygame.image.load(r'E:\dsaproject\ST.jpg')
    seat_image = pygame.transform.scale(seat_image, (900,500))
    #input_box1 = InputBox(500, 400, 250, 40)
    #input_box1.draw(win)
    #pygame.display.flip()
    
    x=180
    y=110
    if(num==1):
        #
        q2=[]
        # print(user_list)
        for i in user_list:
            if(i[0]>=69):
                q1.append(i)
            elif(i[1]=='f'):
                q2.append(i)
            else:
                q.append(i)
        prq=q1+q2+q
        #print(q) 
        print("Priority Queue : ",prq)


        #Seat Allotment
        ub=[3,6,11,14]
        mb=[2,5,10,13]
        lb=[1,4,9,12]
        slb=[7,15]
        sub=[8,16]
        alert="No"
        alerti="No"
        for i in prq:
            #Senior Citizen Person
            if(i[0]>=69 and (len(slb)!=0 or len(lb)!=0)):
                
                if(len(lb)!=0):
                    i[3]=lb[0]
                    i[4]="Lower Birth"
                    lb=lb[::-1]
                    hu=lb.pop()
                    lb=lb[::-1]
                elif(len(slb)!=0):
                    i[3]=slb[0]
                    i[4]="Side Lower Birth"
                    slb=slb[::-1]
                    hu=slb.pop()
                    slb=slb[::-1]
            
            elif(i[1]=='f' and  (len(slb)!=0 or   len(sub)!=0)):
                
                if(len(sub)!=0):

                    i[3]=sub[0]
                    i[4]="Side Upper Birth"
                    sub=sub[::-1]
                    hu=sub.pop()
                    sub=sub[::-1]

                elif(len(slb)!=0):
                    i[3]=slb[0]
                    i[4]="Side Lower Birth"
                    slb=slb[::-1]
                    hu=slb.pop()
                    slb=slb[::-1]
            else:
                if(len(slb)!=0):
                    i[4]="Side Lower Birth"
                    i[3]=slb[0]
                    slb=slb[::-1]
                    hu=slb.pop()
                    slb=slb[::-1]
                elif(len(lb)!=0):
                    i[4]="Lower Birth"
                    i[3]=lb[0]
                    lb=lb[::-1]
                    hu=lb.pop()
                    lb=lb[::-1]
                elif(len(sub)!=0):
                    i[4]="Side Upper Birth"
                    i[3]=sub[0]
                    sub=sub[::-1]
                    hu=sub.pop()
                    sub=sub[::-1]
                elif(len(ub)!=0):
                    i[4]="Upper Birth"
                    i[3]=ub[0]
                    ub=ub[::-1]
                    hu=ub.pop()
                    ub=ub[::-1]
                elif(len(mb)!=0):
                    i[4]="Middle Birth"
                    i[3]=mb[0]
                    mb=mb[::-1]
                    hu=mb.pop()
                    mb=mb[::-1]
        print(prq)       
        print("Seat Allotment : " )
        for i in range(1,len(prq)):
            
            for j in range(0,len(prq)):
                if(prq[j][3]==i):
                    print(prq[j])
    #######


    ####
    # Coupons define
    wy=[['1','Get upto 20% Off the total bill'],['2','Get 1 free meal on your travel'],['3','20% Off on your hotel booking'],['4','Flat 50 RS. off'],['5','30% discount on select restaurants']]
    win.fill((255,255,255))
    cp1=button((0,255,0),400,100,400,50,wy[0][1])
    pygame.display.update()

    cp2=button((0,255,0),400,200,400,50,wy[1][1])
    
    cp3=button((0,255,0),400,300,400,50,wy[2][1])
    pygame.display.update()
    cp4=button((0,255,0),400,400,400,50,wy[3][1])
    pygame.display.update()
    cp5=button((0,255,0),400,500,400,50,wy[4][1])
  
    pygame.display.update()
    #cp6=button((0,255,0),400,500,400,50,wy[4][1])
    
    #pygame.display.update()
    button_list=[cp1,cp2,cp3,cp4,cp5]
    per_button=True


    bonus_list=[]
    for i in passenger_name_list:

        if(i in name_database):
            bonus_list.append(i)
    
    
    input_box_bonus_1 = InputBox(700, 570, 50, 50)
    input_box_bonus_2 = InputBox(700, 570, 50, 50)
    input_box_bonus_3 = InputBox(700, 570, 50, 50)
    input_box_bonus_4 = InputBox(700, 570, 50, 50)
    input_box_bonus_5 = InputBox(700, 570, 50, 50)
    input_box_bonus_6 = InputBox(700, 570, 50, 50)



    bonus_input_box_list=[input_box_bonus_1,input_box_bonus_2,input_box_bonus_3,input_box_bonus_4,input_box_bonus_5]
    bonus_selected=[]
    out_coupon=[]
    while(f==True):
        win.fill((255,255,255))
        l=5
        loo=5
        for i in range(0,len(bonus_list)):
            win.fill((255,255,255))
            g=True
            
            for j in range(0,l):
                
                if((j+1) not in out_coupon):
                    print(l+1)
                    button_list[j].draw(win,(0,0,0))
                    pygame.display.update()
                else:
                    continue

            for k in bonus_list:
                textwrite("Which Coupon , " +bonus_list[i]+" :",(0, 0, 128),30,500,600)
                text_ans=""
                
                while g==True:
                    for event in pygame.event.get():
                                
                        bonus_input_box_list[i].handle_event(event)
                    #win.fill((255,255,255))
                    pygame.display.update()
                    bonus_input_box_list[i].draw(win)


                    #pygame.display.flip()
                    pygame.display.update()
                    if(len(text_ans)>0):
                        for uy in range(0,loo-1):
                            print(wy)
                            if(wy[uy][0]==text_ans):
                                print(loo)
                                print(wy)
                                out_coupon.append(int(text_ans))
                                print(out_coupon)
                                bonus_selected.append([bonus_list[i],wy[uy][0],wy[uy][1]])
                                loo-=1
                                del wy[uy]
                                pygame.display.update()
                                g=False
                                
            print(bonus_selected)                   
        f=False

    o=[]
    win.fill((255,255,255))
    while p==True:
        
        for i in range(0,number_of_passengers):
            o=[]
                
            o.append(passenger_name_list[i])
            o.append(passenger_age_list[i])
            o.append(passenger_gender_list[i])

            for j in prq:
                if(j[2]==o[0]):
                    o.append(j[3])
                    o.append(j[4])
            
            ticket_all_user.append(o)
        textwrite("Congratulations ! ",(0, 0, 128),50,500,100)
        textwrite("Tickets Booked Succesfully !" ,(0, 0, 128),50,500,200)
        pygame.display.update()
        ko=100
        for i in ticket_all_user:
            textwrite(i[0]+"  |  "+str(i[1])+" | "+str(i[2])+" | "+str(i[3])+" | "+i[4],(0, 0, 128),35,400,300+ko)
            ko+=100
        
            pygame.display.update()
        nxtButton=button((0,255,0),900,550,100,50,'Blue Print')
        
        nxtButton.draw(win,(0,0,0))
        pygame.display.update()
        nxtpage=True
        while(nxtpage==True):
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                if 1000 > pos[0] > 900 and 550+50 > pos[1] > 550:
                    if event.type==pygame.MOUSEBUTTONDOWN:  
                    
                        nxtpage=False
                        break
        
        #time.sleep(3)
        pygame.display.update()
        qo=True
        p=False
                
            
    while qo==True:

        win.fill((255,255,255))
        win.blit(seat_image, (50,50))
        ko=50
        for i in ticket_all_user:
            textwrite(i[0]+"  |  "+str(i[1])+" | "+str(i[2])+" | "+str(i[3])+" | "+i[4],(0, 0, 128),20,300,500+ko)
            ko+=50
        textwrite(" Happy Journey , Destination :  "+dest,(0, 0, 128),50,500,650)
        pygame.display.update()
        
        
        time.sleep(100)
        

        
            
        





