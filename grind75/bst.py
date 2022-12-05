class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# A utility function to do inorder tree traversal


# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

r = Node(5)
r = insert(r, 3)
r = insert(r, 2)
r = insert(r, 4)
r = insert(r, 7)
r = insert(r, 6)
r = insert(r, 8)
r = insert(r, 9)


def length(root, sum):
    if root is None:
        return 0
    sum += max(length(root.left, sum), length(root.right, sum))
    sum += 1
    return sum


def check(root):
    return abs(length(root.right, 0)-length(root.left, 0)) < 2


def solution(root):
    return check(root.left) and check(root.right)


print(solution(r))
