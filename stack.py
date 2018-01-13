# Data Structure Collection -- Stack
# A stack follows the LIFO rule, the last item in a stack is the first one to be pushed out.
# To initialize a stack: Stack()
# To push an item in the stack: %stack.push(item)
# To pop an item out of stack: %stack.pop()
# To check if your stack is empty: %stack.is_empty() RETURN VALUE -> BOOL
# To get the size of a stack: %stack.size() RETURN VALUE -> INT
# To add a stack to another use +
# To compare to stacks use =
# To print out a stack use print(str(%stack)) or simply print(%stack)


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def __eq__(self, other):
        equal = False
        if self.size() == other.size():  # check the size of two stacks, if the size is different, they are not equal
            for i in range(self.size()):
                if self.__items[i] == other.__items[i]:  # compare items until finding difference or being identical
                    equal = True
                else:
                    return False
        return equal

    def __add__(self, other):
        new_stack = Stack()
        new_stack.__items = self.__items + other.__items
        return new_stack

    def __str__(self):
        return str(self.__items)


def test_is_empty(stack):
    if stack.is_empty():
        print('empty.')
    else:
        print('not empty')


def test():
    test1 = Stack()
    test1.push(1)
    test1.push('hello')
    print('We have pushed two items in our stack which is int 1 and str hello.')
    print('The test result should be LIFO, the first popped item is', test1.pop())
    print('And the stack size is', test1.size(), end=' ')
    print('which is', end=' ')
    test_is_empty(test1)
    print('Then the second popped item is', test1.pop())
    print('And the stack size is', test1.size(), end=' ')
    print('which is', end=' ')
    test_is_empty(test1)
    test2 = Stack()  # test2 = |1,2->
    test2.push(1)
    test2.push(2)
    test3 = Stack()  # test3 = |1,2->
    test3.push(1)
    test3.push(2)
    test4 = Stack()  # test4 = |1->
    test4.push(1)
    if test2 == test3 and test4 != test2:
        print('We created three more stacks which two are identical [1,2] and one is different [1]')
    print('The content in the different one is', str(test4))
    print('Then content of the two identical ones combined is', test2 + test3)


test()

