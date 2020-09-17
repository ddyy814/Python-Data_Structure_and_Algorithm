# Arrays
numbers = [1,2,300,4,5];

# random indexing --> O(1) get items if we know the index!!
# print(numbers[4])

# numbers[1] = 'Dylan';
# print(numbers[1])

# for i in range(len(numbers)):
#     print(numbers[i])

# print(numbers[:-2])


# O(n) searching time complexity
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num;

print(maximum)