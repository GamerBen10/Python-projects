def fibonacci(n):
    # Return a list of the first n Fibonacci numbers

    fibbi = []
    a, b = 0, 1
    for _ in range(n):
        fibbi.append(a)
        a, b = b, a + b
    return(fibbi)

print(fibonacci(5))
print(fibonacci(1))
print(fibonacci(8))
