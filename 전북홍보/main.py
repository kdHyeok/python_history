from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import  tkinter.font as font


key = ""

mx = 0
my = 0

a = 1


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

    cv = Canvas(width=435, height=430, bg="white", borderwidth=3)

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
        global mx, my

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

        elif mx == 5 and my == 0:
            mx = 5
            my = 5
            Spring()

        elif mx == 10 and my == 5:
            mx = 5
            my = 5
            Summer()


        cv.delete("MYCHR")  # 우선 캐릭터 삭제함
        cv.create_image(mx * 40 + 20, my * 40 + 20, image=img, tag="MYCHR")  # 다시 캐릭터를 화면에 표시함
        root.after(90, charMove)

    charMove()
    Map()
    cv.place(x= 80, y = 40)

def Spring():
    global spwall_label, trip_image, trip_image_label, trip_image1, trip_image_label1, trip_image2, trip_image_label2, trip_image3, trip_image_label3, ch_label,ch, spwall, count_trip, next

    count_trip = 0

    spwall = PhotoImage(file="spring2.png")
    spwall_label = Label(image=spwall)
    spwall_label.place(x = 0 , y = 0)

    exitbtn = Button(root, text="종료", width=4, height=1, command=btnExit)
    exitbtn.place(x=558, y=15)

    ch_text = Label(root, text="", font=10)
    ch_text.place(x=50, y=300)

    ch_text.configure(text="안녕! 우리는 남원의 마스코트 춘향이와 이몽룡이야!!\n남원의 명소를 이야기해줄께!\n다음을 눌러봐.")
    ch = ImageTk.PhotoImage(Image.open("춘향이_이도령.png"))
    ch_label = Label(root, image=ch)
    ch_label.place(x=200, y=50)

    def btnnext():
        global count_trip
        btnnext_count()
        count_trip += 1

    next = Button(root, text="다음", width=10, height=2, command=btnnext)
    next.place(x=250, y=550)

    def btnnext_count():
        global count_trip, trip_image_label
        global trip_image, trip_image_label, trip_image1, trip_image_label1, trip_image2, trip_image_label2, trip_image3, trip_image_label3, trip_image4, trip_image_label4, next

        ch_label.destroy()

        if (count_trip == 0):
            choice()
            ch1()
            ch_text.configure(
                text="가장 먼저 소개할 곳은 광한루원이오! 우리나라 4대누각에 \n들정도로 아름다운 건축물이지!\n 광한루주변의 풍경또한 사계절과 잘 어울러져,\n아름다운 경치를 볼 수 있소!!")
            trip_image = ImageTk.PhotoImage(Image.open("광한루원1.jpg"))
            trip_image_label = Label(root, image=trip_image)
            trip_image_label.place(x=50, y=70)

        elif (count_trip == 1):
            choice1_0.destroy()
            choice2_0.destroy()
            choice3_0.destroy()

            choice1()
            trip_image_label.destroy()
            ch_text.configure(text="춘향테마파크는 춘향전을 테마로한 곳이오. \n다향한 체험과 고증이 잘 된 건물들을 볼수있소.\n")
            trip_image1 = ImageTk.PhotoImage(Image.open("춘향테마파크.png"))
            trip_image_label1 = Label(root, image=trip_image1)
            trip_image_label1.place(x=50, y=50)

        elif (count_trip == 2):
            choice1_1.destroy()
            choice2_1.destroy()
            choice3_1.destroy()

            ch2()
            choice2()
            trip_image_label1.destroy()
            ch_text.configure(text="봄의 팔랑치는 봄에 가장아름다운 산이고,\n따뜻한 기운을 받아 피워지는 철쭉이 군락을 지어 피어있어\n천상의 화원이 돼요.")
            trip_image2 = ImageTk.PhotoImage(Image.open("팔랑치.jpg"))
            trip_image_label2 = Label(root, image=trip_image2)
            trip_image_label2.place(x=50, y=70)

        elif (count_trip == 3):
            choice1_2.destroy()
            choice2_2.destroy()
            choice3_2.destroy()

            choice3()
            trip_image_label2.destroy()
            ch_text.configure(
                text="서도역은 우리나에서 가장 오래지어진 목조건물로 \n옛 청취를 느낄 수 있는 역입니다. \n철길의 양옆으로 푸르픈 초목이 길을 절경으로 보이게 합니다. ")
            trip_image3 = ImageTk.PhotoImage(Image.open("서도역.jpg"))
            trip_image_label3 = Label(root, image=trip_image3)
            trip_image_label3.place(x=50, y=50)

        elif (count_trip == 4):
            choice1_3.destroy()
            choice2_3.destroy()
            choice3_3.destroy()

            ch2_label.destroy()
            choice4()
            trip_image_label3.destroy()
            ch_text.configure(text="우리가 준비한 남원의 명소들 괜찮았어?\n")
            trip_image4 = ImageTk.PhotoImage(Image.open("춘향이_이도령.png"))
            trip_image_label4 = Label(root, image=trip_image4)
            trip_image_label4.place(x=200, y=70)

        elif (count_trip == 5):
            spwall_label.destroy()
            choice1_4.destroy()
            choice2_4.destroy()
            ch_text.destroy()
            trip_image_label4.destroy()
            next.destroy()
            exitbtn.destroy()


    def choice():
        global choice1_0, choice2_0, choice3_0, count_trip

        choice1_0 = Button(root, text="주변에 맛집은 뭐가있어?", width=82, height=2, command=choice_re)
        choice1_0.place(x=10, y=400)

        choice2_0 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_0.place(x=10, y=450)

        choice3_0 = Button(root, text="운영시간이나, 입장료는 어떻게 돼?", width=82, height=2, command=choice_re2)
        choice3_0.place(x=10, y=500)

    def choice1():
        global choice1_1, choice2_1, choice3_1, count_trip

        choice1_1 = Button(root, text="쉴 수 있는 카페가 있어?", width=82, height=2, command=choice_re)
        choice1_1.place(x=10, y=400)

        choice2_1 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_1.place(x=10, y=450)

        choice3_1 = Button(root, text="운영시간이나, 입장료는 어떻게 돼?", width=82, height=2, command=choice_re2)
        choice3_1.place(x=10, y=500)

    def choice2():
        global choice1_2, choice2_2, choice3_2, count_trip

        choice1_2 = Button(root, text="언제에 만개한 철쭉을 볼 수 있어?", width=82, height=2, command=choice_re)
        choice1_2.place(x=10, y=400)

        choice2_2 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_2.place(x=10, y=450)

        choice3_2 = Button(root, text="산 봉우리인데, 도착하기까지 얼마나걸려?", width=82, height=2, command=choice_re2)
        choice3_2.place(x=10, y=500)


    def choice3():
        global choice1_3, choice2_3, choice3_3, count_trip

        choice1_3 = Button(root, text="봄에 가면 뭐가 좋아?", width=82, height=2, command=choice_re)
        choice1_3.place(x=10, y=400)

        choice2_3 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_3.place(x=10, y=450)

        choice3_3 = Button(root, text="입장료가 있어?", width=82, height=2, command=choice_re2)
        choice3_3.place(x=10, y=500)

    def choice4():
        global choice1_4, choice2_4, choice3_4, count_trip

        choice1_4 = Button(root, text="고마워 너무 좋았어!", width=82, height=2, command=choice_re)
        choice1_4.place(x=10, y=400)

        choice2_4 = Button(root, text="좀 아쉬웠어.", width=82, height=2, command=choice_re1)
        choice2_4.place(x=10, y=450)

    def choice_re():
        if count_trip == 1:
            ch_text.configure(text="여행지에서 10분 이내로 도착하는 곳으로 추려봤다네.\n할매추어탕(추어탕)과 부산집(해물탕)의 음식이 일품이었네!")
        elif count_trip == 2:
            ch_text.configure(text="산들 다런이라는 전통카페가 다과가 먹기에도, 보기에도 맛이 좋다네!")
        elif count_trip == 3:
            ch_text.configure(text="5월초부터 점차 피기시작해,\n5월 중순에 가면 만개하는 철쭉의 군락을 볼 수 있어요")
        elif count_trip == 4:
            ch_text.configure(text="봄의 서도역은 피어나기 시작한 푸른 초목들이\n시원하게 이어진 기차길을 둘러싸고 있어,\n그 곳을 천천히 걸으면 따듯한 봄을 느낄 수 있어요.")
        elif count_trip == 5:
            ch_text.configure(text="정말로!?!?! 고마워 준비한 보람이 있었네!")

    def choice_re1():
        if count_trip == 1:
            ch_text.configure(text="관광안내소 바로 옆과 위쪽에 있네만, 유료라네.")
        elif count_trip == 2:
            ch_text.configure(text="주차장은 \"춘향교\"로 넘어오는 입구쪽에 있지.\n참고로 유료주차라네.")
        elif count_trip == 3:
            ch_text.configure(text="팔랑치는 따로 주차장이 마련되있지는 않아서 \n불편할 수 있어요.")
        elif count_trip == 4:
            ch_text.configure(text="무료주차장이 있지만, 다소 협소해요.")
        elif count_trip == 5:
            ch_text.configure(text="아쉽네. 다음번엔 우리가 더 많은 명소들을 찾아올께!!")

    def choice_re2():
        if count_trip == 1:
            ch_text.configure(text="운영시간은 8시~20시이고,\n입장료는 어른 3,000원 어린이 2,000원이오. 단체할인도 있으니 참고하게나.")
        elif count_trip == 2:
            ch_text.configure(text="운영시간은 09시~22시이고,\n입장료는 어른 3,000원 어린이 2,000원이오. 단체할인도 있으니 참고하세나.")
        elif count_trip == 3:
            ch_text.configure(text="가장 빠른 코스인 산덕마을-팔랑치-바래봉(원정회귀)를 타면,\n1시간 10분정도 걸려 만개한 철쭉의 절경을 볼 수 있어요!")
        elif count_trip == 4:
            ch_text.configure(text="입장료는 무료입장이에요!")
        elif count_trip == 5:
            ch_text.configure(text="")



    def ch1():
        global ch1, ch_label1, count_trip

        ch1 = ImageTk.PhotoImage(Image.open("이도령.png"))
        ch_label1 = Label(root, image=ch1)
        ch_label1.place(x=450, y=70)

    def ch2():
        global ch2, ch2_label, count_trip
        ch_label1.destroy()

        ch2 = ImageTk.PhotoImage(Image.open("춘향.jpg"))
        ch2_label = Label(root, image=ch2)
        ch2_label.place(x=450, y=70)

