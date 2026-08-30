def sigma(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

print(5," ",sigma(5))