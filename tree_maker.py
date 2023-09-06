class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __xor__(self, other):
        if self and not other or other and not self:
            return True
        return False


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildTree(preorder, inorder):
    if inorder:
        rootval = preorder[0]
        root = TreeNode(rootval)
        index = inorder.index(preorder.pop(0))
        root.left = buildTree(preorder, inorder[:index])
        root.right = buildTree(preorder, inorder[index + 1 :])
        return root


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
    print_postorder(root.left)
    print_postorder(root.right)

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

