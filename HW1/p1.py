import keyword

if __name__ == "__main__":
    keywordList = []
    for k in keyword.kwlist:
        keywordList.append(k)

    valid = True
    i = input()
    if len(i)==0:
        print('False')
    elif i in keywordList:
        print('False')
    elif i[0]!='_' and not i[0].isalpha():
        print('False')
    else:
        for ch in i[1:]:
            if not ch.isalpha() and not ch.isdigit() and ch!='_':
                valid = False
                break
        print(valid)
