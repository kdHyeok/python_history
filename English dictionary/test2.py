with open('vocabulary.txt', 'w', encoding='UTF-8') as vc:
    vc.write("")
with open('vocabulary.txt', 'r+', encoding='UTF-8') as vc:
    dict_exe = {"apple": "사과", "act": "행동하다", "fact": "사실", "can": "할수있다",
                "man": "남자", "cat": "고양이", "fat": "뚱뚱한", "hat": "모자",
                "camp": "캠프", "lamp": "램프", "stamp": "도장", "last": "마지막",
                "fast": "빠른", "bath": "목욕", "half": "절반", "and": "그리고",
                "band": "밴드", "hand": "손", "land": "땅", "sand": "모래",
                "stand": "서다", "bad": "나쁜", "dad": "아빠", "mad": "미친",
                "sad": "슬픈", "cap": "야구모자", "map": "지도", "ask": "질문하다",
                "gas": "가스", "pass": "지나가다", "glass": "유리", "bag": "가방",
                "candle": "양초", "candy": "사탕", "bank": "은행", "pants": "바지",
                "class": "학급", "dance": "춤추다", "plan": "계획하다", "plant": "식물",
                "handle": "손잡이", "happen": "발생하다", "happy": "행복한",
                "hamburger": "햄버거", "family": "가족", "back": "뒤로", "angry": "화난",
                "answer": "대답하다", "bed": "침대", "red": "빨간", "get": "얻다",
                "let": "시키다", "set": "놓다", "yet": "아직", "wet": "젖은", "hen": "수탉",
                "pen": "펜", "then": "그때"}
    enls, hwls = [], []
    vd = {}

    for i in vc:
        vls = i.strip().split(': ')
        hwls.append(vls[1])
        enls.append(vls[0])
        vd[vls[0]] = vls[1]


    for eng, hw in dict_exe.items():
        if eng not in enls and hw not in hwls:
            vc.write(f"{eng}: {hw}\n")

with open('vocabulary.txt', 'r+', encoding='UTF-8') as vc:
    enls, hwls = [], []
    vd = {}

    for i in vc:
        vls = i.strip().split(': ')
        hwls.append(vls[1])
        enls.append(vls[0])
        vd[vls[0]] = vls[1]

    print(hwls)
    print(enls)
    print('=====================================================================')
    print(vd)