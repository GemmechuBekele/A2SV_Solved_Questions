k = int(input())
r = map(int, input().split())
def finalists(r):
    arr = list(r)
    maxRank = max(arr)
    if maxRank < 25:
        return 0
    decline = maxRank-25
    return decline
print(finalists(r))