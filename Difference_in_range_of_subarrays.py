# Read input values
N = int(input().strip())  # Read the size of the array
nums = list(map(int, input().strip().split()))  # Read the array elements

total_sum = 0

# Iterate over all possible subarrays
for i in range(N):
    min_val = nums[i]
    max_val = nums[i]
    for j in range(i, N):
        if nums[j] < min_val:
            min_val = nums[j]
        if nums[j] > max_val:
            max_val = nums[j]
        total_sum += (max_val - min_val)

print(total_sum)
