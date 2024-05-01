

# struktura liked list
class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next_node = next_node

# drukowanie
def print_linkedlist(head_of_list):
    tmp = head_of_list
    print("[", end="")
    while tmp is not None:
        print(tmp.info, end=" ")
        tmp = tmp.next_node
    print("]")


# dodaje kazdy element z listy i sortuje
def create_linked_and_add_sorted(elements):
    root = None  # Początkowo lista jest pusta
    for element in elements:
        root = add_element_to_linked_list(root, element)
    return root

# wyszukuje 1 wartość
def search_1element(root, value):
    current_node = root
    while current_node is not None:
        if current_node.info == value:
            return current_node
        current_node = current_node.next_node
    return None

# dodaje elemnty z listy do gotowej linked list
def add_elements_to_linked_list(root, elements):
    for element in elements:
        root = add_element_to_linked_list(root, element)
    return root

#  dodaje 1 element do linked list
def add_element_to_linked_list(root, element):
    new_node = Node(element)
    if root is None or root.info > element:
        new_node.next_node = root
        return new_node
    else:
        current = root
        while current.next_node and current.next_node.info < element:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
    return root

# usuwwa linked list od startu
def delete_from_start(head):
    current_node = head
    while current_node is not None:
        next_node = current_node.next_node
        del current_node
        current_node = next_node

# usuwa linked list od konca
def delete_from_end(head):
    if head is None:
        return
    if head.next_node is None:
        del head
        return
    current_node = head
    while current_node.next_node.next_node is not None:
        current_node = current_node.next_node
    del current_node.next_node
    current_node.next_node = None

    delete_from_end(head)


# wyszukuje wiele elementow
def search_many_from_linked(root, values):
    found_nodes = []
    for value in values:
        current = root
        found = False
        while current:
            if current.info == value:
                found_nodes.append(current.info)
                found = True
                break
            current = current.next_node
        if not found:
            found_nodes.append(None)
    return found_nodes



# ============================================================================================
# if __name__ == '__main__':
#     head = Node("a")
#     head = Node("b", head)
#     head = Node("c", head)
#     head = Node("d", head)
#
#     print_linkedlist(head)

#
# a = 5
# b = 7
# root = Node(2)
# root.next_node = Node(4)
# root.next_node.next_node = Node(6)
# root.next_node.next_node.next_node = Node(8)
# root.next_node.next_node.next_node.next_node = Node(10)
#
# put_element(a, root)
#
# print_linkedlist(root)
# put_element(b, root)
#
# print_linkedlist(root)
#
# finded = search_linkedlist(root, 1)
# print_linkedlist(finded)

# roo1 = Node(0)
# print_linkedlist(roo1)

# list = [1,9,10,3,6]
# list2 = create_and_add_sorted(list)
#     # print_linkedlist(list2)
#     #
#     # list_to_find = [9,5,6]
#     # found = search_list(list2, list_to_find)
#     # print(found)


# potwierdzenei dla wyszukania elementow
def print_search_results(values, results):
    for value, result in zip(values, results):
        if result is not None:
            print(f"Wartość {value} została znaleziona w liście.")
        else:
            print(f"Wartość {value} nie została znaleziona w liście.")

# # Lista wartości do wyszukania
# list_to_find = [9, 5, 6]
#
# # Wyniki wyszukiwania
# found = search_list(list2, list_to_find)
#
# # Wyświetlanie wyników
# print_search_results(list_to_find, found)