def Summer():
    global Mcount_trip, pwall_label, trip_image, trip_image_label, trip_image1, trip_image_label1, trip_image2, trip_image_label2, trip_image3, trip_image_label3, ch_label,ch, spwall, count_trip, next, trip_image4,trip_image_label4
    spwall = PhotoImage(file="summer1.png")
    spwall_label = Label(image=spwall)
    spwall_label.place(x = 0, y = 0)

    Mcount_trip = 0

    exitbtn = Button(root, text="종료", width=4, height=1, command=btnExit)
    exitbtn.place(x=558, y=15)

    def btnnext_count():
        global Mcount_trip, trip_image_label
        global trip_image, trip_image_label, trip_image1, trip_image_label1, trip_image2, trip_image_label2, trip_image3, trip_image_label3,trip_image4,trip_image_label4

        ch_label.destroy()

        if (Mcount_trip == 0):
            choice()
            ch1()
            ch_text.configure(text="가장 먼저 소개할 곳은 고창만돌갯벌체험마을이야!  \n 어류를 체험하고 천일염 체험을 직접 체험하며!\n 자연의 경이로움을 느낄 수 있는 곳이야!!")
            trip_image = ImageTk.PhotoImage(Image.open("고창만돌갯벌체험마을1.jpg"))
            trip_image_label = Label(root, image=trip_image)
            trip_image_label.place(x=20, y=30)

        elif (Mcount_trip == 1):
            choice1_0.destroy()
            choice2_0.destroy()
            choice3_0.destroy()

            choice1()
            trip_image_label.destroy()
            ch_text.configure(text="혜구 스님이 창건한 소래사 대한불교조계종 제24교구 본사인\n선운사(禪雲寺)의 말사이다.\n 절 일원이 전라북도 기념물 제78호로 지정되어 있다구!")
            trip_image2 = ImageTk.PhotoImage(Image.open("내소사.jfif"))
            trip_image_label2 = Label(root, image=trip_image2)
            trip_image_label2.place(x=20, y=30)


        elif (Mcount_trip == 2):
            choice1_1.destroy()
            choice2_1.destroy()
            choice3_1.destroy()

            choice2()
            trip_image_label2.destroy()
            ch_text.configure(text="군도로서 자연이 창조해 낸 수려한 경관을 자랑하는 천혜의 해상공원이다. \n바다낚시나 스킨스쿠버 등 레저 ·관광객들이 많이 찾는다구.\n")
            trip_image1 = ImageTk.PhotoImage(Image.open("고군산군도.jpg"))
            trip_image_label1 = Label(root, image=trip_image1)
            trip_image_label1.place(x=20, y=30)

        elif (Mcount_trip == 3):
            choice1_2.destroy()
            choice2_2.destroy()
            choice3_2.destroy()

            choice3()
            trip_image_label1.destroy()
            ch_text.configure(
                text="단군 이래 최대의 건설이라는 새만금간척사업은 총 공사 비용이 6조 원에 달한다\n 세계 최대의 방조제 건설 사업이다\n 자연을 지키는 소박한 마음을 담고 있는 해창 갯벌의 장승들도 함께 둘러보자구.")
            trip_image3 = ImageTk.PhotoImage(Image.open("새만금방조제.jpg"))
            trip_image_label3 = Label(root, image=trip_image3)
            trip_image_label3.place(x=20, y=30)

        elif (Mcount_trip == 4):
            choice1_3.destroy()
            choice2_3.destroy()
            choice3_3.destroy()

            ch_label1.destroy()
            choice4()
            trip_image_label3.destroy()
            ch_text.configure(text="내가 준비한 여름의 전라북도 명소들 괜찮았어?\n")
            trip_image4 = ImageTk.PhotoImage(Image.open("먹방이.png"))
            trip_image_label4 = Label(root, image=trip_image4)
            trip_image_label4.place(x=230, y=70)

        elif (Mcount_trip == 5):
            spwall_label.destroy()
            choice1_4.destroy()
            choice2_4.destroy()
            ch_text.destroy()
            trip_image_label4.destroy()
            next.destroy()
            exitbtn.destroy()

    def btnnext():
        global Mcount_trip
        btnnext_count()
        Mcount_trip += 1

    next = Button(root, text="다음", width=10, height=2, command=btnnext)
    next.place(x=250, y=550)

    def choice():
        global choice1_0, choice2_0, choice3_0

        choice1_0 = Button(root, text="주변에 맛집은 뭐가있어?", width=82, height=2, command=choice_re)
        choice1_0.place(x=10, y=400)

        choice2_0 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_0.place(x=10, y=450)

        choice3_0 = Button(root, text="입장료는 어떻게 돼?", width=82, height=2, command=choice_re2)
        choice3_0.place(x=10, y=500)

    def choice1():
        global choice1_1, choice2_1, choice3_1

        choice1_1 = Button(root, text="주변에 쉴수 있는 곳이 있어?", width=82, height=2, command=choice_re)
        choice1_1.place(x=10, y=400)

        choice2_1 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_1.place(x=10, y=450)

        choice3_1 = Button(root, text="운영시간이나, 입장료는 어떻게 돼?", width=82, height=2, command=choice_re2)
        choice3_1.place(x=10, y=500)


    def choice2():
        global choice1_2, choice2_2, choice3_2
        choice1_2 = Button(root, text="언제가야 바다의풍경을 볼수있어? ?", width=82, height=2, command=choice_re)
        choice1_2.place(x=10, y=400)

        choice2_2 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_2.place(x=10, y=450)

        choice3_2 = Button(root, text="코스는 어떤식으로가야하나??", width=82, height=2, command=choice_re2)
        choice3_2.place(x=10, y=500)

    def choice3():
        global choice1_3, choice2_3, choice3_3
        choice1_3 = Button(root, text="여름에 가면 뭐가 좋아?", width=82, height=2, command=choice_re)
        choice1_3.place(x=10, y=400)

        choice2_3 = Button(root, text="나는 차가있어.", width=82, height=2, command=choice_re1)
        choice2_3.place(x=10, y=450)

        choice3_3 = Button(root, text="입장료가 있어?", width=82, height=2, command=choice_re2)
        choice3_3.place(x=10, y=500)

    def choice4():
        global choice1_4, choice2_4
        choice1_4 = Button(root, text="덕분에 여름을 시원하게 보낼 것 같아!! 고마워!", width=82, height=2, command=choice_re)
        choice1_4.place(x=10, y=400)

        choice2_4 = Button(root, text="흠,, 부족한데 이정도도 충분한 것 같아! 고마워!!", width=82, height=2, command=choice_re1)
        choice2_4.place(x=10, y=450)

    def choice_re():
        if Mcount_trip == 1:
            ch_text.configure(text="여행지에서 10분 이내로 도착하는 곳으로 추려봤다구\n만돌큰손매운탕,해물탕과 만돌뻘집생선회 음식이 일품이었구만\n만돌풍천장어하와이집도,장어맛이 아주좋구만")
        elif Mcount_trip == 2:
            ch_text.configure(text="주차했던 선운산 근처에 호텔, 호스텔, 야영장이 있어! \n너가 원하는 곳에서 푹 쉬면 될거야")
        elif Mcount_trip == 3:
            ch_text.configure(text="고군산군도는 바다는 날짜 상관 없이 언제나 볼 수 있어!!")
        elif Mcount_trip == 4:
            ch_text.configure(text="더운 여름에 뻥 뚫린 바다 사이에서 시원한 바닷바람을 맞는거지!\n 상상만해도 시원하다~!")
        elif Mcount_trip == 5:
            ch_text.configure(text="정말 다행이다! 그럼 시원한 여름 여행 되길 바래!!")


    def choice_re1():
        if Mcount_trip == 1:
            ch_text.configure(text="주차장은 전북 고창군 심원면 애향갯벌로 320있다구 무료주차장이라구.")
        elif Mcount_trip == 2:
            ch_text.configure(text="선운사는 선운산 공영주차장에 주차해놓고 15분정도 걸어가야해!\n주차비는 2,000원이야!")
        elif Mcount_trip == 3:
            ch_text.configure(text="장자도 공영주차장에다가 주차하고 도보여행!!\n주차비는 기본1,000원에 15분당 300원씩이야!")
        elif Mcount_trip == 4:
            ch_text.configure(text="차가 있다면 아주 손쉽게 다니며 바다를 구경할 수 있을거야!\n여기는 차가 없으면 조금 힘들거든!")
        elif Mcount_trip == 5:
            ch_text.configure(text="미안해 다음에는 더 좋은 여행지를 소개하도록 노력할게!")

    def choice_re2():
        if Mcount_trip == 1:
            ch_text.configure(text=" 대인 12,000원/ 소인 8,000원/ 영유아 6,000원 가격여 여벌옷챙기면 좋다구!")
        elif Mcount_trip == 2:
            ch_text.configure(text="입장료는 어른 4,000원/ 청소년 3,000원/ 어린이 1,000원이라구! 참고하라구!.")
        elif Mcount_trip == 3:
            ch_text.configure(text="고창만돌갯벌체험마을-내소사-고군산군도-새만금방조제가 제일가까운코스야")
        elif Mcount_trip == 4:
            ch_text.configure(text="긴~ 방파제라 입장료를 받겠어? 당연히 없지!\n다만 차가 없으면 힘들거야")

    ch_text = Label(root, text="", font=10)
    ch_text.place(x=20, y=300)

    ch_text.configure(text="안녕! 나는 군산의 마스코트 먹방이야!!\n전라북도의 여름 여행지 명소를 소개해줄께!\n밑에 있는 다음을 눌러봐.")
    ch = ImageTk.PhotoImage(Image.open("먹방이.png"))
    ch_label = Label(root, image=ch)
    ch_label.place(x=230, y=50)

    def ch1():
        global ch1, ch_label1
        ch1 = ImageTk.PhotoImage(Image.open("먹방이.png"))
        ch_label1 = Label(root, image=ch1)
        ch_label1.place(x=430, y=70)

