def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n / n == 1 or n / 1 == n:
            print("Простое")
        else:
            print("Составное")
        return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)