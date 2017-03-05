# This is implementation of Singly Linked List using Python


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.dat = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def __str__(self):
        return str(self.data)


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def _create_node(self, data):
        return Node(data, None)

    def _get_last_node(self):
        current = self.head
        previous = None
        while current:
            previous = current
            current = current.get_next()
        return previous

    def add(self, data):
        # there are no nodes in list
        if self.count == 0:
            self.head = self._create_node(data)
            self.count += 1
            return

        # there are nodes present in list, add new node at the end of list
        self.add_at_end(data)

    def add_at_begining(self, data):
        node = self._create_node(data)
        start_node = self.head
        node.set_next(start_node)
        self.count += 1

    def add_at_end(self, data):
        node = self._create_node(data)
        last_node = self._get_last_node()
        self.count += 1
        last_node.set_next(node)

    def __contains__(self, item):
        if self.search(item):
            return True
        return False

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            current = current.get_next()
        return False

    def delete(self, data):
        current = previous = self.head
        while current:
            # found the node!
            if current.get_data() == data:
                # set next of current as next of the previous node to current so that the link doesn't break.
                previous.set_next(current.get_next())
                current = None
                self.count -= 1
                return

            previous = current
            current = current.get_next()

        print "Value does not exist in list"

    def size(self):
        return self.count

    def __str__(self):
        output = "SinglyLinkedList = {"
        pointer = self.head
        while pointer:
            output += str(pointer.get_data()) + ', '
            pointer = pointer.get_next()
        return output + "}"


if __name__ == '__main__':
    lst = SinglyLinkedList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    print lst.size()
    print str(lst)
    lst.delete(2)
    print str(lst)