def Winter():
    global winterground, winter_label, btnquestion, exitbtn, winterchar_label, winterchar, Wtext1, Wchat1, Wchat2,Wchat3
    winterground = PhotoImage(file="Winter.png")
    winter_label = Label(image=winterground)
    winter_label.place(x = 0, y = 0)

    winterchar = PhotoImage(file = "Ttory.png")
    winterchar_label = Label (image = winterchar)
    winterchar_label.place(x = 360, y = 50)

    btnquestion = Button(root, text="다른곳 가보기", width=15, height=2, command=Winter_back)
    btnquestion.place(x=240, y=550)

    exitbtn = Button(root, text="종료", width=4, height=1, command=btnExit)
    exitbtn.place(x=558, y=15)


    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "안녕? 겨울 여행을 가고 싶구나!!! 나는 안내해줄 　　　반딧불이 또리야~\n우리 지금부터 전라북도 겨울 여행 떠나볼까?\n겨울여행 하면 생각나는거 있어?")

    Wtext1.place(x=20, y=290)
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')

    Wchat1 = Button(root, bg="#EAEAEA", text="와 너 정말 귀엽다! 모르겠어, 처음은 어디야??", height=2, width=82, command=Wstory11)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="겨울 하면 스키지! ", height=2, width=82, command=Wstory12)
    Wchat2.place(x=10, y=450)

