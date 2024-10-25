class Tnode:
    def __init__(self, val):  
        self.val = val
        self.left = None
        self.right = None

def create(arr, i, n):
    if i < n:
        temp = Tnode(arr[i]) 
        root = temp
        root.left = create(arr, 2 * i + 1, n)  
        root.right = create(arr, 2 * i + 2, n)  
        return root
    return None

arr = [11, 12, 5, 7, 10, 11, 12, 14]
root = create(arr, 0, len(arr))

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')

def pre_order(root):
    if not root:
        return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)

print("post-order")
post_order(root)
print("\npre-order")
pre_order(root)
print("\nin-order")
in_order(root)
