name={}
score={}
rank={}
i=0
while True:
    valse=input('이름을 입력하세요: ')
    if (valse=='-1'):
        break;
    else:
        name[i]=valse
    valse=input('성적을 입력하세요')
    if (valse=='-1'):
        break;
    else:
        score[i]=int(valse)
        i += 1

for x in range(len(score)):
    rank_count = 1
    for y in range(len(score)):
        if (score[x]<score[y]):
            rank_count += 1
    rank[x]=rank_count

print('======================================')
for n in range(len(score)):
    print(f"이름: {name[n]} / 점수: {score[n]}점 / 석차: {rank[n]}등")
