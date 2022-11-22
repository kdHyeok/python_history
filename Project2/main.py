from tkinter import *
import tkinter.font as font
import pygame

key = ""

mx = 0
my = 0

map = [
        [1, 1, 1, 1, 1, "겨울", 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        ["봄", 0, 0, 0, 1, 0, 1, 0, 0, 0, "가을"],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, "여름", 1, 1, 1, 1, 1]
    ]

def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym

def Game():
    global mx, my, cv
    mx = 5
    my = 5

    cv = Canvas(width=430, height=430, bg="white", borderwidth=3)

    img = PhotoImage(file="jbchar.png")
    cv.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")

    def Map():
        for x in range(11):
            for y in range(11):
                if map[x][y] == 1:
                    cv.create_rectangle(x * 40, y * 40, x * 40 + 39, y * 40 + 39, fill="gray", width=0)

                elif map[x][y] == "봄":
                    cv.create_rectangle(x * 40, y * 40, x * 40 + 39, y * 40 + 39, fill="yellowgreen", width=0)
                    cv.create_text(220,19, text="봄")
                    map[5][0] = 0

                elif map[x][y] == "여름":
                    cv.create_rectangle(x * 40, y * 40, x * 40 + 39, y * 40 + 39, fill="blue", width=0)
                    cv.create_text(418,220, text = "여름")
                    map[10][5] = 0

                elif map[x][y] == "가을":
                    cv.create_rectangle(x * 40, y * 40, x * 40 + 39, y * 40 + 39, fill="orange", width=0)
                    cv.create_text(220,418, text = "가을")
                    map[5][10] = 0

                elif map[x][y] == "겨울":
                    cv.create_rectangle(x * 40, y * 40, x * 40 + 39, y * 40 + 39, fill="skyblue", width=0)
                    cv.create_text(21,220, text="겨울")
                    map[0][5] = 0

    def charMove():
        global mx, my, key

        if key == "Left" and map[mx - 1][my] == 0:
            mx = mx - 1

        if key == "Right" and map[mx + 1][my] == 0:
            mx = mx + 1

        if key == "Up" and map[mx][my - 1] == 0:
            my = my - 1

        if key == "Down" and map[mx][my + 1] == 0:
            my = my + 1

        if mx == 0 and my == 5:
            mx = 5
            my = 5
            Winter()

        elif mx == 5 and my == 10:
            mx = 5
            my = 5
            fall()

        cv.delete("MYCHR")  # 우선 캐릭터 삭제함
        cv.create_image(mx * 40 + 20, my * 40 + 20, image=img, tag="MYCHR")  # 다시 캐릭터를 화면에 표시함
        root.after(90, charMove)

    charMove()
    Map()
    cv.place(x= 80, y = 40)
#=============================================================================================================================
def Winter():
    global winterground, winter_label, btnquestion
    winterground = PhotoImage(file="Winter.png")
    winter_label = Label(image=winterground)
    winter_label.place(x = 0, y = 0)

    btnquestion = Button(root, text="게임 끄기", width=15, height=2, command=Winter_back)
    btnquestion.place(x=240, y=500)

def Winter_back():
    winter_label.destroy()
    btnquestion.destroy()

#======================================================================================================================
def fall():
    global fall_ground, fall_label, btnquestionf, ma1, m1_label, text1, Tfont, chat1, chat2, pa_label #fall_ground, m1의 경우 글로벌 변수로 선언해줘야 이미지가 보임
    pa_label=Label()
    fall_ground = PhotoImage(file="fall_bgr.png")
    ma1 = PhotoImage(file="mas1.png")

    fall_label = Label(image=fall_ground)
    fall_label.place(x = 0, y = 0)
    m1_label = Label(image=ma1)
    m1_label.place(x=370, y=60)

    text1 = Text(root, bg="#EAEAEA", height=6, width=47)
    text1.place(x=20, y=270)
    Tfont = font.Font(family="Arial", size=10, weight="bold")

    text1.insert(1.0,"안녕? 반가워. 나는 너와함께 여행을 갈 수달이라고 해!\n")
    text1.insert(2.0, "우리 지금부터 가을 여행을 떠나볼까?")
    text1.configure(font=Tfont, state='disabled')

    chat1 = Button(root, bg="#BDBDBD", text="좋아! 어디로 갈까?", height=2, width=82, command=fall_1)
    chat1.place(x=10, y=400)
    chat2 = Button(root, bg="#BDBDBD", text="정말 기대된다!!", height=2, width=82, command=fall_1)
    chat2.place(x=10, y=450)

    bsound_play('배경음.mp3',0.2,-1)

    btnquestionf = Button(root,bg="#EAEAEA", text="게임 끄기", width=15, height=2, command=fall_back)
    btnquestionf.place(x=240, y=500)

