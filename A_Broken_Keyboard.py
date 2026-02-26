t = int(input())

for _ in range(t):
    s = input().strip()
    working = set()
    le = 0
    ri = 0
    length = 0
    while ri < len(s):
        if s[le] == s[ri]:
            ri += 1
            length += 1
        else:
            if length % 2 == 1:
                working.add(s[le])

            length = 0
            le = ri

    if length % 2 == 1:
            working.add(s[le])

    print("".join(sorted(working)))