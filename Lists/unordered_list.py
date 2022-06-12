class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        if current == None:
            current = item

    def insert(self, item, pos):
        current = self.head
        position = 0
        while position is not pos:
            current = current.next
            position = position + 1

        current.next = current
        current = item

    def index(self, item):
        current = self.head
        position = 0
        while current is not None:
            if current.data == item:
                return position
            current = current.next
            position = position + 1
        
        if current is None:
            raise ValueError("{} is not in the list".format(item))
        
    def pop(self):
        current = self.head
        previous = None

        while current is not None:
            previous = current
            current = current.next

        if current is None:
            previous = None


        