#======================================================================================
def Text_insert(msg,xx,yy): #텍스트창 추가
    global text1
    text1.destroy()
    text1 = Text(root, bg="#EAEAEA", height=6, width=47)
    text1.place(x=xx, y=yy)
    text1.insert(1.0, str(msg))
    text1.configure(font=Tfont, state='disabled')
def chat1_in(msg,cmd): #버튼1 추가
    global chat1
    chat1.destroy()  # 초기화
    chat1 = Button(root, bg="#BDBDBD", text=str(msg), height=2, width=82, command=cmd)  # 재선언
    chat1.place(x=10, y=400)
def chat2_in(msg,cmd): #버튼2 추가
    global chat2
    chat2.destroy()  # 초기화
    chat2 = Button(root, bg="#BDBDBD", text=str(msg), height=2, width=82, command=cmd)  # 재선언
    chat2.place(x=10, y=450)
def mas_in(img,xx,yy): #캐릭터 추가
    global m1_label, masc
    masc = PhotoImage(file=str(img))
    m1_label.destroy()  # 초기화
    m1_label = Label(image=masc)  # 재선언
    m1_label.place(x=xx, y=yy)
def sound_play(sttr,vr,tm): #소리 넣기
    global test_sound
    pygame.init()
    test_sound = pygame.mixer.Sound(str(sttr))
    test_sound.set_volume(vr)
    test_sound.play(tm)
def bsound_play(sttr,vr,tm): #소리 넣기
    global back_sound
    pygame.init()
    back_sound = pygame.mixer.Sound(str(sttr))
    back_sound.set_volume(vr)
    back_sound.play(tm)
def img_in(img,xx,yy): #추가 이미지 넣기
    global  pa_label, images
    pa_label.destroy()
    images = PhotoImage(file=str(img))
    pa_label = Label(image=images)
    pa_label.place(x=xx, y=yy)
def background_in(bimg):
    global fall_label, back_img, btnquestionf
    fall_label.destroy()
    back_img = PhotoImage(file=str(bimg))
    fall_label = Label(image=back_img)
    fall_label.place(x=0, y=0)
    btnquestionf.destroy()
    btnquestionf = Button(root, bg="#EAEAEA", text="게임 끄기", width=15, height=2, command=fall_back)
    btnquestionf.place(x=240, y=500)
#======================================================================================================================

def fall_1():

    mas_in("mas2.png",370,60)

    Text_insert('알겠어! 지금부터 우리가 갈 곳은 내장산이라는 곳이야!',20,270)
    chat1_in("내장산? 거기가 어디야?", fall_2a)
    chat2_in("내장산 좋지, 정말 기대된다!!", fall_2b)


def fall_2a():
    global chat1
    mas_in("mas2.png",370,60)

    Text_insert('내장산은 호남 5대의 명산 중 하나이자 한국을 대표하는 8경 중 하나로 손꼽히는 곳으로 전북 정읍시와 순창군, 전남 장성군에 걸쳐 있어!',20,270)
    chat1.destroy()
    chat2_in("와.. 되게 넓다, 정말 아름다운 곳이겠는걸?!", fall_2b)

def fall_2b():
    global m1_label, chat1, chat2
    background_in("내장산.png")
    m1_label.destroy() #초기화
    text1.destroy()
    chat1.destroy() #초기화

    sound_play('car.mp3',0.4,0)
    chat2_in("어? 여기가 바로 내장산이구나~!",fall_3)

def fall_3():
    global text
    img_in("주차장.png",80,50)

    mas_in("mas1.png",370,60)
    Text_insert('내장산에 드디어 도착했어! 혹시 다음에 차를 타고오게 된다면 산아래에 공용 주차장이 있으니까 참고하도록해!\n\n'
                     '주차요금은 경차는 2,000원, \n중소형은 4,000원(성수기 5,000원), \n대형은 6,000원(성수기 7,500원)이니까 잘 알아둬.',20,270)
    chat1_in("도착하니까 배가 너무 고프다.. 주위에 맛있는 곳 없을까?",fall_4a)
    chat2_in("알겠어! 그럼 이제 빨리 단풍구경하러 가자!!",fall_4b)

