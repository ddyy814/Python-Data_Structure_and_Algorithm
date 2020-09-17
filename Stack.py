

# Stack

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):  # insert data
        self.stack.append(data)

    def pop(self):  # remove data
        data = self.stack[-1]   # index of the last item
        del self.stack[-1]
        return data

    def peek(self):  # return the last value without removing
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peek: ", stack.peek())
print(stack.sizeStack())