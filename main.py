import time
from PIL import Image
from PIL import ImageFilter
from copy import deepcopy
import telebot
bot_token= '1731148597:AAH_FPxXEae5uoWOOKv4by__KtSFBk7FChU'
bot = telebot.TeleBot(bot_token)
def fbetterq(p,x,y):
    # print("rij ")
    cnt=100;
    while(cnt>0):
        q=p
        for i in range(1,x-1):
            #print(i)
            for j in range(1,y-1):
                
                w1=abs(p[i,j][0]-q[i-1,j][0])+abs(p[i,j][1]-q[i-1,j][1])+abs(p[i,j][2]-q[i-1,j][2])
                w2=abs(p[i,j][0]-q[i+1,j][0])+abs(p[i,j][1]-q[i+1,j][1])+abs(p[i,j][2]-q[i+1,j][2])
                w3=abs(p[i,j][0]-q[i,j-1][0])+abs(p[i,j][1]-q[i,j-1][1])+abs(p[i,j][2]-q[i,j-1][2])
                w4=abs(p[i,j][0]-q[i,j+1][0])+abs(p[i,j][1]-q[i,j+1][1])+abs(p[i,j][2]-q[i,j+1][2])
                if (w1<=w2 and w1<=w3 and w1<=w4):
                    p[i,j]=q[i-1,j]
                elif (w2<=w3 and w2<=w4):
                    p[i,j]=q[i+1,j]
                elif (w3<=w4):
                    p[i,j]=q[i,j-1]
                else :
                    p[i,j]=q[i,j+1]
        cnt-=1
    return p

def f_low_qq(p,x,y):
    vis=[[0] * y for i in range(x)]
    cnt=1
    for i in range(y):
        vis[0][i]=1
    for i in range(x):
        vis[i][0]=1
    while(cnt>0):
        q=p
        for i in range(1,x-1):
            for j in range(1,y-1):
                z=0
                z=abs(q[i,j][0]-q[i-1,j][0])+abs(q[i,j][1]-q[i-1,j][1])+abs(q[i,j][2]-q[i-1,j][2])
               # if (z>=100):
                   # print(i,j,z,x,y,q[i,j][0],q[i,j][1])
                    
                
                if (z<15 and vis[i-1][j]==1):
                    vis[i][j]=1
                z=abs(q[i,j][0]-q[i,j-1][0])+abs(q[i,j][1]-q[i,j-1][1])+abs(q[i,j][2]-q[i,j-1][2])
                if (z<15 and vis[i][j-1]==1):
                    vis[i][j]=1
    
        cnt-=1
    q=p
    for i in range(x-2,0,-1):
        for j in range(y-2,0,-1):
            z=0
            z=abs(q[i,j][0]-q[i+1,j][0])+abs(q[i,j][1]-q[i+1,j][1])+abs(q[i,j][2]-q[i+1,j][2])
           # if (z>=100):
               # print(i,j,z,x,y,q[i,j][0],q[i,j][1])
                    
                
            if (z<15 and vis[i+1][j]==1):
                vis[i][j]=1
            z=abs(q[i,j][0]-q[i,j-1][0])+abs(q[i,j][1]-q[i,j+1][1])+abs(q[i,j][2]-q[i,j+1][2])
            if (z<15 and vis[i][j+1]==1):
                vis[i][j]=1
    cnt=1
    while(cnt>0):
        print(cnt)
        for i in range(1,x-1):
            print(i)
           # print(i)
            for j in range(1,y-1):
                if (vis[i][j]==0):
                    continue
                r=p[i,j][0]
                g=p[i,j][1]
                b=p[i,j][2]
                pnt=0
                for ww in range(i-5,i+5):
                    for yy in range(j-5,j+5):
                        if (ww>=0 and ww<x and yy>=0 and yy<y):
                            pnt+=1
                            r+=p[ww,yy][0]
                            g+=p[ww,yy][1]
                            b+=p[ww,yy][2]
                            
                r=r//pnt
                b=b//pnt
                g=g//pnt
                p[i,j]=(r,g,b)
        cnt-=1
        
    return p
def fputbackground(p,w,x,y):
    vis=[[0] * y for i in range(x)]
    cnt=1
    for i in range(y):
        vis[0][i]=1
    for i in range(x):
        vis[i][0]=1
    while(cnt>0):
        q=p
        for i in range(1,x-1):
            for j in range(1,y-1):
                z=0
                z=abs(q[i,j][0]-q[i-1,j][0])+abs(q[i,j][1]-q[i-1,j][1])+abs(q[i,j][2]-q[i-1,j][2])
               # if (z>=100):
                   # print(i,j,z,x,y,q[i,j][0],q[i,j][1])
                    
                
                if (z<15 and vis[i-1][j]==1):
                    vis[i][j]=1
                z=abs(q[i,j][0]-q[i,j-1][0])+abs(q[i,j][1]-q[i,j-1][1])+abs(q[i,j][2]-q[i,j-1][2])
                if (z<15 and vis[i][j-1]==1):
                    vis[i][j]=1
    
        cnt-=1
    q=p
    for i in range(x-2,0,-1):
        for j in range(y-2,0,-1):
            z=0
            z=abs(q[i,j][0]-q[i+1,j][0])+abs(q[i,j][1]-q[i+1,j][1])+abs(q[i,j][2]-q[i+1,j][2])
           # if (z>=100):
               # print(i,j,z,x,y,q[i,j][0],q[i,j][1])
                    
                
            if (z<15 and vis[i+1][j]==1):
                vis[i][j]=1
            z=abs(q[i,j][0]-q[i,j-1][0])+abs(q[i,j][1]-q[i,j+1][1])+abs(q[i,j][2]-q[i,j+1][2])
            if (z<15 and vis[i][j+1]==1):
                vis[i][j]=1
    cnt=1
    print("hey")
    while(cnt>0):
        q=p
        for i in range(1,x-1):
            print(i)
            for j in range(1,y-1):
                if (vis[i][j]==0):
                    continue
                else :
                    p[i,j]=w[i,j]
        cnt-=1
        
    return p
