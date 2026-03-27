def backtrack(i, position):
    global total, valid

    if i == len(s2):
        total += 1
        if position == target:
            valid += 1
        return
    if s2[i] == "+":
        backtrack(i+1, position+1)
    elif s2[i] == "-":
        backtrack(i+1, position-1)
    else:
        backtrack(i+1, position+1)
        backtrack(i+1, position-1)
backtrack(0, 0)
print(f"{valid/total:.12f}")