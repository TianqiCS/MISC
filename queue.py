# Data Structure Collection -- queue
# A queue follows the FIFO rule, the first item in a queue is the first one to be dequeued.
# To initialize a queue: Queue()
# To enqueue an item in the queue: %queue.enqueue(item)
# To dequeue an item out of queue: %queue.dequeue()
# To check if your queue is empty: %queue.is_empty() RETURN VALUE -> BOOL
# To get the size of a queue: %queue.size() RETURN VALUE -> INT
# To add a queue to another use +
# To compare to queue use ==
# To print out a queue use print(str(%queue)) or simply print(%queue)


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def __eq__(self, other):
        equal = False
        if self.size() == other.size():  # check the size of two queues, if the size is different, they are not equal
            for i in range(self.size()):
                if self.__items[i] == other.__items[i]:  # compare items until finding difference or being identical
                    equal = True
                else:
                    return False
        return equal

    def __add__(self, other):
        new_queue = Queue()
        new_queue.__items = self.__items + other.__items
        return new_queue

    def __str__(self):
        return str(self.__items)


def test_is_empty(queue):
    if queue.is_empty():
        print('empty.')
    else:
        print('not empty')


def test():
    test1 = Queue()
    test1.enqueue(1)
    test1.enqueue('hello')
    print('We have enqueued two items in our queue which is int 1 and str hello.')
    print('The test result should be FIFO, the first dequeued item is', test1.dequeue())
    print('And the queue size is', test1.size(), end=' ')
    print('which is', end=' ')
    test_is_empty(test1)
    print('Then the second dequeued item is', test1.dequeue())
    print('And the queue size is', test1.size(), end=' ')
    print('which is', end=' ')
    test_is_empty(test1)
    test2 = Queue()  # test2 = <-1,2<-
    test2.enqueue(1)
    test2.enqueue(2)
    test3 = Queue()  # test3 = <-1,2<-
    test3.enqueue(1)
    test3.enqueue(2)
    test4 = Queue()  # test4 = <-1<-
    test4.enqueue(1)
    if test2 == test3 and test4 != test2:
        print('We created three more queues which two are identical [1,2] and one is different [1]')
    print('The content in the different one is', str(test4))
    print('Then content of the two identical ones combined is', test2 + test3)


test()

