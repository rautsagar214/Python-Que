postfix = input().strip().split()
stack = []

for token in postfix:
    if token in "+-*/":
        op2 = stack.pop()
        op1 = stack.pop()
        # Construct infix expression
        infix_expr = f"({op1} {token} {op2})"
        stack.append(infix_expr)
    else:
        stack.append(token)

# At the end, stack will contain the final infix expression
print(stack[0])