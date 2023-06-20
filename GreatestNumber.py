nums = [4, 6700, 2, 320, 89, 3, 1, 890, 100]
greatest_number = nums[0]

for num in nums:
    if greatest_number < num:
        greatest_number = num

print(greatest_number)
