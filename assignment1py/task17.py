import math
def odd_series(limit):
    total = 0
    for i in range(1, limit+1, 2):  
        total += (i ** 2) / math.factorial(i)
    return total
def even_series(limit):
    total = 0
    for i in range(2, limit+1, 2):  
        total += (i ** 2) / math.factorial(i)
    return total
n = 7
odd_sum = odd_series(n)
even_sum = even_series(n)
print(f"Sum of odd series up to {n} is: {odd_sum:.4f}")
print(f"Sum of even series up to {n} is: {even_sum:.4f}")
