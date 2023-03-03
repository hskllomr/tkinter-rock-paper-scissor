from tkinter import *
import random

root = Tk()


root.geometry("300x300")


root.title("Rock Paper Scissor Game")

computer_value = {
    "0": "Rock",#bilgisayarın rastgele seçeceği değerler
    "1": "Paper",
    "2": "Scissor"
}

def reset_game():#oyunu sıfırla
    b1["state"]="active"#butonları aktifleştir
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text="Player          ")
    l3.config(text="Computer")
    l4.config(text="")

def button_disable():#oyuncu seçim yaptıktan sonra butonun işlevini geçersiz kıl.
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"

def rock():
    x=computer_value[str(random.randint(0,2))]
    if x=="Rock":
        match_result="Draw"
    elif x=="Scissor":
        match_result="Player Win"
    else:
        match_result="Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock      ")
    l3.config(text=x)
    button_disable()

def paper():#bu fonksiyon kağıdı seçtiğimiz durum için
    x=computer_value[str(random.randint(0,2))]
    if x=="Paper":
        match_result="Draw"
    elif x=="Scissor":
        match_result="Computer Win"
    else:
        match_result="Player Win"
    l4.config(text=match_result)#sonucu orta bölümdeki yere yazdır
    l1.config(text="Paper      ")#sol bölmeye kağıdı yaz
    l3.config(text=x)#sağ bölmeye bilgisyarın seçtiği metaryeli yaz
    button_disable()#butonu kilitle


def scissor():
    x = computer_value[str(random.randint(0, 2))]
    if x == "Rock":
        match_result = "Computer Win"
    elif x == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Scissor      ")
    l3.config(text=x)
    button_disable()



Label(root,text="Rock Paper Scissor",font="normal 20 bold",fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,text="Player       ",font=10)#orta sol bölme

l2 = Label(frame,text="VS             ",font="normal 10 bold")#orta bölme

l3 = Label(frame, text="Computer", font=10)#sağ bölme

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,text="",font="normal 20 bold",bg="white",width=15,borderwidth=2,relief="solid")#sonuç bölmesi
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1=Button(frame1,text="Rock",font=10,width=7,command=rock)
b2=Button(frame1,text="Paper",font=10,width=7,command=paper)#buton bölmesi
b3=Button(frame1,text="Scissor",font=10,width=7,command=scissor)

b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b3.pack(padx=10)

Button(root,text="Reset Game",font=10,fg="red",bg="black",command=reset_game).pack(pady=20)#reset butonu

root.mainloop()









