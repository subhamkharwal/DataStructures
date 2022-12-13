# Extends the Linked List class to implement the Python List utilities
from linked_list import LinkedList, Node


class MyList(LinkedList):
    # Constructor inherited from LinkedList
    def __init__(self, value):
        super().__init__(value)

    # Implement Append method - O(1)
    def append(self, value):
        node = Node(value)
        # Validate if list is empty
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    # Implement Prepend method - O(1)
    def prepend(self, value):
        node = Node(value)
        # Validate if list is empty
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            node.next = temp
            self.head = node
        self.length += 1

    # Implement get method to get the element at given index - O(n)
    def get(self, index):
        # Validate index
        if index >= self.length or index < 0:
            return None
        # Validate if list is empty
        if self.head is None:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    # Implement pop method to get the last element in List - O(n)
    def pop(self):
        # If list is empty
        if self.length == 0:
            return None
        # If list has only one element
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return self.tail
        else:
            temp = self.tail
            self.tail = self.get(self.length - 2)
            self.tail.next = None
            self.length -= 1
            return temp

    # Implement remove method to remove an element at given index - O(n)
    def remove(self, index):
        # Validate index
        if index >= self.length or index < 0 or self.head is None:
            return None
        # If list has only one element
        if self.length == 1 and index == 0:
            self.head = None
            self.tail = None
            self.length -= 1
            return self.tail
        # If element is the first element
        if index == 0 and self.length > 1:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp
        # If the element is last element
        if index + 1 == self.length:
            return self.pop()
        # If element is middle of the list
        else:
            temp = self.get(index)
            prev = self.get(index - 1)
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    # Implement insert to add an element at an given index - O(n)
    def insert(self, index, value):
        node = Node(value)
        # Validate index
        if index > self.length or index < 0 or self.head is None:
            return False
        # If there is no element in list
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return True
        # Insert is in the beginning
        if index == 0 and self.head is not None:
            self.prepend(value)
        # Insert is in the tail
        elif index == self.length and self.tail is not None:
            self.append(value)
        # Insert is in middle of the list
        else:
            prev = self.get(index - 1)
            node.next = prev.next
            prev.next = node
            self.length += 1
        return True

    # Implement search to find an element in a list - O(n)
    def search(self, value):
        if self.head is None:
            return None
        else:
            temp = self.head
            for i in range(self.length):
                if temp.value == value:
                    return i
                temp = temp.next
            return None


if __name__ == "__main__":
    my_list = MyList(7)
    my_list.append(1)
    my_list.append(67)
    my_list.prepend(10)
    my_list.prepend(6)
    my_list.print()
    print("search(1)", my_list.search(7))
    print("search(100)", my_list.search(100))
    print("get(3)", my_list.get(3).value)
    print("pop", my_list.pop().value)
    my_list.print()
    print("remove(3)", my_list.remove(3).value)
    my_list.print()
    print("Current length", my_list.length)
    print("remove(0)", my_list.remove(0).value)
    my_list.print()
    print("Current length", my_list.length)
    my_list.insert(0, 9)
    my_list.print()
    print("Current length", my_list.length)
    my_list.insert(3, 19)
    my_list.print()
    print("Current length", my_list.length)
    my_list.insert(3, 29)
    my_list.print()
    print("Current length", my_list.length)

