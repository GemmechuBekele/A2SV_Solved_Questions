t = int(input())

for _ in range(t):
    n =  int(input())
    red = list(map(int, input().split()))
    m =  int(input())
    blue = list(map(int, input().split()))

    prefix = 0
    for i in range(t):
        