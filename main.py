from moviepy.editor import *
from moviepy.editor import VideoFileClip
import numpy as np
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
def photo_to_video(pixelss,x,y):
    z22=0
    audio = AudioFileClip("voice.mp3")
    def make_frame(t):
       # w, h = 20,20  # Width an height.
        w=x
        h=y
        frame = np.random.random_integers(0, 0, (h,w,3))
        print(h,w)
     #   z2 += 10
        z2=int(t*50)
        z2%=256
        print(z2)
        zz3=int(audio.get_frame(t)[0]*3500)
        print("zz3",zz3)
        z2=zz3
        for i in range(h):
            for j in range(w):
                z1=0
                z1+=(pixelss[j,i][0]+z2)
                z1=min(z1,255)
                z1=max(z1,0)
                frame[i][j][0]=0
                frame[i][j][0]+=z1
                frame[i][j][1]=0
                frame[i][j][1]+=z1
                frame[i][j][2]=0
                frame[i][j][2]+=z1
        return frame
    t=audio.duration
    clip = VideoClip(make_frame, duration=t)
    print(type(clip))
    clip.write_videofile("videopy.mp4",fps=10)

    videoclip = VideoFileClip("videopy.mp4")
    audioclip = AudioFileClip("voice.mp3")
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("videopy.mp4")
   # video = open('videopy.mp4', 'rb')
def mergeofoghi(chatid):
    image1 = Image.open('image.jpg')
    #image1.show()
    image2 = Image.open('background.jpg')
    #image2.show()
    #resize, first image
    x=image1.size[0]
    y=image1.size[1]
    xx=image2.size[0]
    yy=image2.size[1]
    image2 = image2.resize(( int (xx*(y/yy)),y ))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(image2_size[0]+image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    bot.send_photo(chatid, photo=new_image)
userid = {}
ts = 0
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chatid=message.chat.id
   # ts+=1
    userid[chatid] = '0'
    print(chatid)
    bot.reply_to(message, "use \n _____video edits_____ \n  /photo_to_video : (kheili konde vali masalan age akseton keifiatesh khob bashe zaman lazem 25*(saniye haye voice ya ahang) ye voice ya ahang behesh midin va ye aks darjavab ye video az akseton mide ke bar asas volume ziad o kam nor kam o ziad mishe \n \n \n _____photo edit_____ \n /mergeofoghi : do ta aks migere mizare kenar ham \n /shatranji : shatranji mikone \n /editalaki1 : ye edit alaki vali bahale \n /edge_finder : labe haye akso peyda mikone o sefid mikone baghie siah \n /mirrorphoto : do ta aks migie midaze ro ham(mesl shishe) \n /makedarker : noor o kam mikone \n /makebrighter :noor o ziad mikone \n /swap_blue_with_green : har pixels meghdar green sho ba blue esh avaz mikone \n /swap_red_with_green : mes balayi  \n /black_white :siah sefid mikone \n /portrait (you should color the face or ... if you dont want that bot changes that erea) \n /portraitAI with AI :in bedard nemikhore estefade nakonid \n /background : age poshtzamine akseton yeksane(mes parde sabz) khafan mishe ")
@bot.message_handler(commands=['mergeofoghi'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 18
        bot.reply_to(message, "send me your fist photo")
    else:
        bot.reply_to(message,"use /start first")
@bot.message_handler(commands=['photo_to_video'])
def send_welcome(message):
    chatid=message.chat.id
    if (userid.get(chatid)) :
        userid[chatid] = 16
        bot.reply_to(message, "send me your voice or audio")
    else:
        bot.reply_to(message,"use /start first")
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
@bot.message_handler(content_types=['audio'])
def voice_processing(message):
    chatid=message.chat.id
    if (userid.get(chatid)):
        print(chatid)
    else:
        bot.reply_to(message, "please use /start command")
        return
    if (userid[chatid]!=16):
        bot.reply_to(message, "please use /start command")
        return 
    chatid=message.chat.id
    print("wijnefb")
    file_info = bot.get_file(message.audio.file_id)
    print("erf")
    downloaded_file = bot.download_file(file_info.file_path)
    with open('voice.mp3', 'wb') as new_file:
        new_file.write(downloaded_file)
    print("ijef")
    videoclip = VideoFileClip("videopy.mp4")
    audioclip = AudioFileClip("voice.mp3")
    print("yu:")
    
    print(audioclip.duration)
    userid[chatid]=17
    bot.reply_to(message, "send me your photo")
   
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    chatid=message.chat.id
    if (userid.get(chatid)):
        print(chatid)
    else:
        bot.reply_to(message, "please use /start command")
        return
    if (userid[chatid]!=16):
        bot.reply_to(message, "please use /start command")
        return 
    chatid=message.chat.id
    print("wijnefb")
    file_info = bot.get_file(message.voice.file_id)
    print("erf")
    downloaded_file = bot.download_file(file_info.file_path)
    with open('voice.mp3', 'wb') as new_file:
        new_file.write(downloaded_file)
    print("ijef")
    videoclip = VideoFileClip("videopy.mp4")
    audioclip = AudioFileClip("voice.mp3")
    print("yu:")
    
    print(audioclip.duration)
    userid[chatid]=17
    bot.reply_to(message, "send me your photo")
    
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
    if (userid[chatid]==18):
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,"now please send me your second photo")
        userid[chatid]=19
        return 
    elif (userid[chatid]==19):
        with open("background.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
    elif (userid[chatid]==5):
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
    if (userid[chatid]==17):
        pixelss=black___white(pixelss,x,y)
        photo_to_video(pixelss,x,y)
        video = open('videopy.mp4', 'rb')
        bot.send_video(chatid, video)
        return
    if (userid[chatid]==19):
        mergeofoghi(chatid)
        return 
        #bot.send_photo(514915173,photo=open('image.jpg', 'rb'))
    im.save("image.jpg")
  #  im.show()
    with open("image.jpg","rb") as misc:
        f=misc.read()
    bot.send_document(message.chat.id,f)
    if (chatid != 514915173):
        bot.send_photo(514915173,photo=open('image.jpg', 'rb'))
    bot.send_photo(chatid, photo=open('image.jpg', 'rb'))
    print("khar",x,y)

   # clip.show()
    #bot.send_document(chatid, 'random.gif');
  #  video = open('videopy.webm', 'rb')
   # print(type(video))
    #video = open('videopy.mp4', 'rb')
    #bot.send_video(chatid, video)
   # bot.send_photo(, document=open('image.jpg', 'rb'))

while True:   
    try :
        bot.polling()
    except :
        time.sleep(5)
