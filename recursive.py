# def powerFour(n):
#     if n == 1:
#         return True
#     if n < 1 or n % 4 != 0:
#         return False
#     return powerFour(n//4)
# po = powerFour(24)
# print(po)
# # power(64)
#factorial
# def factorial(n):
#     assert n>=0 and int(n)==n, "The number must be positive integer"
#     if n==0:
#         return 1
#     if n == 1:
#         return 1
    
#     facto = n*factorial(n-1)
#     return facto

# fac = factorial(-3)
# print(fac)
#fibonnacci number
# def f(n):
#     assert n>=0 and int(n)==n, "The number must be integer!"
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     fibo = f(n-1) + f(n-2)
#     return fibo
# fib = f(3.7)
# print(fib)