# Create a Simple Single Linked list Data Structure
# Eg. head => 8 -> 6 -> 10 <= tail

# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    # Method to print the list
    def print(self):
        node = self.head
        print("head", end=" -> ")
        while node:
            if node.next is not None:
                print(node.value, end=" -> ")
            else:
                print(node.value, end=" <- ")
            node = node.next
        print("tail")


if __name__ == "__main__":
    ll = LinkedList(2)
    ll.print()
