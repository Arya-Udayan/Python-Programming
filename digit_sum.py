count = 0
total_sum = 0
for number in range(101,199):
    if number % 7 == 0:  
        count += 1
        total_sum += number
print("Number of integers divisible by 7:", count)
print("Sum of integers divisible by 7:", total_sum)
