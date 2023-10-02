from tkinter import *
import time
window= Tk()
window.title('digi Clock')
window.geometry('600x400')
def myTime():
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am_pm=time.strftime("%p")
    day=time.strftime('%A')
    zone=time.strftime('%Z')
    myText=hr+":"+min+":"+sec+" "+am_pm
    mytext2=day+","+zone
    myLabel.config(text=myText)
    mylabel2.config(text=mytext2)

    myLabel.after(1000,myTime)

myLabel=Label(window,text="heloo hamid",font=('calibri',70),fg='white',bg='black')
myLabel.pack()
mylabel2=Label(window,text="",font=("Times New Roman",24),fg='blue')

mylabel2.pack()
myTime()
window.mainloop()