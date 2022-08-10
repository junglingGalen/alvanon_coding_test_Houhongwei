"""
Implement a stack that accepts the following commands and performs the operations described:

push v: Push integer v onto the top of the stack
pop: Pop the top element from the stack
inc i v: Add v to each of the bottom i elements of the stack

After each operation, print the value at the top of the stack.
If the stack is empty, print the string 'EMPTY'.
"""


class Stack():

    def __init__(self):
        self.stack = []

    def print_stack(self):
        if self.stack:
            print(",".join(map(str, self.stack)))
        else:
            print("EMPTY")

    def execute_command(self, command: str, v=None, i=None):
        if command == "push":
            self.stack.append(v)
        if command == "pop":
            if self.stack:
                self.stack.pop()
        if command == "inc":
            if None in (v, i):
                raise Exception("params error")
            for i in range(i):
                self.stack[i] += v
        self.print_stack()
        return self.stack


if __name__ == '__main__':
    test_commands = [
        {"command": "push", "v": 3},
        {"command": "push", "v": 2},
        {"command": "pop"},
        {"command": "push", "v": 5},
        {"command": "push", "v": 6},
        {"command": "inc", "v": 3, "i": 2}
    ]
    s = Stack()
    for command in test_commands:
        s.execute_command(**command)
