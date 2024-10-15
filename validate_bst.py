class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    prev = [None]
    return inorderTraversal(root, prev)

def inorderTraversal(node, prev):
    if node is None:
        return True

    if not inorderTraversal(node.left, prev):
        return False

    if prev[0] is not None and node.val <= prev[0]:
        return False
    prev[0] = node.val
    return inorderTraversal(node.right, prev)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(isValidBST(root))
