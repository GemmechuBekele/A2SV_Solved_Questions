t = int(input())

for _ in range(t):# 1A2B3B4A5A6B7B8A9A
    
    n = int(input())

    step = 1
    current_owner = "Alice"
    a = 0
    b = 0

    while n > 0: 
        give = min(n, step)

        if current_owner == "Alice":
            a+=give
        else:
            b+=give
        
        n -= give

        if step % 2 == 1:
            if current_owner == "Alice":
                current_owner = "Bob"
            else:
                current_owner = "Alice"
        step += 1
        

    print(a, b)