def fportrait(p,w,x,y):
    vis=[[0] * y for i in range(x)]
    for i in range(0,x):

        for j in range(0,y):
          
            if (abs(p[i,j][0]+p[i,j][1]+p[i,j][2]-w[i,j][0]-w[i,j][1]-w[i,j][2])<20):
                vis[i][j]=1
               # print(i,j)
            else :
                vis[i][j]=0
           
    print("hey")
    cnt=1
    while(cnt>0):
        q=p
        for i in range(1,x-1):
            print(i)
            for j in range(1,y-1):
                if (vis[i][j]==0):
                    continue
                else :
                    p[i,j]=(0,0,0)
                    continue
                r=p[i,j][0]
                g=p[i,j][1]
                b=p[i,j][2]
                pnt=0
                for ww in range(i-5,i+5):
                    for yy in range(j-5,j+5):
                        if (ww>=0 and ww<x and yy>=0 and yy<y):
                            pnt+=1
                            r+=p[ww,yy][0]
                            g+=p[ww,yy][1]
                            b+=p[ww,yy][2]
                                
                r=r//pnt
                b=b//pnt
                g=g//pnt
                p[i,j]=(r,g,b)
        cnt-=1
        
    return p

def black___white(pixels,x,y):
    for i in range(0,x):
        for j in range(0,y):
        
            z= pixels[i,j][0]+pixels[i,j][1]+pixels[i,j][2]
            z =z//3
         
            pixels[i,j]=(z,z,z)
    return pixels

def swap_red_with_green(p,x,y):
    for i in range(0,x):
        for j in range(0,y):
            z=0
         #   print(i,j)
            z+=p[i,j][0]
            z%=256
            zz=0
            zz+=p[i,j][1]
            zzz=0
            zzz+=p[i,j][2]
            zz%=256
            zzz%=256
            p[i,j]=(zz,z,zzz)
    return p
def swap_blue_with_green(p,x,y):
    for i in range(0,x):
        for j in range(0,y):
            z=0
         #   print(i,j)
            z+=p[i,j][0]
            z%=256
            zz=0
            zz+=p[i,j][1]
            zzz=0
            zzz+=p[i,j][2]
            zz%=256
            zzz%=256
            p[i,j]=(z,zzz,zz)
    return p
def makebrighter(p,x,y):
    for i in range(0,x):
        for j in range(0,y):
            z=30
         #   print(i,j)
            z+=p[i,j][0]
            z=min(z,255)
            zz=30
            zz+=p[i,j][1]
            zzz=30
            zzz+=p[i,j][2]
            zz=min(zz,255)
            zzz=min(zzz,255)
            p[i,j]=(z,zz,zzz)
    return p
def makedarker(p,x,y):
    for i in range(0,x):
        for j in range(0,y):
            z=-30
         #   print(i,j)
            z+=p[i,j][0]
            if (z<0) :
                z=0
            zz=-30
            zz+=p[i,j][1]
            zzz=-30
            zzz+=p[i,j][2]
            zz=min(zz,255)
            zzz=min(zzz,255)
            if (zz<0):
                zz=0
            if (zzz<0):
                zzz=0
            p[i,j]=(z,zz,zzz)
    return p
def editalaki1(p,x,y):
    for i in range(0,x):
        for j in range(0,y-2):
            if (i%6==0):
                if (j%6!=2 and j%6!=3):
                    p[i,j]=(255,255,255)
            if (i%6==1):
                if (j%6==0 or j%6==5):
                    p[i,j]=(255,255,255)
            if (i%6==5):
                if (j%6!=2 and j%6!=3):
                    p[i,j]=(255,255,255)
            if (i%6==4):
                if (j%6==0 or j%6==5):
                    p[i,j]=(255,255,255)
            if (p[i,j][0]!=255 or p[i,j][1]!=255 or p[i,j][2]!=255):
                p[i,j]=p[i-(i%6),j-(j%6)+2]
    return p
def shatranji(p,x,y):
    for i in range(0,x):
        for j in range(0,y-2):
            p[i,j]=p[i-(i%6),j-(j%6)]
    return p
