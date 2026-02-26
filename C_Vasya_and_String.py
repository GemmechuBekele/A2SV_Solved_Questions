n, k = map(int, input().split())
s = input().strip()

a_target = "a"
b_target = "b"
a_count = 0
b_count = 0
change_made = 0
left = 0
for right in range(n):
    if s[right]!= a_target:
        change_made += 1

    while change_made > k:
        if s[left] != a_target:
            change_made -= 1
        left += 1
    a_count = max(a_count, right-left+1)

change_made = 0
left = 0
for right in range(n):
    if s[right]!= b_target:
        change_made += 1

    while change_made > k:
        if s[left] != b_target:
            change_made -= 1
        left += 1
    b_count = max(b_count, right-left+1)

print(max(a_count, b_count))