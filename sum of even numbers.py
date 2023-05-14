def sum_of_even_numbers(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum

n = int(input())
print("Sum of even numbers from 2 to", n, ":", sum_of_even_numbers(n))
