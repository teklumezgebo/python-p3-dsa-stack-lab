class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
       if len(self.items) == self.limit:
           return True
       else:
           return False

    def search(self, target):
        if target in self.items:
            if self.items[-1] == target:
                return 0
            else:
                targetIndex = self.items.index(target)
                lastElementIndex = self.items.index(self.items[-1])
                return lastElementIndex - targetIndex
        else:
            return -1