def Wstory11():
    global Wtext1, Wchat1, Wchat2
    Wimgstory1()
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "겨울 하면 스키! 겨울에만 할 수 있는 스키가 먼저 떠오르지 않아? \n그래서 처음에 갈 곳은 무주 덕유산 리조트!!\n우리나라에서 제일 유명한 스키 리조트이지! ")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="스키! 나도 좋아하는건데 고마워!! 숙소는 어떻게 해야할까?", height=2, width=82, command=Wstory21)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="스키? 나 잘 못타는데 괜찮을까? ", height=2, width=82, command=Wstory22)
    Wchat2.place(x=10, y=450)

def Wstory12():
    global Wtext1, Wchat1, Wchat2
    Wimgstory1()
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "오~ 뭘 좀 아는데?? \n 그래서 처음에 갈 곳은 무주 덕유산 리조트!!\n 우리나라에서 제일 유명한 스키 리조트이지!")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="스키! 나도 좋아하는건데 고마워!! 숙소는 어떻게 해야할까?", height=2, width=82, command=Wstory21)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="스키? 나 잘 못타는데 괜찮을까? ", height=2, width=82, command=Wstory22)
    Wchat2.place(x=10, y=450)

def Wstory21():
    global Wtext1, Wchat1, Wchat2,a,  Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 3
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "걱정마! 리조트니까 안에 숙박시설은 물론! 찜질방이라든지 골프장, 식당까지 다있어!\n여기서 1박 2일동안 스키타고 놀면 돼!\n 밤에도 탈수있게 야간개장도 있다구~")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="그러면 잠이랑 밥은 문제 없겠다! 근데 내가 스키를 잘 못타는데 괜찮을까??", height=2, width=82, command=Wstory221)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="고마워! 그럼 다음날에는 어디로 갈까? ", height=2, width=82, command=Wstory31)
    Wchat2.place(x=10, y=450)

