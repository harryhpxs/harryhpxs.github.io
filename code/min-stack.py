class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.mainStack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.mainStack:
            top = self.mainStack.pop()
            if top == self.minStack[-1]：
                self.minStack.pop()

    def top(self) -> int:
        if self.mainStack:
            return self.mainStack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return None
