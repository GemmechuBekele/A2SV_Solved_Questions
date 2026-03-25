n = int(input())
s = input().strip()

unique_char = set(s)
distinct_char_len = len(unique_char)
count = {}
left = 0
min_length = float("inf")
formed = 0

for right in range(n):
    char = s[right]
    count[char] = count.get(char, 0)+1

    if count[char] == 1:
        formed += 1

    while formed == distinct_char_len:
        min_length = min(min_length, right - left + 1)
        count[s[left]] -= 1

        if count[s[left]]  == 0:
            formed -= 1
            
        left += 1

print(min_length)