def Wstory211():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 3
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "걱정마! 리조트니까 안에 숙박시설은 물론! 찜질방이라든지 골프장, 식당까지 다있어!\n여기서 1박 2일동안 스키타고 놀면 돼!\n밤에도 탈수있게 야간개장도 있다구~")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="그러면 잠이랑 밥은 문제 없겠다! 고마워! 그럼 다음날엔 어디로 갈까?", height=2, width=82, command=Wstory31)
    Wchat1.place(x=10, y=400)


def Wstory22():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "걱정하지마! 초급자 코스부터 중급자, 상급자 코스별로 나뉘어져 있으니\n처음이면 초급자 코스부터 시작하면 돼!\n그리고 스키 장비도 대여할수 있단 말씀! 몸만 오면 된다고!!")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오~ 그러면 문제 없을것 같아 숙소는 어떻게 할까? ", height=2, width=82, command=Wstory211)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="고마워! 그럼 다음날에는 어디로 갈까? ", height=2, width=82, command=Wstory31)
    Wchat2.place(x=10, y=450)

def Wstory221():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "걱정하지마! 초급자 코스부터 중급자, 상급자 코스별로 나뉘어져 있으니\n처음이면 초급자 코스부터 시작하면 돼!\n그리고 스키 장비도 대여할수 있단 말씀! 몸만 오면 된다고!!")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="고마워! 이정도면 무주 리조트에서 재밌게 놀수 있을것 같아!! 내일은 어디 갈까? ", height=2, width=82, command=Wstory31)
    Wchat1.place(x=10, y=400)

def Wstory31():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wimage_label.destroy()

    a = 4
    Wimgstory1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "다음날엔 바로 덕유산 정상으로 가서 겨울 산을 구경하는 거야!!\n덕유산 등산코스는 바로 리조트에 이어져 있어서 손쉽게 코스로 갈수가 있어\n정상까지 3시간 내려오는데 2시간! 쉽지?")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="산 정상이라고..? 왕복 5시간? 전날에 스키타느라 온몸이 아픈데 어떻게 가..? ", height=2, width=82, command=Wstory32)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="등산? 문제없지!! 그런데 눈이 오는 날에는 올라가기 힘들지 않을까?", height=2, width=82, command=Wstory32)
    Wchat2.place(x=10, y=450)

