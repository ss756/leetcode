'''
Problem Description: ALso called the Tower Of Brahma or Lucas Tower is a mathematical game or puzzle.
It consists of three rods and a number of disks of different sizes which can slide to any rod. The puzzle
starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus
making a conical shape.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1. Only one disk can be moved at one time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
or on an empty stack.

'''

class Solution:
    def towerofHanoi(self, n: int, src: str, dest: 'str', helper: 'str'):
        if n == 0:
            return
        self.towerofHanoi(n-1, src, helper, dest)
        print("Move {} disk from {} to {}".format(n, src, dest))
        self.towerofHanoi(n-1, helper, dest, src)
    def __init__(self):
        n = 3
        self.towerofHanoi(n, 'A', 'C', 'B')
Solution()
