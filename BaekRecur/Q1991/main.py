tree = {}

# 입력 받기
for _ in range(int(input())):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder(node):
    if node == ".":
        return
    print(node, end='')             # 루트 출력
    preorder(tree[node][0])         # 왼쪽
    preorder(tree[node][1])         # 오른쪽

def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])          # 왼쪽
    print(node, end='')             # 루트
    inorder(tree[node][1])          # 오른쪽

def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])        # 왼쪽
    postorder(tree[node][1])        # 오른쪽
    print(node, end='')             # 루트

preorder('A')
print()
inorder('A')
print()
postorder('A')
