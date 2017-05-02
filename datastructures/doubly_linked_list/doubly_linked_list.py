class Node(object):
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.previous = prev

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_prev(self):
        return self.previous

    def set_previous(self, prev):
        self.previous = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def _create_node(self, data):
        return Node(data, None, None)

    def add(self, data):
        # there are no items in the list yet
        if self.count == 0:
            self.add_at_beginning(data)

        # there are more than one items in the list
        self.add_at_end(data)

    def add_at_beginning(self, data):
        node = self._create_node(data)
        self.head = node
        self.tail = node
        node.previous = None
        node.next = None
        self.count += 1

    def add_at_end(self, data):
        print "self.head = " + str(self.head.get_data()) + " | self.tail = " + str(
            self.tail.get_data()) + " data = " + str(data)

        if self.count == 1:
            # this is the second element being added in the list
            node = self._create_node(data)
            node.previous = self.tail
            self.head = node
            node.next = self.tail
            self.count += 1
            return

        # there are more than one items in the list
        node = self._create_node(data)
        self.tail.next = node
        node.previous = self.tail
        self.tail = node
        node.next = self.head
        self.count += 1

        # print "after add : " + self.display()

    def display(self):
        output = ""
        pointer = self.head
        # there is only one element
        if self.count == 1:
            output = str(self.head.get_data())
        else:
            while pointer != self.tail:
                output += str(pointer.get_data()) + ", "
                pointer = pointer.get_next()

        return output

    def __str__(self):
        return self.display()


if __name__ == '__main__':
    lst = DoublyLinkedList()
    lst.add("a")
    lst.add("b")
    lst.add("c")
    lst.add("d")
    print str(lst)
