def is_prime(func):
    def wrapper(*args):
        summa = func(*args)
        rez = [True for i in range(2, summa - 1) if summa % i == 0]
        if(len(rez) == 0): print("Простое")
        else: print("Составное")
        return summa
    return wrapper

@is_prime
def sum_three(*n):
    return sum(n)


result = sum_three(2, 3, 6)
print(result)