def mirrorphoto(p,q,x,y):
    for i in range(0,x):
        for j in range(0,y):
            z=q[i,j][0]
         #   print(i,j)
            z+=p[i,j][0]
            z//=2
            zz=q[i,j][1]
            zz+=p[i,j][1]
            zz//=2
            zzz=q[i,j][2]
            zzz+=p[i,j][2]
            zzz//=2
            p[i,j]=(z,zz,zzz)
    return p
userid = {}
ts = 0
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chatid=message.chat.id
   # ts+=1
    userid[chatid] = '0'
    print(chatid)
    bot.reply_to(message, "use \n /shatranji \n /editalaki1 \n /edge_finder \n /mirrorphoto \n /makedarker \n /makebrighter \n /swap_blue_with_green \n /swap_red_with_green \n /black_white \n /portrait (you should color the face or ... if you dont want that bot changes that erea) \n /portraitAI with AI \n /background")
@bot.message_handler(commands=['shatranji'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 15
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['editalaki1'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 14
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['edge_finder'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 13
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['makedarker'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 10
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['mirrorphoto'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 11
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['makebrighter'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 9
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['portrait'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 5
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['swap_red_with_green'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 7
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")

@bot.message_handler(commands=['swap_blue_with_green'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 8
        bot.reply_to(message, "send me your main photo")
    else:
        bot.reply_to(message,"use /start first")

@bot.message_handler(commands=['black_white'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 1
        bot.reply_to(message, "send me your photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['portraitAI'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 2
        bot.reply_to(message, "send me your photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['background'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 3
        bot.reply_to(message, "now send me your main photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(func=lambda msg: True)
def send___welcome(message):
        bot.reply_to(message,message)
ma =dict()
ma[813953288]=1
ma[-537382648]=1
ma[180255479]=1
ma[-506115149]=1
ma[-500852224]=1
ma[411207441]=1
@bot.message_handler(content_types=['photo'])
def photo(message):
    chatid=message.chat.id
    print (chatid)
    if (ma.get(chatid) or chatid<0) :
        return 
    print ('message.photo ='), message.photo
    fileID = message.photo[-1].file_id
    #print 'fileID =', fileID
    file_info = bot.get_file(fileID)
    #print 'file.file_path =', file_info.file_path
    downloaded_file = bot.download_file(file_info.file_path)
    if (userid.get(chatid)):
        print(chatid)
    else:
        bot.reply_to(message, "please use /start command")
        return
    
    
    #if (userid[chatid]==3):
    if (userid[chatid]==5):
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,"now please send this photo and highlight or mark the places you dont want to change (face and ...)")
        userid[chatid]=6
        return 
    elif (userid[chatid]==6):
        with open("background.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
    elif (userid[chatid]==3):
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,"send me your background")
        userid[chatid] = 4
        return
    elif (userid[chatid]==11):
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,"send me your background")
        userid[chatid] = 12
        return
    elif (userid[chatid]==12):
        with open("background.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
    elif (userid[chatid]==4):
        with open("background.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
    else:
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
    im = Image.open("image.jpg")
    background = Image.open("background.jpg")
    pixelss = im.load()
    #print(userid[chatid])
    x=im.size[0]
    y=im.size[1]
    print(x)
    print(y)
    background = background.resize((x,y))
    print(background.size)
    print(userid[chatid])
    print( " we ")
   # pixel_values = list(im.getdata())
    #pixel_values = numpy.array(pixel_values).reshape((x, y, 3))
    print("shash")
    
    pix = background.load()
    print( " woeijd ")
    if (userid[chatid]==12):
        pixelss=mirrorphoto(pixelss,pix,x,y)
    if (userid[chatid]==10):
        pixelss=makedarker(pixelss,x,y)
    if (userid[chatid]==9):
        pixelss=makebrighter(pixelss,x,y)
    if (userid[chatid]==8):
        pixelss=swap_blue_with_green(pixelss,x,y)
    if (userid[chatid]==7):
        pixelss=swap_red_with_green(pixelss,x,y)
    if (userid[chatid]==6):
        pixelss=fportrait(pixelss,pix,x,y)
    if (userid[chatid]==1 or userid[chatid]==13):
        pixelss=black___white(pixelss,x,y)
    if (userid[chatid]==2):
        pixelss=f_low_qq(pixelss,x,y)
    if (userid[chatid]==14):
        pixelss=editalaki1(pixelss,x,y)
    print("duhf")
    if (userid[chatid]==4):
        print("rjfern")
        fputbackground(pixelss,pix,x,y)
        print("urg3foe4ijg")
    if (userid[chatid]==13):
        #pixelss=edgefinder(pixelss,x,y)
        im = im.filter(ImageFilter.FIND_EDGES)
    if (userid[chatid]==15):
        pixelss = shatranji(pixelss,x,y)
    im.save("image.jpg")
    im.show()
    with open("image.jpg","rb") as misc:
        f=misc.read()
    bot.send_document(message.chat.id,f)
    bot.send_photo(chatid, photo=open('image.jpg', 'rb'))
    
   # bot.send_photo(, document=open('image.jpg', 'rb'))

while True:   
    try :
        bot.polling()
    except :
        time.sleep(5)