def Wstory32():
    global Wtext1, Wchat1, Wchat2, Wchat3, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 6
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "하하핫 그럴줄 알았지~ 걱정하지마! 리조트 안에 곤도라 타고 바로 향적봉, 정상으로 갈수 있어! ")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="걱정했네! 고마워! 근데 공짜는 아닐것 같은데 타는데 얼마씩 할까? ", height=2, width=82, command=Wstory321)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="고마워! 갔다오고 나서 배가 고플것 같은데 주변에 맛집 있을까?", height=2, width=82, command=Wstory322)
    Wchat2.place(x=10, y=450)
    Wchat3 = Button(root, bg="#EAEAEA", text="고마워! 이제 다음은 어디로 갈까? ", height=2, width=82,command=WstoryAro)
    Wchat3.place(x=10, y=500)

def Wstory321():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wchat3.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "왕복권은 대인이 16,000원, 소인이 12,000원이고\n편도권은 대인 12,000원, 소인은 9,000원씩해!\n ")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="고마워! 갔다오고 나서 배가 고플것 같은데 주변에 맛집 있을까?", height=2, width=82,command=Wstory322)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="고마워! 이제 다음은 어디로 갈까?", height=2, width=82, command=WstoryAro)
    Wchat2.place(x=10, y=450)

def Wstory322():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wchat3.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 7
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "리조트 입구에 맛집들이랑 카페들이 뭉쳐있어!\n저중에서 '무주뚝배기'를 추천할게!! 추운날에 산까지 갔다왔는데, 뜨끈한 가마솥설렁탕 먹으면 온몸이 녹을꺼야!")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="고마워! 이제 다음은 어디로 갈까?", height=2, width=82, command=WstoryAro)
    Wchat1.place(x=10, y=400)

def WstoryAro():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size, winterchar_label,winterchar2
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wchat3.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()
    winterchar_label.destroy()

    winterchar2 = PhotoImage(file="Aro.png")
    winterchar_label = Label(image=winterchar2)
    winterchar_label.place(x=360, y=50)


    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "안녕! 나는 또리 친구 아로라고해~\n지금부터는 내가 소개해줄게!")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="안녕 아로야! 이제 어디로 가야할까??", height=2, width=82, command=Wstory41)
    Wchat1.place(x=10, y=400)

def Wstory41():
    global Wtext1, Wchat1, Wchat2, Wchat3, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wimage_label.destroy()

    a = 8
    Wimgstory1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "바로 무주 반디랜드로 가는거야!\n리조트에서 차로 20분 거리밖에 안돼!!\n그리고 여기서 나랑 또리가 반겨줄거야!!\n그리고 스키와 등산을 한 몸을 산책하며 쉴수 있지!!")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="반디랜드?? 뭐하는 곳이야?", height=2, width=82, command=Wstory42)
    Wchat1.place(x=10, y=400)

def Wstory42():
    global Wtext1, Wchat1, Wchat2,Wchat3, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "무주 반디랜드는 크게 곤충박물관, 천문과학관, 반딧불이 연구소, 통나무집, 물놀이장과 사계절 썰매장이 있어! 그중에 크게 곤충박물관하고 천문과학관, 겨울이니 썰매장을 알려줄게!\n입장료는 공짜지만 안에 있는곳에서 따로 입장료를 받아! ")

    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="곤충박물관을 가고싶어!", height=2, width=82, command=Wstory431)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="천문과학관을 알고싶어!!", height=2, width=82, command=Wstory432)
    Wchat2.place(x=10, y=450)
    Wchat3 = Button(root, bg="#EAEAEA", text="썰매장이 궁금해!! ", height=2, width=82, command=Wstory433)
    Wchat3.place(x=10, y=500)

def Wstory431():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wchat3.destroy()
    Wimage_label.destroy()

    a = 12
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "곤충박물관! 입장료는 성인 5,000원, 청소년은 4,000원, 어린이랑 노인분들은 3,000원이야!\n곤충박물관은 곤충들 뿐만 아니라 공룡들의 화석까지도 볼 수 있지!!\n또 3D입체영상실, 돔스크린 영상실로 곤충들을 애니메이션으로 볼 수 있어!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오! 정말 좋은 곳 같아! 천문과학관은 뭐하는 곳이야?", height=2, width=82, command=Wstory4311)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="오~ 썰매장은 어떻게 가?", height=2, width=82, command=Wstory4312)
    Wchat2.place(x=10, y=450)

def Wstory4311():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wimage_label.destroy()

    a = 18
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"천문과학관! 입장료는 성인 3,000원, 청소년이랑 노인분들은 2,000원, 어린이 1,000원!\n이 곳은 우주의 탄생, 역사, 태양계,별자리, 우주환경을 볼 수 있고 또 관측실로 별을 직접 볼 수 있어!!! 과학체험도 할 수 있다구")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오! 이제 썰매장은?", height=2, width=82, command=Wstory4312)
    Wchat1.place(x=10, y=400)

def Wstory4312():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 23
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0, "사계절 썰매장은 10:00~17:00에 운영되고 월요일에는 쉬어! 입장료는 성인 7,000원, 청소년 6,000원, 어린이 5,000원이야!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="여기는 이정도로 될 것 같아!! 다음은 어디로 갈까?", height=2, width=82, command=Wstory51)
    Wchat1.place(x=10, y=400)

