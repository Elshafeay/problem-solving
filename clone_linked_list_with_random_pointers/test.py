import unittest
from node_class import Node


class TestLinkedListCloning(unittest.TestCase):
    maxDiff = None

    @staticmethod
    def creating_list() -> Node:
        # initiating nodes with data
        n1, n2, n3, n4 = Node(5), Node(6), Node(7), Node(8)
        # connecting each node with its Successor
        n1.next, n2.next, n3.next, n4.next = n2, n3, n4, None
        # connecting each node with its random node
        n1.rnd = n3
        n2.rnd = n4
        n3.rnd = n2
        n4.rnd = n1
        # returning linked list head node
        return n1

    def test_get_linked_list(self):
        head = self.creating_list()
        result_list = Node.get_linked_list(head)
        self.assertEqual(result_list[2].data, 7)
        self.assertEqual(result_list[2].next, result_list[3])
        self.assertEqual(result_list[2].rnd, result_list[1])

    def test_clone_linked_list(self):
        head = self.creating_list()
        new_head = Node.clone_linked_list(head)

        # getting the two lists for comparison
        old_list = Node.get_linked_list(head)
        new_list = Node.get_linked_list(new_head)

        self.assertEqual(new_list[1].data, 6)
        self.assertEqual(new_list[1].next, new_list[2])
        self.assertEqual(new_list[1].rnd, new_list[3])
        self.assertEqual(old_list, new_list)
        self.assertIsNot(old_list, new_list)


if __name__ == "__main__":
    unittest.main()
