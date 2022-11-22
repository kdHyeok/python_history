import random
rps = ["X", '가위', '바위', '보'] # 가위, 바위, 보를 구분하는 변수
com_point = 0 #컴퓨터 점수
user_point = 0 #사용자 점수
play = int(input("|| 가위바위보 게임!! ||\n" #게임을 계속 진행할지 말지 구분해주는 변수
             "        [규칙]\n"
             "|  가위로 이기면 10점 |\n"
             "|  바위로 이기면 20점 |\n"
             "|  보로 이기면 30점  |\n"
             "-------------------\n"
             "게임을 시작하시겠습니까? "
             "\"시작(1)\",  \"종료(2)\" :"))
while(play == 1): # 반복 게임
    user = int(input("\n무엇을 내시겠습니까? \n 가위(1), 바위(2), 보(3)\n")) #사용자가 뭘 낼지 입력
    com = random.randint(1,3) # 컴퓨터가 뭘 낼지 랜덤으로 입력
    print('사용자: ' + rps[user] + ' VS  컴퓨터: ' + rps[com]) # 사용자와 컴퓨터가 무엇을 냈는지 확인

    #=========================================여기서부터 상황에 따른 컴퓨터와 사용자의 승패를 구분
    if(user==com):
        print('비겼습니다.')
    if (user == 1 and com == 2):
        print('졌습니다.')
        com_point += 20 #승패에 따른 점수 가산
    if (user == 2 and com == 3):
        print('졌습니다.')
        com_point += 30
    if (user == 3 and com == 1):
        print('졌습니다.')
        com_point += 10
    if (user == 1 and com == 3):
        print('이겼습니다.')
        user_point += 10
    if (user == 2 and com == 1):
        print('이겼습니다.')
        user_point += 20
    if (user == 3 and com == 2):
        print('이겼습니다.')
        user_point += 30
    #==========================================여기까지 승패 결정

    print('\n====================')
    print('사용자 점수: '+ str(user_point) )# 승패에 따른 점수 출력, int형의 값을 그대로 출력하지 못해서 점수를 str형으로 변경
    print('컴퓨터 점수: '+ str(com_point))
    print('====================\n')
    play = int(input("다시 하시겠습니까? \n \"시작(1)\",  \"종료(2)\" :")) #게임을 다시 할지 확인
#여기까지 반복 종료
# 종료를 선택 시 play 변수가 0이 되어 while문 종료
print('종료합니다.') #while문 종료 시 종료 알림