def Wstory432():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wchat3.destroy()
    Wimage_label.destroy()

    a = 18
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"천문과학관! 입장료는 성인 3,000원, 청소년이랑 노인분들은 2,000원, 어린이 1,000원!\n이 곳은 우주의 탄생, 역사, 태양계,별자리, 우주환경을 볼 수 있고 또 관측실로 별을 직접 볼 수 있어!!! 과학체험도 할 수 있다구")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오! 정말 좋은 곳 같아! 곤충박물관은 어떤 곳이야?", height=2, width=82, command=Wstory4321)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="오~ 썰매장은 어떻게 가?", height=2, width=82, command=Wstory4312)
    Wchat2.place(x=10, y=450)

def Wstory4321():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wimage_label.destroy()

    a = 12
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"곤충박물관! 입장료는 성인 5,000원, 청소년은 4,000원, 어린이랑 노인분들은 3,000원이야!\n곤충박물관은 곤충들 뿐만 아니라 공룡들의 화석까지도 볼 수 있지!!\n또 3D입체영상실, 돔스크린 영상실로 곤충들을 애니메이션으로 볼 수 있어!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오! 이제 썰매장은?", height=2, width=82, command=Wstory4312)
    Wchat1.place(x=10, y=400)

def Wstory433():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wchat3.destroy()
    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 23
    WintertvImage1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"사계절 썰매장은 10:00~17:00에 운영되고 월요일에는 쉬어! 입장료는 성인 7,000원, 청소년 6,000원, 어린이 5,000원이야!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오! 재밌겠다! 이제 곤충박물관은 뭐하는 곳이야?", height=2, width=82, command=Wstory4331)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="오! 천문과학관은 어떤 곳이야??", height=2, width=82, command=Wstory4332)
    Wchat2.place(x=10, y=450)

def Wstory4331():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 12
    Wimgstory1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"곤충박물관! 입장료는 성인 5,000원, 청소년은 4,000원, 어린이랑 노인분들은 3,000원이야!\n곤충박물관은 곤충들 뿐만 아니라 공룡들의 화석까지도 볼 수 있지!!\n또 3D입체영상실, 돔스크린 영상실로 곤충들을 애니메이션으로 볼 수 있어!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="재밌겠는데? 천문과학관은 어떤 곳이야?", height=2, width=82, command=Wstory4332)
    Wchat1.place(x=10, y=400)

def Wstory4332():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()
    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 18
    Wimgstory1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"천문과학관! 입장료는 성인 3,000원, 청소년이랑 노인분들은 2,000원, 어린이 1,000원!\n이 곳은 우주의 탄생, 역사, 태양계,별자리, 우주환경을 볼 수 있고 또 관측실로 별을 직접 볼 수 있어!!! 과학체험도 할 수 있다구")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="여기는 이정도로 될 것 같아!! 다음은 어디로 갈까?", height=2, width=82, command=Wstory51)
    Wchat1.place(x=10, y=400)

def Wstory51():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 24
    Wimgstory1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"그 전에 배고프지 않아? 내가 센스있게 또 주변 맛집 하나 소개해줄게!\n카루시아단이라고 다음 목적지 가는 길에 있는데 돈까스가 끝내줘!!\n여기서 먹고 가면 좋을것 같아~")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="오! 맛있겠다! 고마워 아로야! 이거 먹고 어디 갈까?", height=2, width=82, command=Wstory61)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="배가 안고파서 안먹어도 될것같아 그래도 알려줘서 고마워!! 다음은 어디야?", height=2, width=82, command=Wstory61)
    Wchat2.place(x=10, y=450)

def Wstory61():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()

    a = 26
    Wimgstory1()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"이제 내가 소개해주는 마지막 장소야! 집 가는길에 들릴 수 있게 길 중간에 있는 곳이지!\n나제통문(라제통문)이라 하는 곳이야!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="나제통문? 문같은데 무슨 문인데??", height=2, width=82, command=Wstory62)
    Wchat1.place(x=10, y=400)
    Wchat2 = Button(root, bg="#EAEAEA", text="어어 많이 들었는데.. 그 삼국시대 무슨 문이였는데, 뭐더라? 알려줘 아로야!", height=2, width=82, command=Wstory62)
    Wchat2.place(x=10, y=450)

def Wstory62():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"삼국시대의 신라와 백제가 국경을 이루던 곳이야!! 또 삼국 통일전쟁 당시 김유신 장군이 드나들었다 해서 통일문이라고도 불리지! 나제통문 옆으로는 남대천이 흐르고 있으니 잠깐 서서 마지막 여유를 즐기고 가~~!!")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=20, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="고마워 아로야!! 덕분에 겨울여행 알차게 보낼수 있을 것 같아!!", height=2, width=82, command=Wstory71)
    Wchat1.place(x=10, y=400)

