def rabbit_pairs(k, n):
    f1, f2 = 1, 1
    for _ in range(n - 2):
        f1, f2 = f2, f2 + k * f1
    return f2

res = rabbit_pairs(4, 31)
print(res)