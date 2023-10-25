#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    i = 1
    while i < 3:
        if i > a:
            raise Exception('Too far')
        result += (a ** b) / i
        i += 1

    result += a + b
    return result

# Test cases
result1 = magic_calculation(1, 2)
print(result1)

result2 = magic_calculation(1, 4)
print(result2)

result3 = magic_calculation(4, 1)
print(result3)

result4 = magic_calculation(3, 3)
print(result4)

result5 = magic_calculation(1, 1)
print(result5)
