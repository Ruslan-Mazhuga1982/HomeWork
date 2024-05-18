def test_func(*params):
    print(params)
    print(type(params))


test_func(1, 2, 3, 4, 'urban', {'a': 1, 'b': 2, 'c': 3}, [10, 20, 30, 40])

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(6))

def factorial_1(n):
    if (n <= 1):
        return 1
    else:
        return (n * factorial_1(n-1))
n = int(input("Введите число:"))
print("Факториал числа равен:")
print(factorial_1(n))
factorial_1(n)