def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_numbers(prime):
    numbers = []
    digits = list(str(prime))
    for i in range(4):
        original_digit = digits[i]
        for j in range(10):
            if j != int(original_digit):
                digits[i] = str(j)
                new_num = int("".join(digits))
                if is_prime(new_num):
                    numbers.append(new_num)
        digits[i] = original_digit
    return numbers

# Example usage
prime_number = 1033
result = generate_numbers(prime_number)
print(result)
