s = list(map(int, input().split()))

seen = set()
for num in s:
    if num not in seen:
        seen.add(num)

valera = 4 - len(seen)
print(valera)