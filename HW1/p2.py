

def isFloat(num):
    if '.' in num:
        floatParts = num.split('.')
        if len(floatParts) == 2:
            if (floatParts[0].isdigit() or len(floatParts[0])==0) and floatParts[1].isdigit():
                return True
    return False


if __name__ == "__main__":
    numberType = 'none'
    num = input().lower()
    otherBase = 'bBoOxX'
    if len(num)==0:
        numberType = 'none'
    elif num.isdigit():
        if num[0]=='0' and len(num)!=1:
            numberType = 'none'
        else:
            numberType = 'int'
    elif num[0]=='0' and (num[1] in otherBase):
        if num[2:].isdigit():
            numberType = 'int'
    elif 'e' in num:
        expParts = num.split('e')
        if len(expParts)==2:
            if (isFloat(expParts[0]) or expParts[0].isdigit()):
                exp = ''
                if expParts[1][0]=='-':
                    exp = expParts[1][1:]
                else:
                    exp = expParts[1]
                if exp.isdigit():
                    numberType = 'float'
    elif '.' in num:
        if isFloat(num):
            numberType = 'float'
    print(numberType)