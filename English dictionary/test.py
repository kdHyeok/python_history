inFp = None
inList, inStr = [], ""
while(inFp.readline()!=""):
    inStr = inFp.readline()
    inList.append(inStr)

for i in range(3):
    inStr = inFp.readline()
    inList.append(inStr)
    print(i)

inFp = open("C:/Users/qaz00/OneDrive - 전주대학교/바탕 화면/data.txt", "r", encoding='utf-8')
