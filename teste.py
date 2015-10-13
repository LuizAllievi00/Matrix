from __future__ import print_function

import __builtin__

class Test:
    def __init__(self):
        self.attr = "nothing"

    def print(self):
        __builtin__.print('attr:', self.attr)
test = Test()
print(test)
