# Name: Kevin Coalwell
# OSU Email: coalwelk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A3 - Linked Lists, Stacks, Queues, & Deques
# Due Date: 5.5.25
# Description: Singly Linked List Implementation


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def get_at_index(self, index: int):
        """
        Returns the node at a specified index.
        """
        if index < 0 or index >= self.length():
            raise SLLException
        else:
            # Iterating until index, starting with first real node
            n = self._head.next
            for i in range(0, index):
                n = n.next
            return n

    def insert_front(self, value: object) -> None:
        """
        Inserts a new node at the beginning of the list.
        """
        # Getting current first node
        current_first = self._head.next
        # Creating new first node and pointing to old first
        new_first = SLNode(value, current_first)
        # Pointing sentinel to new_first
        self._head.next = new_first

    def insert_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list.
        """
        # Creating new node
        new_node = SLNode(value)
        # Starting at the head
        n = self._head
        while n is not None:
            # Checking if n is last node
            if n.next is None:
                break
            else:
                n = n.next
        # Setting last node to point to new last node
        n.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new node at a specified index.
        """
        # Verifying valid index
        if index < 0 or index > self.length():
            raise SLLException
        else:
            # Iterating until index
            n = self._head
            for i in range(0, index):
                n = n.next
            # Creating new node
            new_node = SLNode(value, n.next)
            n.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node at the specified index from the list.
        """

        if index < 0 or index >= self.length():
            raise SLLException
        else:
            # Iterating until index
            n = self._head
            for i in range(0, index):
                n = n.next
            # n is now node before the node we are removing. Skipping over node to remove.
            n.next = n.next.next

    def remove(self, value: object) -> bool:
        """
        Searches the list. Removes the first node that matches value and returns True, else returns False.
        """
        # Iterating through nodes

        # How to keep track of the previous node, once we find the one we want to remove?
        node = self.get_at_index(0)
        # Iterating up until we reach the last node, if necessary.
        while node.next is not None:
            if node.next.value == value:
                node.next = node.next.next
                return True
            else:
                node = node.next
        # Checking if last remaining node is what we want
        if node.value == value:
            self._head.next = None
            return True
        else:
            return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match provided value.
        """
        count = 0
        for i in range(0, self.length()):
            node = self.get_at_index(i)
            if node.value == value:
                count += 1
        return count

    def find(self, value: object) -> bool:
        """
        Returns a boolean based on if a given value is present in the list.
        """
        for i in range(0, self.length()):
            node = self.get_at_index(i)
            if node.value == value:
                return True
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns a new LinkedList with size number of nodes from the original list,
        beginning with start_index.
        """
        # Verifying valid start index
        if start_index < 0 or start_index >= self.length():
            raise SLLException
        elif start_index + size > self.length():
            raise SLLException
        else:
            # Creating new, empty LinkedList
            ll_slice = LinkedList()
            for i in range(start_index, start_index + size):
                ll_slice.insert_back(self.get_at_index(i).value)
            return ll_slice



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print("\n# insert_front example 1")
    # test_case = ["A", "B", "C"]
    # lst = LinkedList()
    # for case in test_case:
    #     lst.insert_front(case)
    #     print(lst)

    # print("\n# insert_back example 1")
    # test_case = ["C", "B", "A"]
    # lst = LinkedList()
    # for case in test_case:
    #     lst.insert_back(case)
    #     print(lst)
    #
    # print("\n# insert_at_index example 1")
    # lst = LinkedList()
    # test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    # for index, value in test_cases:
    #     print("Inserted", value, "at index", index, ": ", end="")
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    # print("\n# remove_at_index example 1")
    # lst = LinkedList([1, 2, 3, 4, 5, 6])
    # print(f"Initial LinkedList : {lst}")
    # for index in [0, 2, 0, 2, 2, -2]:
    #     print("Removed at index", index, ": ", end="")
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print("\n# remove example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [7, 3, 3, 3, 3]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# remove example 2")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# count example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    # print("\n# find example 1")
    # lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    # print(lst)
    # print(lst.find("Waldo"))
    # print(lst.find("Superman"))
    # print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
