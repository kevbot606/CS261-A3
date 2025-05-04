# Name: Kevin Coalwell
# OSU Email: coalwelk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A3 - Linked Lists, Stacks, Queues, & Deques
# Due Date: 5.5.25
# Description: SLL Queue Stack Implementation

from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a new element to the queue.
        """
        # Setting head to new node
        if self.is_empty():
            self._head = SLNode(value)
            self._tail = self._head
        # Capturing old tail and inserting new tail
        else:
            node = SLNode(value)
            old_tail = self._tail
            old_tail.next = node
            self._tail = node


    def dequeue(self) -> object:
        """
        Removes the first element from the queue.
        """
        # Checking if empty
        if self.is_empty():
            raise QueueException()
        # Capturing old head before removing
        else:
            old_head = self._head
            self._head = self._head.next
            return old_head.value

    def front(self) -> object:
        """
        Return the first element from the queue.
        """
        # Checking if empty
        if self.is_empty():
            raise QueueException()
        else:
            return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
