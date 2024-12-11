def max_content_children(n, greed_factors, m, cookie_sizes):
    for i in range(n):
        for j in range(0, n-i-1):
            if greed_factors[j] > greed_factors[j+1]:
                greed_factors[j], greed_factors[j+1] = greed_factors[j+1], greed_factors[j]

    for i in range(m):
        for j in range(0, m-i-1):
            if cookie_sizes[j] > cookie_sizes[j+1]:
                cookie_sizes[j], cookie_sizes[j+1] = cookie_sizes[j+1], cookie_sizes[j]
    
    content_children = 0
    i = 0
    j = 0
    
    while i < n and j < m:
        if cookie_sizes[j] >= greed_factors[i]:
            content_children += 1
            i += 1
        j += 1
    
    return content_children

n = int(input("Enter the number of children (n): "))
greed_factors = []
print("Enter the greed factors (g): ")
for i in range(n):
    greed_factors.append(int(input()))

m = int(input("Enter the number of cookies (m): "))
cookie_sizes = []
print("Enter the cookie sizes (s): ")
for i in range(m):
    cookie_sizes.append(int(input()))

print(max_content_children(n, greed_factors, m, cookie_sizes))
