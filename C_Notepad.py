t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    seen = {}
    found = False

    for i in range(n-1):
        sub_string = s[i:i+2]

        if sub_string in seen:
            if i - seen[sub_string] >= 2:
                found= True
                break
        else:
            seen[sub_string] = i

    print("YES" if found else "NO")
