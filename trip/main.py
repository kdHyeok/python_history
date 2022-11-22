from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox

root = Tk()
root.title("봄 여행")
root.geometry("600x600")
root.resizable(False,False)

spwall = PhotoImage(file="spring2.png")
spwall_label = Label(image=spwall)
spwall_label.pack()

count_trip=0


def btnnext_count():
    global count_trip,trip_image_label
    global trip_image,trip_image_label,trip_image1,trip_image_label1,trip_image2,trip_image_label2,trip_image3,trip_image_label3

    ch_label.destroy()
    choice()

    if (count_trip ==0):

        ch1()
        ch_text.configure(text="가장 먼저 소개할 곳은 광한루원이야! 우리나라 4대누각에 \n들정도로 아름다운 건축물이지!\n 광한루주변의 풍경또한 사계절과 잘 어울러져,\n아름다운 경치를 볼 수 있어!!")
        trip_image = ImageTk.PhotoImage(Image.open("광한루원1.jpg"))
        trip_image_label = Label(root, image=trip_image)
        trip_image_label.place(x=50, y=70)

    elif (count_trip==1):

        choice1()
        trip_image_label.destroy()
        ch_text.configure(text="춘향테마파크는 춘향전을 테마로한 곳이다. \n다향한 체험과 고증이 잘 된 건물들을 볼수있다네.\n")
        trip_image1 = ImageTk.PhotoImage(Image.open("춘향테마파크.png"))
        trip_image_label1 = Label(root, image=trip_image1)
        trip_image_label1.place(x=50, y=70)

    elif (count_trip==2):

        choice2()
        ch2()
        trip_image_label1.destroy()
        ch_text.configure(text="팔랑치")
        trip_image2 = ImageTk.PhotoImage(Image.open("팔랑치.jpg"))
        trip_image_label2 = Label(root, image=trip_image2)
        trip_image_label2.place(x=50, y=100)

    elif (count_trip==3):

        choice3()
        trip_image_label2.destroy()
        ch_text.configure(text="서도역")
        trip_image3 = ImageTk.PhotoImage(Image.open("서도역.jpg"))
        trip_image_label3 = Label(root, image=trip_image3)
        trip_image_label3.place(x=50, y=50)


def btnnext():
    global count_trip
    btnnext_count()
    count_trip += 1





next=Button(root,text="다음",width=10,height=2,command=btnnext)
next.place(x=250,y=550)

def choice():
    global choice1_0,choice2_0,choice3_0

    choice1_0=Button(root,text="주변에 맛집은 뭐가있어?",width=20,height=2,command=choice_re)
    choice1_0.place(x=110,y=400)

    choice2_0=Button(root,text="나는 차가있어.",width=20,height=2,command=choice_re1)
    choice2_0.place(x=110,y=450)

    choice3_0=Button(root,text="꼭 봐야할 건 뭐야?",width=20,height=2,command=choice_re2)
    choice3_0.place(x=110,y=500)

    if count_trip==1:
        choice1_0.destroy()
        choice2_0.destroy()
        choice3_0.destroy()
        choice1()


def choice1():
    global choice1_1,choice2_1,choice3_1

    choice1_1=Button(root,text="주변에 쉴수 있는 곳이 있어?",width=20,height=2,command=choice_re)
    choice1_1.place(x=110,y=400)

    choice2_1=Button(root,text="나는 차가있어.",width=20,height=2,command=choice_re1)
    choice2_1.place(x=110,y=450)

    choice3_1=Button(root,text="꼭 봐야할 건 뭐야?",width=20,height=2,command=choice_re2)
    choice3_1.place(x=110,y=500)

    if count_trip==2:
        choice1_1.destroy()
        choice2_1.destroy()
        choice3_1.destroy()
        choice2()



def choice2():
    global choice1_2, choice2_2, choice3_2
    choice1_2=Button(root,text="봄에 가면 뭐가 있어?",width=20,height=2,command=choice_re)
    choice1_2.place(x=110,y=400)

    choice2_2=Button(root,text="나는 차가있어.",width=20,height=2,command=choice_re1)
    choice2_2.place(x=110,y=450)

    choice3_2=Button(root,text="",width=20,height=2,command=choice_re2)
    choice3_2.place(x=110,y=500)

    if count_trip==3:
        choice1_2.destroy()
        choice2_2.destroy()
        choice3_2.destroy()
        choice3()


def choice3():
    global choice1_3, choice2_3, choice3_3
    choice1_3=Button(root,text="",width=20,height=2,command=choice_re)
    choice1_3.place(x=110,y=400)

    choice2_3=Button(root,text="",width=20,height=2,command=choice_re1)
    choice2_3.place(x=110,y=450)

    choice3_3=Button(root,text="",width=20,height=2,command=choice_re2)
    choice3_3.place(x=110,y=500)

    if count_trip==4:
        choice1_3.destroy()
        choice2_3.destroy()
        choice3_3.destroy()


def choice_re():
    if count_trip==1:
        ch_text.configure(text="여행지에서 10분 이내로 도착하는 곳으로 추려봤다네.\n할매추어탕(추어탕)과 부산집(해물탕)의 음식이 일품이었네!")
    elif count_trip==2:
        ch_text.configure(text="산들 다런이라는 전통카페가 다과가 먹기에도, 보기에도 맛이 좋다네!")
    elif count_trip==3:
        ch_text.configure(text="")
    elif count_trip==4:
        ch_text.configure(text="ㄴ")

def choice_re1():
    if count_trip==1:
        ch_text.configure(text="관광안내소 바로 옆과, 위쪽에 있네만, 유료라네")
    elif count_trip==2:
        ch_text.configure(text="주차장은 \"춘향교\"로 넘어오는 입구쪽에 있지.\n참고로 유료주차이지.")
    elif count_trip==3:
        ch_text.configure(text="ㄷ")
    elif count_trip==4:
        ch_text.configure(text="ㄴ")

def choice_re2():
    if count_trip==1:
        ch_text.configure(text="이 장소는 춘향을 테마로 만들어진 곳으로 풍경을 보아도 좋고,\n전통문화 체험관도 있어 옛 문화를 접할 수 있다네 ")
    elif count_trip==2:
        ch_text.configure(text="ㅅ")
    elif count_trip==3:
        ch_text.configure(text="ㄷ")
    elif count_trip==4:
        ch_text.configure(text="ㄴ")




ch_text=Label(root,text="",font=10)
ch_text.place(x=50,y=300)


ch_text.configure(text="안녕! 우리는 남원의 마스코트 춘향이와 이몽룡이야!!\n남원의 명소를 이야기해줄께!\n다음을 눌러봐.")
ch = ImageTk.PhotoImage(Image.open("춘향이_이도령.png"))
ch_label = Label(root, image=ch)
ch_label.place(x=200, y=50)


def ch1():
    global ch1,ch_label1
    ch1=ImageTk.PhotoImage(Image.open("이도령.png"))
    ch_label1=Label(root,image=ch1)
    ch_label1.place(x=450,y=70)

def ch2():
    global ch2,ch2_label
    ch2=ImageTk.PhotoImage(Image.open("춘향.jpg"))
    ch2_label=Label(root,image=ch2)
    ch2_label.place(x=450,y=70)




root.mainloop()