def fall_4a():
    mas_in("mas3.png",370,60)
    img_in("맛집.png",30,5)
    sound_play('hungry.mp3',0.4,0)
    Text_insert('나도 배고프다ㅎㅎ;; 그럼 이 근처에 맛집을 알려줄게.\n\n'
                '1번, 화덕갈비 정읍점! 육류,고기요리를 하는 곳이야.\n'
                '2번, 내장산한옥회관! 한정식을 하는곳이지.',20,270)
    chat1_in("고기??! 맛있겠다. 고기먹으러 가자!", fall_4aa)
    chat2_in("한정식 좋지! 우리 한정식이나 먹으러 가자~", fall_4ab)

def fall_4aa():
    background_in("화덕갈비.png")
    mas_in("mas1.png",370,60)
    img_in("고기집.png",50,5)
    Text_insert('여기가 바로 화덕갈비 정읍점이야~!\n'
                '....\n(30분 후)\n....\n'
                '고기 완전 맛있다~!! 넌 어땠어? ',20,270)
    chat1_in("맛있었어! 근데.. 아직 배고픈데, 우리 아까 다른 곳도 갈까?", fall_4ab)
    chat2_in("아~ 배부르다! 완전 맛있었어, 이제 다시 내장산으로 돌아가자!", fall_4b)
def fall_4ab():
    background_in("한옥회관.png")
    mas_in("mas1.png",370,60)
    img_in("한정식.png",50,5)
    Text_insert('여기가 바로 내장산한옥회관이야~!\n'
                '....\n(30분 후)\n....\n'
                '한정식 완전 맛있다~!! 넌 어땠어? ',20,270)
    chat1_in("맛있었어! 근데.. 아직 배고픈데, 우리 아까 다른 곳도 갈까?", fall_4aa)
    chat2_in("아~ 배부르다! 완전 맛있었어, 이제 다시 내장산으로 돌아가자!", fall_4b)

def fall_4b():
    background_in("탐방안내소p.png")
    mas_in("mas2.png",370,60)
    img_in("안내소.png",80,50)
    Text_insert('여기가 바로 내장잔 국립공원의 탐방 안내소야!\n'
                '이제 우리가 갈 코스를 정할건데 어디로 갈까?\n'
                '[전망대 코스]\n'
                '소요시간 : 00 시간 50분   거리 : 1.8 ㎞   난이도 : 하\n'
                '[서래봉 코스]\n'
                '소요시간 : 04 시간 00분   거리 : 5.9 ㎞   난이도 : 하',20,270)
    chat1_in("전망대 코스로 가자!", fall_5a)
    chat2_in("서래봉 코스로 가자!", fall_5b)

def fall_5a():
    background_in("등산길.png")
    mas_in("mas1.png",370,60)
    img_in("전망대 코스.png",50,10)
    Text_insert('이제부터 우리는 전망대 코스로 갈꺼야!\n'
                '전망대 코스는 탐방안내소~케이블카~전망대~내장사~탐방안내소\n'
                '순으로 거쳐가는 길이니까 잘 따라와!',20,270)
    chat2_in("출발하자!", fall_5a1)
    chat1.destroy()
def fall_5a1():
    img_in("케이블카.png",40,40)
    Text_insert('어때? 케이블카로 타고가니까 편하고 경치도 좋지?',20,270)
    chat2_in("그러게 완전 좋다!", fall_5a2)
def fall_5a2():
    img_in("a2.png",40,40)
    Text_insert('여기는 천연기념물91호로 지정된 굴거리나무군락지야!',20,270)
    chat2_in("그렇구나~ 정말 에쁘다!", fall_5a3)
def fall_5a3():
    img_in("a3.png",40,40)
    Text_insert('여기가 바로 전망대야!',20,270)
    chat2_in("전망대에서 보니까 경치가 너무 좋다.", fall_5a4)
def fall_5a4():
    img_in("a4.png",40,40)
    Text_insert('그치? 주위에 단풍으로 물든 모습이 너무 예쁘다.',20,270)
    chat2_in("정말 그렇다. 빨리 내장사도 가보자!", fall_5a5)
