postfix = input().strip().split()
stack = []

for token in postfix:
    if token in "+-*/":
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(f"{token} {op1} {op2}")
    else:
        stack.append(token)

print(stack[0])