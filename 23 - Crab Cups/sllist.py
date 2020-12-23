class Node:
    """
    """
    __slots__ = ('data', 'next')


    def __init__(self, data=None, next=None):
        """
        """
        self.data = data
        self.next = next if next is not None else self


    def append(self, data):
        """
        """
        self.next = Node(data, self.next)

        return self.next


    def remove_trio(self):
        """
        """
        trio = self.next
        self.next = self.next.next.next.next
        trio.next.next.next = None

        return trio


    def reinsert_trio(self, trio):
        """
        """
        tail = self.next
        self.next = trio
        trio.next.next.next = tail

        return self


    def find(self, value: int):
        """
        """
        here = self
        while here.data != value:
            here = here.next
            #assert self != here

        return here



def make_circular_list(iterable) -> Node:
    """
    """
    iterable = iter(iterable)
    first = Node(next(iterable))
    node = first
    for data in iterable:
        node = node.append(data)

    return first



class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None) # this is the sentinel node!
        self.head.next = self.head   # link it to itself


    def add(self, data):             # no special case code needed for an empty list
        self.head.next = Node(data, self.head.next)


    def extend(self, iterable):
        for data in iterable:
            self.add(data)


    def __contains__(self, data):    # example algorithm, implements the "in" operator
        current = self.head.next
        while current != self.head:
            if current.data == data: # element found
                return True
            current = current.next
        return False
