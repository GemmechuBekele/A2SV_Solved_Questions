n = int(input())

nums = list(map(int, input().split()))

sereja = 0
dima = 0

left = 0
right = n-1
turn = True
while left <= right:
    if nums[left] > nums[right]:
        pick = nums[left]
        left += 1
    else:
        pick = nums[right]
        right -= 1

    if turn:
        sereja += pick
    else:
        dima += pick

    turn = not turn

print(sereja, dima)
