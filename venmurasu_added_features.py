from tkinter import Label,Toplevel,Scrollbar,Text,RIGHT,Y,END,Button,Tk,StringVar,Frame,Entry,FLAT,Canvas
import datetime as dt
from PIL import ImageTk,Image
from tamil import utf8,numeral
from gtts import gTTS 
from playsound import playsound
import user_defined_library_package #user defined library

def mainpart():
    num=int(number.get())
    #same as the main file
    if(num<=12000):
        f=open(r"venmurasu_tamil_word_file_13.txt",'r',encoding='utf8')
    else:
        f=open(r"venmurasu_tamil_word_file_complete.txt",'r',encoding='utf8')
        
    tamil_list=f.read().split(',')
    f.close()  
    word_list=dict()
    for val in tamil_list:
        letters = utf8.get_letters(val) 
        length = len(letters)
        if length!=0:
            key=length
            word_list.setdefault(length,[])
            word_list[length].append(val)
        
    count=num
    
    file=open("sorted_words_file.txt",'a',encoding='utf8')
    userscreen.attributes('-topmost',False)
    global displayscreen #displayscreen to display sorted words
    displayscreen=Toplevel(userscreen)
    scrollbar = Scrollbar(displayscreen) #creating a scroll bar
    scrollbar.pack(side=RIGHT, fill=Y)                   
    textbox = Text(displayscreen,width=100,height=30,bd=5,font=("Cambria",'15'))
    textbox.pack() #Text box to display words
    
    displayscreen.title("Displaying Longest Words")
    photo = ImageTk.PhotoImage(Image.open( r"sound2.png") ) #sound icon
    
    value=1
    i=0
    btn_list = [] 
    def onClick1(idx):
        mytext=btn_list[idx].cget("text")
        language = 'ta' #tamil language
        myobj = gTTS(text=mytext, lang=language, slow=False) #tamil text to speech
        date_string = dt.datetime.now().strftime("%d%m%Y%H%M%S")
        filename = "voice"+date_string+".mp3"
        myobj.save(filename) #saving the audio with date time as filename
        playsound(filename) #playing the audio
        
    def onClick2(idx): #classification of letters
        mytext=btn_list[idx].cget("text")
        uyir,mei,uyirmei,ayutham,vada_mozhi,vallinam,mellinam,idayinam=user_defined_library_package.classify_words(mytext)
        class Table:
         def __init__(self,root):
            for i in range(rows):
                for j in range(cols): 
                    self.e = Entry(root, width=35, fg='black',font=('Cambria',16,'bold')) 
                    self.e.grid(row=i, column=j) 
                    self.e.insert(END, lst[i][j]) 
    
        lst=[ (u"உயிரெழுத்து (Uyir)",int(uyir)),
              (u"மெய்யெழுத்து (Mei)",int(mei)),
              (u"உயிர் மெய் எழுத்து (UyirMei)",int(uyirmei)),
              (u"ஆய்த எழுத்து (Ayutha)",int(ayutham)),
              (u"வடமொழி  எழுத்து (Sanskrit)",int(vada_mozhi)),
              (' ',' '),
              (u"வல்லினம் (Vallinam)",int(vallinam)),
              (u"மெல்லினம் (Mellinam)",int(mellinam)),
              (u"இடையினம் (Idayinam)",int(idayinam))]
        rows=len(lst)
        cols=len(lst[0])
       
        classify = Toplevel(displayscreen) #classification screen
        classify.title(mytext)
        t = Table(classify) 
        classify.mainloop() 
            
    
    for key in sorted(word_list,reverse=True):
        if count>0:
            textbox.insert(END,numeral.num2tamilstr(key)+u'  எழுத்துக்கள் : '  + str(key)+'\n\n')
            for val in word_list[key]: 
                textbox.insert(END,str(value)+' : '+val+'  ({})   '.format(str(key)))   
                file.write(str(key))
                file.write(val)  #storing in a file
                file.write('\n')
                btn1=Button(textbox,text = val,image=photo,borderwidth= 3, cursor="hand2",command = lambda idx=i : onClick1(idx))
                btn2=Button(textbox,text =u"வகைப்படுத்து",  borderwidth= 4,cursor="hand2",command = lambda idx=i : onClick2(idx))
                btn_list.append(btn1)
                i+=1
                textbox.window_create(textbox.index("end"), window = btn1) #adding buttons to Text box
                textbox.window_create(textbox.index("end"), window = btn2)
                textbox.insert(END,'\n\n')
                value+=1
                count=count-1
                
                if(count==0):
                    break
            textbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=textbox.yview) #configurations
    file.close()
    displayscreen.mainloop()
    
#Gui using tkinter
#we have tried our best to make the gui adapt to every different sized screen    
global userscreen
userscreen=Tk() #creating the root window
screen_width=userscreen.winfo_screenwidth() #reads your screen width
screen_height=userscreen.winfo_screenheight() #reads your screen height
userscreen.lift() #bringing the window to the front.tkinter window usually opens in the background
userscreen.attributes('-topmost',True) #making the window as the topmost window
userscreen.state('zoomed') #making it full screen
userscreen.geometry(str(screen_width)+'x'+str(screen_height)) #specifying geometry..varies from device to device
userscreen.title("Venmurasu Coding Contest")
#labels
label1=Label(userscreen,text=u"வெண்முரசு", fg="white",bg="maroon", width="300", height="2",font=("Cambria", 24,'bold') ).pack()
label2 = Label(userscreen, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="black", bg="antiquewhite",width=300,height=1, font=("Cambria", 18,'bold')).pack()
#background image
FILENAME ='img1.jpg'
canvas = Canvas(userscreen, width=screen_width, height=screen_height)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = FILENAME)
canvas.create_image(screen_width/2.5,screen_height/2.5, image=tk_img)

label3=Label(userscreen,text=u"சொற்களின் எண்ணிக்கையை உள்ளிடவும்",fg="Black",font=("Cambria",17,"bold")).place(x=screen_width/10.24,y=screen_height/5.4)
label4=Label(userscreen,text=u"வார்த்தை எண்ணிக்கை :",fg="Black",font=("Cambria",17,"bold")).place(x=screen_width/25.6,y=screen_height/2.88)

global number
number=StringVar()
#entry box 
entrybg = Frame(userscreen, background = 'orange', borderwidth = 3, relief = FLAT)
numberentry=Entry(entrybg,width=30,font=('10'),textvar=number)
entrybg.place(x=screen_width/3.3,y=screen_height/2.9)
numberentry.pack(ipady=4)
#submit button
btn1bg = Frame(userscreen, background = 'white', borderwidth = 3, relief = FLAT)
btn1=Button(btn1bg,text="உள்ளிடவும்", height="1", width="20",command=mainpart,font=("Cambria",17,"bold"),bg="maroon",fg="white")
btn1bg.place(x=screen_width/4.65,y=screen_height/1.92)
btn1.pack()

userscreen.mainloop()
