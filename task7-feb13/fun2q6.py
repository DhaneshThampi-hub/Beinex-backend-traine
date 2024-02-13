'''6.	Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
'''

fibonacci_series = lambda n: [0, 1] if n == 2 else fibonacci_series(n-1) + [fibonacci_series(n-1)[-1] + fibonacci_series(n-1)[-2]]
n = int(input("Enter a number (n) for Fibonacci series: "))
result = fibonacci_series(n)
print(f"Fibonacci series up to {n}:", result)