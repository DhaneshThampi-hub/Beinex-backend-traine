start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
even_sum = 0
for number in range(start, end + 1):
    if number % 2 == 0:
        even_sum += number
print(f"The sum of even numbers between {start} and {end} is: {even_sum}")