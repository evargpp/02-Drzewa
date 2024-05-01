class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def insert(root, x):
    if root is None:
        return TreeNode(x)
    if x < root.info:
        root.left = insert(root.left, x)
    elif x > root.info:
        root.right = insert(root.right, x)
    return root

def create_bst_from_array(arr):
    root = None
    for x in arr:
        root = insert(root, x)
    return root


def search(root, x):
    ptr = root
    while ptr:
        if x > ptr.info:
            ptr = ptr.right
        elif x < ptr.info:
            ptr = ptr.left
        else:
            return ptr  # Znaleziono węzeł
    return None  # Węzeł nie został znaleziony

def search_in_bst_by_array(root, arr):
    results = []
    for x in arr:
        ptr = root
        found = False
        while ptr:
            if x > ptr.info:
                ptr = ptr.right
            elif x < ptr.info:
                ptr = ptr.left
            else:
                results.append(ptr)
                found = True
                break
        if not found:
            results.append(None)  # Dodajemy None dla elementów nieznalezionych
    return results



def inorder(root):
    if root:
        inorder(root.left)
        print(root.info, end=' ')
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.info, end=' ')

def preorder(root):
    if root:
        print(root.info, end=' ')
        preorder(root.left)
        preorder(root.right)

def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, value):
    if root is None:
        return root

    # Jeśli wartość do usunięcia jest mniejsza od wartości roota, jest w lewym poddrzewie
    if value < root.info:
        root.left = delete_node(root.left, value)
    # Jeśli wartość do usunięcia jest większa od wartości roota, jest w prawym poddrzewie
    elif value > root.info:
        root.right = delete_node(root.right, value)
    # Znaleziono węzeł do usunięcia
    else:
        # Przypadek 1: Węzeł do usunięcia ma tylko jedno dziecko lub nie ma dzieci
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Przypadek 2: Węzeł do usunięcia ma dwoje dzieci
        temp = find_min_node(root.right)
        root.info = temp.info
        root.right = delete_node(root.right, temp.info)

    return root

def delete_tree_in_order(node):
    if node is not None:
        # Najpierw przejdź przez lewe poddrzewo
        delete_tree_in_order(node.left)
        node.left = None
        # Następnie przejdź przez prawe poddrzewo
        delete_tree_in_order(node.right)
        node.right = None
        node = None

def delete_tree_reverse_order(node):
    if node is not None:
        # Najpierw przejdź przez prawe poddrzewo
        delete_tree_reverse_order(node.right)
        node.right = None
        # Następnie przejdź przez lewe poddrzewo
        delete_tree_reverse_order(node.left)
        node.left = None
        node = None
        
        
# test usuwania
# # Tworzenie przykładowego drzewa BST
# root = create_bst_from_array([50, 30, 70, 20, 40, 60, 80])
# 
# print("Drzewo przed usunięciem:")
# inorder(root)
# print("\n")
# 
# # Usuwanie węzłów w kolejności in-order
# print("Usuwanie węzłów w kolejności in-order:")
# delete_tree_in_order(root)
# 
# # Ponowne stworzenie drzewa do usuwania w kolejności reverse in-order
# root = create_bst_from_array([50, 30, 70, 20, 40, 60, 80])
# 
# print("\nDrzewo przed usunięciem w reverse in-order:")
# inorder(root)
# print("\n")
# 
# # Usuwanie węzłów w kolejności reverse in-order
# print("Usuwanie węzłów w kolejności reverse in-order:")
# delete_tree_reverse_order(root)


# usuwanie 1 elementu
# root = create_bst_from_array([50, 30, 70, 20, 40, 60, 80])
# print("Drzewo przed usunięciem:")
# inorder(root)
# print()
#
# root = delete_node(root, 50)
# print("Drzewo po usunięciu elementu 50:")
# inorder(root)
# print()
#
#
# root = None
# root = insert(root, 10)
# root = insert(root, 5)
# root = insert(root, 15)
# root = insert(root, 3)
# root = insert(root, 7)
# root = insert(root, 12)
#
# print("Inorder:")
# inorder(root)
# print("\nPostorder:")
# postorder(root)
# print("\nPreorder:")
# preorder(root)
#
#
# result = search(root, 7)
# if result:
#     print("\nElement znaleziony:", result.info)
# else:
#     print("\nElement nie znaleziony.")
#
# array = [20, 10, 30, 5, 15, 25, 35]
# root = create_bst_from_array(array)
#
# print("Inorder:")
# inorder(root)
# print("\nPreorder:")
# preorder(root)
# print("\nPostorder:")
# postorder(root)
# Przykładowe użycie szykania na bazie lsity
# array = [20, 10, 30, 5, 15, 25, 35]
# root = create_bst_from_array(array)
#
# search_elements = [15, 25, 40]  # Elementy do wyszukania
#
# results = search(root, search_elements)
# for x, result in zip(search_elements, results):
#     if result:
#         print("Element", x, "znaleziony w drzewie.")
#     else:
#         print("Element", x, "nie znaleziony w drzewie.")
