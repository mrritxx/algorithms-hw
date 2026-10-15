import unittest

from bubble_sort import bubble_sort
from quick_sort import quick_sort
from dynamic_array import Array
from deque import Deque
from linked_list import LinkedList
from avl_tree import insert, to_list, height


class TestSorts(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
        self.assertEqual(bubble_sort([]), [])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(quick_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
        self.assertEqual(quick_sort([]), [])


class TestArray(unittest.TestCase):
    def test_array(self):
        a = Array()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.get(0), 1)
        a.set(0, 10)
        self.assertEqual(a.get(0), 10)
        self.assertEqual(a.remove(1), 2)
        self.assertEqual(a.size(), 2)


class TestDeque(unittest.TestCase):
    def test_deque(self):
        d = Deque()
        d.add_back(2)
        d.add_front(1)
        d.add_back(3)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.remove_front(), 1)
        self.assertEqual(d.remove_back(), 3)
        self.assertEqual(d.size(), 1)


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        lst = LinkedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        lst.remove(2)
        self.assertEqual(lst.to_list(), [1, 3])
        lst.remove(1)
        self.assertEqual(lst.to_list(), [3])


class TestAVLTree(unittest.TestCase):
    def test_avl_tree(self):
        root = None
        for x in [5, 3, 8, 1, 4]:
            root = insert(root, x)
        self.assertEqual(to_list(root), [1, 3, 4, 5, 8])

    def test_avl_balance(self):
        root = None
        for x in range(1, 8):
            root = insert(root, x)
        self.assertEqual(height(root), 3)
        self.assertEqual(root.value, 4)


if __name__ == "__main__":
    unittest.main()
