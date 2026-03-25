t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ops = []
    
    for value in range(1, 2*n + 1):
        
        if value <= n:
            target_row = 'a'
            target_pos = value - 1
        else:
            target_row = 'b'
            target_pos = value - n - 1
        
        # Find value
        found = False
        for i in range(n):
            if a[i] == value:
                row = 'a'
                pos = i
                found = True
                break
            if b[i] == value:
                row = 'b'
                pos = i
                found = True
                break
        
        # If wrong row, swap vertically
        if row != target_row:
            ops.append((3, pos + 1))
            a[pos], b[pos] = b[pos], a[pos]
            row = target_row
        
        # Move to correct position
        if row == 'a':
            while pos > target_pos:
                a[pos], a[pos-1] = a[pos-1], a[pos]
                ops.append((1, pos))
                pos -= 1
            while pos < target_pos:
                a[pos], a[pos+1] = a[pos+1], a[pos]
                ops.append((1, pos+1))
                pos += 1
        else:
            while pos > target_pos:
                b[pos], b[pos-1] = b[pos-1], b[pos]
                ops.append((2, pos))
                pos -= 1
            while pos < target_pos:
                b[pos], b[pos+1] = b[pos+1], b[pos]
                ops.append((2, pos+1))
                pos += 1
    
    print(len(ops))
    for op in ops:
        print(op[0], op[1])