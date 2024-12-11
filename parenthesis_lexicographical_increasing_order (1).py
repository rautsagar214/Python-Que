N = int(input())
result = []
stack = [("", 0, 0)]

while stack:
    curr, open_count, close_count = stack.pop()
    if open_count == N and close_count == N:
        result.append(curr)
    if open_count < N:
        stack.append((curr + "(", open_count + 1, close_count))
    if close_count < open_count:
        stack.append((curr + ")", open_count, close_count + 1))

result.sort()
for comb in result:
    print(comb,end=" ")