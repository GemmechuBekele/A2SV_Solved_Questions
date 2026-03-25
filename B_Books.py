# n, t = map(int, input().split())
# a = list(map(int, input().split()))
# maxbook = 0
# le = 0
# tot = 0
# for ri in range(n):
#     tot += a[ri]

#     while tot > t:
#         tot -=a[le]
#         le += 1

#     maxbook= max(maxbook, ri-le+1)
# print(maxbook)
n, k = map(int, input().split())
seq = list(map(int, input().split()))

minute = 0
left = 0
current_minute = 0
for right in range(n):
    current_minute += seq[right]
    if current_minute < k:
        minute = max(minute, right - left +1)
    else:
        current_minute -= seq[left]
        left += 1
        minute = max(minute, right - left +1)
print(minute)