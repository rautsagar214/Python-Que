num = input().strip()
k = int(input().strip())

stack = []

for digit in num:
    while stack and k > 0 and stack[-1] > digit:
        stack.pop()
        k -= 1
    stack.append(digit)

final_stack = stack[:-k] if k else stack
result = ''.join(final_stack).lstrip('0')
print(result if result else '0')
