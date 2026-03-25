# a = int(input())
# b = int(input())
# m = int(input())
# print(pow(a, b))
# print(pow(a, b, m))

def power(n, e):
    if e == 0:
        return 1
    p = n*power(n, e-1)
    return p
print(power(5, 2))