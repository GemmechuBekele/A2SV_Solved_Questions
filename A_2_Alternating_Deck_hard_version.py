t = int(input())

for _ in range(t):
    
    n = int(input())

    step = 1
    is_A = True
    wa = 0
    ba = 0
    wb = 0
    bb = 0
    position = 0

    while n > 0: 
        give = min(n, step)

        if position % 2 == 0:
            white = (give +1)//2
            black = (give)//2
        else:
            white = (give)//2
            black = (give + 1)//2
        if is_A:
            wa+=white
            ba += black
        else:
            wb+=white
            bb += black

        position += give
        n-=give

        if step % 2 == 1:
            is_A = not is_A

        step += 1

    print(wa, ba, wb, bb)