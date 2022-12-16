# 14. LCM of Two Numbers

def lcm(a, b):
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

    return min(ans)


print(lcm(36, 24))
