import random
war = open('Wrong_answer.txt', 'r+', encoding='UTF-8')
vc = open('vocabulary.txt', 'r+', encoding='UTF-8')
quiz_point = 0
quiz_count = 0

dict_exe = {}
for i in vc:
    vcls = i.strip().split(': ')
    dict_exe[vcls[0]] = vcls[1]
wa_dic = {}
for i in war:
    vls = i.strip().split(': ')
    wa_dic[vls[0]] = vls[1]

def reverse_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

def serch(dic, key):
    if key in dic:
        print(f"{key}의 뜻은 {dic[key]}입니다.")
    else:
        new_dic = reverse_dict(dic)
        if key in new_dic:
            print(f"{key}는 {new_dic[key]}입니다.")
        else:
            print("존재하지 않는 단어입니다.")


def random_quiz(dict, ox):
    dict_key = list(dict.keys())
    dict_value = list(dict.values())
    lee = int(len(dict_key)-1)
    num = random.randint(0, lee)
    print(dict_key[num])
    question = input("다음 뜻은? :")
    if ox == 1:
        global quiz_count
        quiz_count += 1
    if question == dict_value[num]:
        print("정답입니다.")
        if ox == 1:
            global quiz_point
            quiz_point += 1
            print(f"{quiz_count}문제 중 {quiz_point}문제를 맞추셨습니다.")

    else:
        print("틀렸습니다. 오답노트에 들어가니다.")
        print("정답은 " + dict_value[num] + "입니다.")
        global wa_dic
        if dict_key[num] not in wa_dic.keys() and dict_value[num] not in wa_dic.values():
            war.write(f"{dict_key[num]}: {dict_value[num]}\n")
        wa_dic[dict_key[num]] = dict_value[num]

        print(wa_dic)

while True:
    print("=============")
    print("1. 단어 검색")
    print("2. ")
    print("3. 단어 퀴즈")
    print("4. 오답 시험")
    print("5. 종료")
    print("=============")
    ch = int(input("무엇을 하시겠습니까? :"))
    if ch == 1:
        while True:
            ss = input("무엇을 검색하시겠습니까? :")
            serch(dict_exe, ss)
            retry = int(input("다시 하시겠습니까? (1. Yes, 2. No)"))
            if retry == 2:
                break

    elif ch == 3:
        print("랜덤퀴즈를 시작합니다.\n")
        while True:
            random_quiz(dict_exe, 1)
            retry = int(input("다시 하시겠습니까? (1. Yes, 2. No)"))
            if retry == 2:
                break
    elif ch == 4:
        print("오답 퀴즈를 시작합니다.\n")
        while True:
            print(wa_dic)
            random_quiz(wa_dic, 0)
            retry = int(input("다시 하시겠습니까? (1. Yes, 2. No)"))
            if retry == 2:
                break
    elif ch == 5:
        break
