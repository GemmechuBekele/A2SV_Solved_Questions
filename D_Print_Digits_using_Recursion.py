t = int(input())
for _ in range(t):
    n = int(input())
    def prinNum(s):
        if s == "":
            return
        print(int(s[0]), end=" ")
        prinNum(s[1:])
    prinNum(str(n))
    print()
