def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
all_numbers = list(range(1, 101))
even_numbers = [num for num in all_numbers if num % 2 == 0]
odd_numbers = [num for num in all_numbers if num % 2 != 0]
prime_numbers = [num for num in all_numbers if is_prime(num)]
divisible_by_4 = [num for num in even_numbers if num % 4 == 0]
divisible_by_6 = [num for num in even_numbers if num % 6 == 0]
divisible_by_8 = [num for num in even_numbers if num % 8 == 0]
divisible_by_10 = [num for num in even_numbers if num % 10 == 0]
divisible_by_3 = [num for num in all_numbers if num % 3 == 0]
divisible_by_5 = [num for num in all_numbers if num % 5 == 0]
divisible_by_7 = [num for num in all_numbers if num % 7 == 0]
divisible_by_9 = [num for num in all_numbers if num % 9 == 0]
print("Numbers divisible by 4:", divisible_by_4)
print("Numbers divisible by 6:", divisible_by_6)
print("Numbers divisible by 8:", divisible_by_8)
print("Numbers divisible by 10:", divisible_by_10)
print("Numbers divisible by 3:", divisible_by_3)
print("Numbers divisible by 5:", divisible_by_5)
print("Numbers divisible by 7:", divisible_by_7)
print("Numbers divisible by 9:", divisible_by_9)