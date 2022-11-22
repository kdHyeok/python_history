import pygame
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import random

fp = open('wordDic.txt', 'r', encoding='UTF-8')
wDic = dict()

root = Tk()
op1 = StringVar()
searchEng = StringVar()


while True:
    st = fp.readline()
    if not st :
        break;
    kor, eng = st.split()
    wDic[eng] = kor

def reverse_dict(dict):
    new_dict = {}
    for key, value in wDic.items():
        new_dict[value] = key
    return new_dict

def searchbutton():
    global searchLB1, searchLB2, searchent
    searchLB1 = Label(root, text="궁금한거 있으면 쳐봐!", width=45, height=2, foreground="white", background="#2f3640", anchor=CENTER, font=("30"))
    searchLB1.place(x=80, y=120)

    searchLB2 = Label(root, text="여기로 답해줄게!", width=45, height=2, foreground="white", background="#2f3640", anchor=CENTER, font=("30"))
    searchLB2.place(x=80, y=160)

    searchent = Entry(root, width=30, borderwidth = 5,fg = "white", bg = "black",textvariable=searchEng)
    searchent.bind("<Return>",searcheng)
    searchent.place(x=170, y=250)

def searcheng(event):
        ss = searchEng.get()

        if ss in wDic:
            searchLB2.configure(text=f"{ss}의 뜻은 {wDic[ss]}입니다.")
        else:
            new_dic = reverse_dict(wDic)
            if ss in new_dic:
                searchLB2.configure(text=f"{ss}의 뜻은 {new_dic[ss]}입니다.")
            else:
                searchLB2.configure(text="이 단어는 아직 안배웠어")
        searchent.delete(0,"end")

def intRandom():
    global a
    a = random.randrange(1, 11, 1)


