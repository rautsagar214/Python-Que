class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, val: int):
        self.main_stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        if self.main_stack:
            popped = self.main_stack.pop()
            if popped == self.max_stack[-1]:
                self.max_stack.pop()
            return popped
        return None

    def get_max(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]
        return None  # If there's no element in the stack

# Initialize the MaxStack
s = MaxStack()

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
    elif query[0] == 3:  # Get maximum element
        results.append(s.get_max())

# Output results in a single line
print(" ".join(map(str, results)))
