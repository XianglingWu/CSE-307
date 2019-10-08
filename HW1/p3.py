

if __name__ == "__main__":
    line1 = input()
    line2 = input()
    valid = False

    escaped = True
    quote = ''

    if len(line1)>0:
        if line1[-1]=='\\':
            if line1[0]=='\"' or line1[0]=='\'':
                escaped = False
                quote = line1[0]
                i=1
                while i<len(line1)-1:
                    if not escaped:
                        if line1[i]=='\\':
                            escaped = True
                        elif line1[i]==quote:
                            escaped = True
                            break
                    else:
                        escaped = False
                    i+=1

    valid = not escaped
    if valid:
        valid = False

        i=0
        while i<len(line2)-1:
            if not escaped:
                if line2[i]=='\\':
                    escaped = True
                elif line2[i]==quote:
                    escaped = i!=len(line2)-1
                    break
            else:
                escaped = False
            i+=1
        if line2[i]==quote:
            valid = not escaped
        else:
            valid = False
    print(valid)