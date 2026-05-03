t=int(input())
for _ in range(t):
    n = int(input())

    if n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        if n >= 4 and n%2 == 0:
            print(0)
        elif n >= 4 and n % 2 == 1:
            print(1)