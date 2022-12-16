# 15. GCD of Two Numbers

def gcd(a, b):
    ans = []
    gcd = 1

    n = 2
    while n < a and n < b:
        if a % n == 0 and b % n == 0:
            a = a / n
            b = b / n
            ans.append(n)
        else:
            n = n + 1

    for i in ans:
        gcd = gcd * i
    return gcd


print(gcd(7, 11))
