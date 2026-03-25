n, k = map(int, input().split())
s = input().strip()

def birthdayCake(s):
    weight = 0
    count = 0
    first = None
    s = sorted(s)
    for i in s:
        if first is None:
            #pick the first char
            first = i
            char = ord(first)-ord("a")+1
            weight += char
            count += 1
        elif ord(i) >= ord(first)+2:
            #pick next char
            first = i
            char = ord(first)-ord("a")+1
            weight += char
            count += 1
            
        if count == k:
            return weight
    return -1
print(birthdayCake(s))