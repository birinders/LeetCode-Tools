from typing import Final

null: Final = None


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __xor__(self, other):
        if self and not other or other and not self:
            return True
        return False


def buildTree_PreIn(preorder, inorder):
    if inorder:
        rootval = preorder[0]
        root = TreeNode(rootval)
        index = inorder.index(preorder.pop(0))
        root.left = buildTree_PreIn(preorder, inorder[:index])
        root.right = buildTree_PreIn(preorder, inorder[index + 1 :])
        return root


def buildTreeLC(values: list):
    """
    Builds a Binary Tree from LeetCode's format of providing binary trees.

    It is recommended to copy paste their tree lists directly to avoid invalid input.
    """

    if not values:
        return None
    n = len(values)
    idx = 1
    head = TreeNode(values[0])
    prev_level = [head]

    while prev_level:
        new_prev = []
        for node in prev_level:
            if idx < n and values[idx] is not None:
                node.left = TreeNode(values[idx])
                new_prev.append(node.left)

            if idx + 1 < n and values[idx + 1] is not None:
                node.right = TreeNode(values[idx + 1])
                new_prev.append(node.right)

            idx += 2

        prev_level = new_prev

    return head


def print_level(root):
    queue = [root]

    while queue:
        print(*[node.val for node in queue], end="\n")

        nqueue = []
        for node in queue:
            if node.left:
                nqueue.append(node.left)
            if node.right:
                nqueue.append(node.right)

        queue = nqueue


def print_preorder(root):
    if not root:
        return None
    print(root.val)
    print_preorder(root.left)
    print_preorder(root.right)


def print_inorder(root):
    if not root:
        return None
    print_inorder(root.left)
    print(f"{root.val} ", end="")
    print_inorder(root.right)


def print_postorder(root):
    if not root:
        return None
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val)
