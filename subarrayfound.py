# Read inputs
n = int(input())  # Length of the array
arr = list(map(int, input().split()))  # The array elements
k = int(input())  # The target sum

cumulative_sum = 0
cumulative_sum_map = {} 

found = False

for i in range(n):
    cumulative_sum += arr[i]
 
    if cumulative_sum == k:
        print(0, i)
        found = True
        break
    

    if (cumulative_sum - k) in cumulative_sum_map:
        print(cumulative_sum_map[cumulative_sum - k] + 1, i)
        found = True
        break
  
    cumulative_sum_map[cumulative_sum] = i

if not found:
    print("No subarray found")