def imageRandom():
    global image_size, answer, label3, image_label, btnanswer, btnclears, cleanbutton
    intRandom()

    answer = tkinter.Entry(width = 30, textvariable=op1)
    answer.bind('<Return>', enters)
    answer.place(x=170,y=330)

    btnanswer = Button(root, text="제출", width=5, height=1, command=randomgame)
    btnanswer.place(x=170, y=360)

    randomgame()

    btnclears = Button(root, text="다음 문제!",width=8, height=1, command=btnclear)
    btnclears.place(x=220, y=360)

    cleanbutton = Button(root, text = "화면 끄기!", width = 8, height = 1, command=btnclean)
    cleanbutton.place(x= 325, y = 360)

    label3 = Label(root, text="이건 영어로 멀까요? 맞추면 초콜렛 한개!",width = 45, height = 1,foreground = "white",background = "#2f3640", anchor = CENTER,font=("16"))
    label3.place(x=80, y=70)

    if(a == 1):
        images = Image.open(f"{image_names}.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif(a == 2):
        images = Image.open("banana.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif(a == 3):
        images = Image.open("수박.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif(a == 4):
        images = Image.open("dance.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif(a == 5):
        images = Image.open("ask.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif (a == 6):
        images = Image.open("dog.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif (a == 7):
        images = Image.open("cat.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif (a == 8):
        images = Image.open("family.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif (a == 9):
        images = Image.open("flower.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

    elif (a == 10):
        images = Image.open("red.png")
        image_size = images.resize((250, 200))
        image_size = ImageTk.PhotoImage(image_size)
        image_label = Label(image=image_size)
        image_label.place(x=150, y=100)

def randomgame():
    txt = answer.get()

    if (a == 1):
        if(txt == 'apple'):
            label3.configure(text= "사과는 apple! 정답!")
        elif(txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 사과")

    if (a == 2):
        if (txt == 'banana'):
            label3.configure(text= "바나나는 banana! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 바나나")
    if (a == 3):
        if (txt == 'watermelon'):
            label3.configure(text="수박은 watermelon! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 수박")

    if (a == 4):
        if (txt == 'dance'):
            label3.configure(text="춤은 dance! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 노래가 나오면서 사람들이 하는 것!")

    if (a == 5):
        if (txt == 'ask'):
            label3.configure(text="질문하다는 ask! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 여러분들이 모를때 선생님한테 하는 것!")

    if (a == 6):
        if (txt == 'dog'):
            label3.configure(text="개는 dog! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 멍멍!")

    if (a == 7):
        if (txt == 'cat'):
            label3.configure(text="고양이는 cat! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 야옹~")

    if (a == 8):
        if (txt == 'family'):
            label3.configure(text="가족은 family! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 아빠, 엄마, 나, 형, 누나, 동생")

    if (a == 9):
        if (txt == 'flower'):
            label3.configure(text="꽃은 flower! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text= "틀렸어요! 힌트 : 식물인데 이쁘고 향이나요!")

    if (a == 10):
        if (txt == 'red'):
            label3.configure(text="빨간색은 red! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 색깔 중 빨간색!")

def btnQuestion():
    click_sound.play()
    label1 = Label(root, text = "영어 단어 번영 게임")
    label2 = Label(root, text = "영어 단어를 번역하는 게임 입니다.")

    label1.pack()
    label2.pack()

    keys = list(wDic.keys())
    random.shuffle(keys)
    count = 0
    correct = 0

    for eng in keys:
        count = count + 1
        kor = wDic[eng]

        guess = input('{} 영어 단어를 번역하세요: '.format(eng))

        if guess == kor:
            print('영어 단어의 번역이 맞습니다.')
            correct += 1
        else:
            print('영어 단어의 번역이 틀립니다.')

        if count == 4:
            print('%d번 맞췄어요!! 수고햇어!'%correct)
            break

def btnExit():
    msgbox = tkinter.messagebox.askquestion('확인','끌꺼야? 한번만 더 보자!!')
    if msgbox == 'yes':
        exit()

def enters(event):
    txt = op1.get()

    if (a == 1):
        if (txt == 'apple'):
            label3.configure(text="사과는 apple! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 사과")

    if (a == 2):
        if (txt == 'banana'):
            label3.configure(text="바나나는 banana! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 바나나")
    if (a == 3):
        if (txt == 'watermelon'):
            label3.configure(text="수박은 watermelon! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 수박")

    if (a == 4):
        if (txt == 'dance'):
            label3.configure(text="춤은 dance! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 노래가 나오면서 사람들이 하는 것!")

    if (a == 5):
        if (txt == 'ask'):
            label3.configure(text="질문하다는 ask! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 여러분들이 모를때 선생님한테 하는 것!")

    if (a == 6):
        if (txt == 'dog'):
            label3.configure(text="개는 dog! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 멍멍!")

    if (a == 7):
        if (txt == 'cat'):
            label3.configure(text="고양이는 cat! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 야옹~")

    if (a == 8):
        if (txt == 'family'):
            label3.configure(text="가족은 family! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 아빠, 엄마, 나, 형, 누나, 동생")

    if (a == 9):
        if (txt == 'flower'):
            label3.configure(text="꽃은 flower! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 식물인데 이쁘고 향이나요!")

    if (a == 10):
        if (txt == 'red'):
            label3.configure(text="빨간색은 red! 정답!")
        elif (txt == ''):
            print("긴장하지 말고 맞춰봐요! 맞추면 초콜렛 한개 !")
        else:
            label3.configure(text="틀렸어요! 힌트 : 색깔 중 빨간색!")
    answer.delete(0, "end")

def btnclear():
    imageRandom()
    label3.destroy()
    image_label.destroy()
    btnanswer.destroy()
    answer.destroy()
    btnclears.destroy()
    cleanbutton.destroy()

def btnclean():
    label3.destroy()
    image_label.destroy()
    btnanswer.destroy()
    answer.destroy()
    btnclears.destroy()
    cleanbutton.destroy()

pygame.init()

test_sound = pygame.mixer.Sound('C:/Users/qaz00/PycharmProjects/Game/Linda 행진곡.mp3')
test_sound.set_volume(0.2)
test_sound.play(-1)

click_sound = pygame.mixer.Sound('C:/Users/qaz00/PycharmProjects/Game/Catoon Duck.mp3')


root.title("영어 공부")
root.geometry("550x550")
root.resizable(False,False)


wall = PhotoImage(file ='C:/Users/qaz00/PycharmProjects/Game/배경/background.png')
wall_label = Label(image=wall)
wall_label.place(x = 0, y = 0)

searchbtn = Button(root, text = "단어 검색", width = 15, height = 2, command=searchbutton)
searchbtn.place(x = 120 , y = 400)

btnQuestion = Button(root, text = "문제 풀기", width = 15, height = 2, command=btnQuestion)
btnQuestion.place(x = 330 , y = 450)

btngame = Button(root, text = "보면서 푸는 퀴즈", width = 15, height = 2, command=imageRandom)
btngame.place(x = 120 , y = 450)

btnexit = Button(root, text = "끄기",command=btnExit)
btnexit.place(x = 260, y = 500)

root.mainloop()

