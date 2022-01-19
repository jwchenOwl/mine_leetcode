class CQueue:

    def __init__(self):
        self.append_stack = []
        self.del_stack = []

    def appendTail(self, value: int) -> None:
        if not self.del_stack:
            self.append_stack.append(value)
        else:
            while self.del_stack:
                self.append_stack.append(self.del_stack.pop())
            self.append_stack.append(value)


    def deleteHead(self) -> int:
        if not self.append_stack and not self.del_stack:
            return -1
        if self.del_stack:
            return self.del_stack.pop()
        while self.append_stack:
            self.del_stack.append(self.append_stack.pop())

        ret = self.del_stack.pop()

        return ret
