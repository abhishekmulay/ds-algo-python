import unittest
from SinglyLinkedList import SinglyLinkedList


class SinglyLinkedListTest(unittest.TestCase):

    def test_list_count(self):
        lst = SinglyLinkedList()
        self.assertEqual(lst.size(), 0, " Count should be 0")

        lst.add("some data")
        self.assertEqual(lst.size(), 1, " Count should be 1")

        lst.add("some more data")
        self.assertEqual(lst.size(), 2, " Count should be 2")

    def test_in_list(self):
        lst = SinglyLinkedList()
        lst.add(2)
        self.assertTrue(2 in lst, "2 should be in list")
        self.assertFalse(10 in lst, "10 should not be in list")

    def test_delete(self):
        lst = SinglyLinkedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(lst.size(), 3)
        lst.delete(2)
        self.assertEqual(lst.size(), 2 , " list length should decrease after delete")
        self.assertFalse( 2 in lst, "2 should be removed from list")

if __name__ == '__main__':
    unittest.main()
