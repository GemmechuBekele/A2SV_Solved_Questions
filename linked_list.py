class Node:
    def __init__(self, value):
        self.value = value # value
        self.next = None # pointer

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # pointer to new node
            self.tail = new_node # new tail is over new node

        self.length += 1
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' → '
            temp_node = temp_node.next

        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if new_node is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traversal(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def search(self, target):
        if self.head is None:
            return "Link doesn't exist"
        else:
            node = self.head
            while node:
                if node.value == target:
                    return node.value
                node = node.next
            return "Link doesn't exist"
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current
        return current
    def set_method(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
nll = LinkedList()
nll.append(5)

nll.insert(0, 1)
print(nll)
# print(nll.length)