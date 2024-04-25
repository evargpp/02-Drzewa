
class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next_node = next_node


def print_linkedlist(head_of_list):
    tmp = head_of_list
    print("[", end="")
    while tmp is not None:
        print(tmp.info, end=" ")
        tmp = tmp.next_node
    print("]")


# ============================================================================================
# if __name__ == '__main__':
#     head = Node("a")
#     head = Node("b", head)
#     head = Node("c", head)
#     head = Node("d", head)
#
#     print_linkedlist(head)

a = 5
root = Node(2)
root.next_node = Node(4)
root.next_node.next_node = Node(6)
root.next_node.next_node.next_node = Node(8)
root.next_node.next_node.next_node.next_node = Node(10)

if root.info > a:
    tmp_node = Node(a)
    tmp_node.next_node = root
    root = tmp_node
else:
    tmp_node = root
    while (tmp_node.next_node is not None) and (tmp_node.next_node.info < a):
        tmp_node = tmp_node.next_node
    new_node = Node(a)

    new_node.next_node = tmp_node.next_node
    tmp_node.next_node = new_node

print_linkedlist(root)
