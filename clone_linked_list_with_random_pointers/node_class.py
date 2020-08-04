class Node:
    def __init__(self, data=None, next: 'Node' = None, rnd: 'Node' = None):
        self.data = data
        self.next = next
        self.rnd = rnd

    @staticmethod
    def get_linked_list(head) -> list:
        ll = []
        n = head
        while n:
            ll.append(n)
            n = n.next

        return ll

    @staticmethod
    def clone_linked_list(head) -> 'Node':
        nodes_map = {}
        n = head
        while n:
            nodes_map[n] = Node(n.data)
            n = n.next

        n = head
        while n:
            nodes_map[n].next = nodes_map.get(n.next)
            nodes_map[n].rnd = nodes_map.get(n.rnd)
            n = n.next

        return nodes_map.get(head)

    def __hash__(self):
        return hash((self.data, self.next, self.rnd.data))

    def __eq__(self, other):
        return (self.data, self.rnd.data) == (other.data, other.rnd.data)
