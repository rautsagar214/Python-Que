n = int(input())
black_section = list(map(int, input().split()))

# Initialize variables
water_trapped = 0

# Create arrays to store the maximum height to the left and right of each bar
left_max = [0] * n
right_max = [0] * n

# Fill left_max array
left_max[0] = black_section[0]
for i in range(1, n):
    if black_section[i] > left_max[i - 1]:
        left_max[i] = black_section[i]
    else:
        left_max[i] = left_max[i - 1]

# Fill right_max array
right_max[n - 1] = black_section[n - 1]
for i in range(n - 2, -1, -1):
    if black_section[i] > right_max[i + 1]: 
        right_max[i] = black_section[i]
    else:
        right_max[i] = right_max[i + 1]

# Calculate the water trapped
for i in range(n):
    water_trapped += min(left_max[i], right_max[i]) - black_section[i]

print(water_trapped)
