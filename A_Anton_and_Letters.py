letters = input().strip()
seen = set()
for ch in letters:
    if "a" <= ch <= "z":
        seen.add(ch)

print(len(seen))