#multiplication of two numbers using two different function like input or assigning the number

def multiply_once(n, m):
    return n * m

def multiply_n_iterations(n, m):
    result = 0
    if n > 0:
        for i in range(n):
            result += m
    elif n < 0:
        for i in range(-n):
            result -= m
    return result

N = int(input("Enter N: "))
M = int(input("Enter M: "))

print("Multiply with 1 iteration:", multiply_once(N, M))
print("Multiply with N iterations:", multiply_n_iterations(N, M))
