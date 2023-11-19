
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def tailor(x, n):
    result = 0
    for i in range(n):
        result += x**i / factorial(i)
    return result


print(tailor(10,10))
# 10086.573192239859
