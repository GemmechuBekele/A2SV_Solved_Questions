username = input().strip()

seen = set()
for char in username:
    if char not in seen:
        seen.add(char)

count = len(seen)
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!" )