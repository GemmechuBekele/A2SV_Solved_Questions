n = int(input())

words = input().strip()
seen = set()
for ch in words:
    if ch not in seen:
        seen.add(ch.capitalize())

if len(seen) == 26:
    print("YES")
else:
    print("NO")