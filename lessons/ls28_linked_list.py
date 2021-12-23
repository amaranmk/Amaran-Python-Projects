"""Example fo writing a test subject."""

from __future__ import annotations  # Needed to allow us to declare a recursive data strcuture

from typing import Optional


class Node:
    """Style linked list Node."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor."""
        self.data = data
        self.next = next


def count(head: Optional[Node]) -> int:
    """Counts up the lengh of a linked list"""
    if head is None:
        return 0
    else:
        return 1 + count(head.next)
            


third_node: Node = Node(3, None)
second_node: Node = Node(2, third_node)
a_node: Node = Node(1, second_node)
print(a_node.next.next.data)
print(count(a_node))