def Wstory71():
    global Wtext1, Wchat1, Wchat2, a, Wimage_label, Wimage_size, winterchar_label, winterchar3
    Wtext1.destroy()
    Wchat1.destroy()

    Wimage_label.destroy()
    Wnextbtn.destroy()
    Wbeforebtn.destroy()
    winterchar_label.destroy()

    winterchar3 = PhotoImage(file="AroTtory.png")
    winterchar_label = Label(image=winterchar3)
    winterchar_label.place(x=100, y=20)

    Wtext1 = Text(root, bg="#EAEAEA", height=6, width=47)
    Wtext1.insert(1.0,"여기까지 우리가 알려주는 전라북도 겨울여행 장소야!! 이걸 보고 알찬 겨울여행 됐으면 좋겠다!\n밑에 다른곳 가보기 누르면 다른 친구들이 알려주는 여행지가 있으니 꼭 알아봐바~~")
    Tfont = font.Font(family="Arial", size=10, weight="bold")
    Wtext1.configure(font=Tfont, state='disabled')
    Wtext1.place(x=150, y=290)

    Wchat1 = Button(root, bg="#EAEAEA", text="고마워 아로야, 또리야!! (게임으로 돌아가기)", height=2, width=82, command=Winter_back)
    Wchat1.place(x=10, y=400)

def Wimgstory1():
    global Wnextbtn, Wbeforebtn
    WintertvImage1()

    Wnextbtn = Button(root, text="다음", width=4, height=1, command=WImageNext)
    Wnextbtn.place(x=200, y=240)

    Wbeforebtn = Button(root, text="이전", width=4, height=1, command=WImageBefore)
    Wbeforebtn.place(x=100, y=240)

def WintertvImage1():
    global a, Wimage_label, Wimage_size

    if (a == 1):
        Wimages = Image.open("ski1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 2):
        Wimages = Image.open("ski2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 3):
        Wimages = Image.open("Whotel1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image=Wimage_size)
        Wimage_label.place(x=20, y=70)

    elif (a == 4):
        Wimages = Image.open("mountain1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 5):
        Wimages = Image.open("mountain2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 6):
        Wimages = Image.open("mountain3.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image=Wimage_size)
        Wimage_label.place(x=20, y=70)

    elif (a == 7):
        Wimages = Image.open("foodmap1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image=Wimage_size)
        Wimage_label.place(x=20, y=70)

    elif (a == 8):
        Wimages = Image.open("land1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 9):
        Wimages = Image.open("land2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 10):
        Wimages = Image.open("land3.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 11):
        Wimages = Image.open("land4.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 12):
        Wimages = Image.open("landinsect1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 13):
        Wimages = Image.open("landinsect2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 14):
        Wimages = Image.open("landinsect3.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 15):
        Wimages = Image.open("landinsect4.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 16):
        Wimages = Image.open("landinsect5.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 17):
        Wimages = Image.open("landinsect6.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 18):
        Wimages = Image.open("space1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 19):
        Wimages = Image.open("space2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 20):
        Wimages = Image.open("space3.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 21):
        Wimages = Image.open("space4.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 22):
        Wimages = Image.open("space5.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 23):
        Wimages = Image.open("snow1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image=Wimage_size)
        Wimage_label.place(x=20, y=70)

    elif (a == 24):
        Wimages = Image.open("food1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 25):
        Wimages = Image.open("food2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 26):
        Wimages = Image.open("door0.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 27):
        Wimages = Image.open("door1.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 28):
        Wimages = Image.open("door2.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)

    elif (a == 29):
        Wimages = Image.open("door3.png")
        Wimage_size = Wimages.resize((320, 200))
        Wimage_size = ImageTk.PhotoImage(Wimage_size)
        Wimage_label = Label(image = Wimage_size)
        Wimage_label.place(x = 25, y = 32)


def WImageNext():
    global a, Wimage_label
    a = a + 1

    if(a == 3):
        a = a - 1

    elif(a == 6):
        a = a - 1

    elif (a == 12):
        a = a - 1

    elif (a == 18):
        a = a - 1

    elif (a == 23):
        a = a - 1

    elif (a == 26):
        a = a - 1

    elif (a == 30):
        a = a - 1

    Wimage_label.destroy()
    WintertvImage1()

def WImageBefore():
    global a, Wimage_label
    a = a - 1

    if(a == 0):
        a = a + 1

    elif(a == 3):
        a = a + 1

    elif(a == 7):
        a = a + 1

    elif(a == 11):
        a = a + 1

    elif(a == 17):
        a = a + 1

    elif(a == 23):
        a = a + 1

    elif(a == 25):
        a = a + 1

    Wimage_label.destroy()
    WintertvImage1()

def Winter_back():
    global a
    a = 1
    winter_label.destroy()
    btnquestion.destroy()
    Wimage_label.destroy()
    exitbtn.destroy()
    Wbeforebtn.destroy()
    Wnextbtn.destroy()
    winterchar_label.destroy()
    Wtext1.destroy()
    Wchat1.destroy()
    Wchat2.destroy()

def btnExit():
    msgbox = tkinter.messagebox.askquestion('끄기','종료하시겠습니까?')
    if msgbox == 'yes':
        exit()

root = Tk()
root.title("전라북도 관광 홍보")
root.resizable(False,False)

root.geometry('600x600')

root.bind("<KeyRelease>", key_up)
root.bind("<KeyPress>", key_down)

back = PhotoImage(file ='background.png')
back_label = Label(image = back)
back_label.place(x = 0, y = 0)

exitbtn = Button(root, text = "종료", width = 4, height = 1, command = btnExit)
exitbtn.place(x = 558, y = 15)

btngame = Button(root, text="여행 떠나기", width=15, height=2, bg = "white", command = Game)
btngame.place(x=240, y=500)

root.mainloop()