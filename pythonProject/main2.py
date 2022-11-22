
#임의의 양의 정수 n에 대해  다음의 s(n)을 계산하는 함수를 작성하고, 이 함수를 이용하여

#n=1, 2, 3, 4, 5, 6,7, 8, 9, 10에 대한 계산결과를 출력하는 파이썬 프로그램을 작성하라.
#s(n) = 1 + (1*2) + (1*2*3) + (1*2*3*4) + .... + (1*2*3*...*n)

n={1,2,3,4,5,6,7,8,9,10}

def fecto(x):
    a=1
    for i in range(1,x+1):
        a *= i
    return a

def S(N):
    sum=0
    for i in N:
        sum += fecto(i)
        print(f"{i}! = {fecto(i)}  ",end='')
    print("\n\nS(n) = ",end='')
    for i in N:
        print(f"({fecto(i)})",end='')
        if i<len(N):
            print("+",end='')

    print(f" = {sum}")

S(n)