def fall_5a5():
    background_in("내장사b.png")
    mas_in("mas1.png", 370, 60)
    img_in("a5.png",40,40)
    mas_in("mas2.png", 370, 60)
    sound_play('새.mp3', 0.6, 0)
    Text_insert('헥헥.. 이제 마지막으로 내장사에 도착했어!',20,270)
    chat2_in("와, 진짜 공기 좋다. 내장사도 정말 아름다운 곳인거같아!", fall_5a6)
def fall_5a6():
    background_in("탐방안내소p.png")
    mas_in("mas2.png",370,60)
    pa_label.destroy()
    Text_insert('자, 이제 다시 돌아왔네. 산에 올라갔다오니까 어때?',20,270)
    chat1_in("정말 재밌고 힐링되는 시간이였어! 고마워.", fall_6)
    chat2_in("아쉬운데, 서래봉 코스도 다녀와보자!", fall_5b)
def fall_5b():
    background_in("등산길.png")
    mas_in("mas1.png",370,60)
    img_in("서래봉 코스.png",50,10)
    Text_insert('이제부터 우리는 서래봉 코스로 갈꺼야!\n'
                '서래봉 코스는 일주문~벽련암~서래봉~불출봉~원적암~내장사~일주문\n'
                '순으로 거쳐가는 길이니까 잘 따라와!',20,270)
    chat2_in("이제 출발하자!", fall_5b1)
    chat1.destroy()
def fall_5b1():
    img_in("b1.png",40,40)
    Text_insert('여기가 일주문이야. 여기서부터 시멘트로 이루어져 있고 다소 경사가 있는 구간이니까 조심해!',20,270)
    chat2_in("알았어! 조심히 가보자!!", fall_5b2)
def fall_5b2():
    img_in("b2.png",40,40)
    Text_insert('여기는 벽련암. 정말 경치 좋지?',20,270)
    chat2_in("정말 멋있다!", fall_5b3)
def fall_5b3():
    img_in("b3.png",40,40)
    Text_insert('여기 보이는 곳이 바로 서래봉이야!',20,270)
    chat2_in("경치가 정말 장난 아닌데? 멋진 관경이다.", fall_5b4)
def fall_5b4():
    img_in("b4.png",40,40)
    mas_in("mas4.png", 370, 60)
    Text_insert('헥헥... 저기 밑에 보여? 저기가 우리가 아까 지나쳤던 벽련암이야!',20,270)
    chat2_in("우와 진짜? 우리 되게 멀리왔다.", fall_5b5)
def fall_5b5():
    background_in("내장호b.png")
    mas_in("mas1.png", 370, 60)
    img_in("b5.png",40,40)
    sound_play('산.mp3', 0.1, 0)
    Text_insert('자! 드디어 도착했다. 여기가 바로 이 코스의 하이라이트 내장호야!',20,270)
    chat2_in("와,,, 정말 아름답다. 너무 에쁜거같아.", fall_5b6)
def fall_5b6():
    background_in("탐방안내소p.png")
    mas_in("mas2.png",370,60)
    test_sound.stop()
    pa_label.destroy()
    Text_insert('자, 이제 다시 돌아왔네. 산에 올라갔다오니까 어땠어?',20,270)
    chat1_in("정말 재밌고 힐링되는 시간이였어! 고마워.", fall_6)
    chat2_in("아쉬운데, 전망대 코스도 다녀와보자!", fall_5a)
def fall_6():
    background_in("내장산.png")
    mas_in("mas2.png",210,10)
    Text_insert('재밌었다니 다행이네.\n'
                '이제 오늘 여행은 끝났어! 재밌게 즐겼니?',150,330)
    chat2_in("고마워 수달아! 덕분에 재밌게 즐겼어. 다음에 또 보자! ", fall_back)
    chat1.destroy()
def fall_back():
    fall_label.destroy()
    btnquestionf.destroy()
    m1_label.destroy()
    text1.destroy()
    chat1.destroy()
    chat2.destroy()
    pa_label.destroy()
    back_sound.stop()


#=================================================================================================

root = Tk()
root.title("전라북도 관광 홍보")
root.resizable(False,False)

root.geometry('600x600')

root.bind("<KeyRelease>", key_up)
root.bind("<KeyPress>", key_down)

back = PhotoImage(file ='background.png')
back_label = Label(image = back)
back_label.place(x = 0, y = 0)

btngame = Button(root, text="여행 떠나기", width=15, height=2, command = Game)
btngame.place(x=240, y=500)

root.mainloop()