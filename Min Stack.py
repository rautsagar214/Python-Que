class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int):
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.main_stack:
            popped = self.main_stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
            return popped
        return None

    def get_min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None  # If there's no element in the stack

# Initialize the MinStack
s = MinStack()

# Take input
n = int(input())  # Number of queries
results = []

for _ in range(n):
    query = list(map(int, input().split()))
    
    if query[0] == 1:  # Push operation
        s.push(query[1])
    elif query[0] == 2:  # Pop operation
        popped_element = s.pop()
        if popped_element is not None:
            results.append(popped_element)
    elif query[0] == 3:  # Get minimum element
        results.append(s.get_min())

# Output results in a single line
print(" ".join(map(str, results)))
