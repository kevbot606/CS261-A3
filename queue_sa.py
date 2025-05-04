# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


# Note: Changing any part of the pre-implemented methods (besides adding  #
#       default parameters) will cause the Gradescope tests to fail.      #


from static_array import StaticArray, StaticArrayException


class QueueException(Exception):
    """
    Custom exception to be used by Queue class.
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        size = self._current_size
        out = "QUEUE: " + str(size) + " elements. ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty, False otherwise.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def print_underlying_sa(self) -> None:
        """
        Print underlying StaticArray. Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(self._sa)

    def _increment(self, index: int) -> int:
        """
        Move index to next position.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # ---------------------------------------------------------------------- #

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end/back of the queue.
        """
        # Checking if enough room
        if self._current_size >= self._sa.length():
            self.resize_up()

        # Incrementing _back
        self._back = self._increment(self._back)

        # Adding element
        self._sa.set(self._back, value)

        # Incrementing size
        self._current_size += 1

    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        Removes and returns the element at the front of the queue.
        """
        # Checking if empty
        if self.is_empty():
            raise QueueException()
        else:
            elem = self._sa.get(self._front)

            # Incrementing front
            self._front = self._increment(self._front)

            # Updating size
            self._current_size -= 1

            return elem

    def front(self) -> object:
        """
        TODO: Write this implementation
        """
        pass

    def resize_up(self):
        """Resizes up the StaticArray and reindexes elements."""
        new_sa = StaticArray(self._sa.length()*2)
        old_index = self._front
        for new_index in range(self._current_size):
            new_sa[new_index] = self._sa[old_index]
            old_index = self._increment(old_index)
        self._sa = new_sa
        self._front = 0
        self._back = self._current_size - 1


    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # # My Testing ------------------------------
    # print("My Own Testing")
    # q = Queue()
    # print(q)
    # for value in range(6):
    #     q.enqueue(value)
    #     print(f"Front: {q._back} Back {q._back}")
    #     print(q)
    #     print(q._sa)
    # for value in range(3):
    #     q.dequeue()
    #     print(f"Front: {q._back} Back {q._back}")
    #     print(q)
    #     print(q._sa)
    # for value in range(6, 12):
    #     q.enqueue(value)
    #     print(f"Front: {q._back} Back {q._back}")
    #     print(q)
    #     print(q._sa)



    print("\n# Basic functionality tests #")
    print("\n# enqueue()")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue()")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for _ in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)
    q.print_underlying_sa()

    # print("\n# front()")
    # q = Queue()
    # print(q)
    # for value in ['A', 'B', 'C', 'D']:
    #     try:
    #         print(q.front())
    #     except Exception as e:
    #         print("No elements in queue", type(e))
    #     q.enqueue(value)
    # print(q)
    #
    # print("\n# Circular buffer tests: #\n")
    #
    # def action_and_print(
    #         header: str, action: callable, values: [], queue: Queue) -> None:
    #     """
    #     Print header, perform action,
    #     then print queue and its underlying storage.
    #     """
    #     print(header)
    #     if values:
    #         for value in values:
    #             action(value)
    #     else:
    #         action()
    #     print(queue)
    #     queue.print_underlying_sa()
    #     print()
    #
    # q = Queue()
    #
    # # action_and_print("# Enqueue: 2, 4, 6, 8", q.enqueue, [2, 4, 6, 8], q)
    #
    # # Calling the action_and_print() function declared two lines above,
    # # would be equivalent to following lines of code:
    # print("# Enqueue: 2, 4, 6, 8")
    # test_case = [2, 4, 6, 8]
    # for value in test_case:
    #     q.enqueue(value)
    # print(q)
    # q.print_underlying_sa()
    # print()
    #
    # action_and_print("# Dequeue a value", q.dequeue, [], q)
    # action_and_print("# Enqueue: 10", q.enqueue, [10], q)
    # action_and_print("# Enqueue: 12", q.enqueue, [12], q)
    #
    # print("# Dequeue until empty")
    # while not q.is_empty():
    #     q.dequeue()
    # print(q)
    # q.print_underlying_sa()
    # print()
    #
    # action_and_print("# Enqueue: 14, 16, 18", q.enqueue, [14, 16, 18], q)
    # action_and_print("# Enqueue: 20", q.enqueue, [20], q)
    # action_and_print("# Enqueue: 22, 24, 26, 28", q.enqueue,
    #                  [22, 24, 26, 28], q)
    # action_and_print("# Enqueue: 30", q.enqueue, [30], q)
