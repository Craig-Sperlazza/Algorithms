import bst
t = bst.BST()
print(t)

for i in range(4):
    t.insert(i);

print(t)

t.delete_min()
print(t)

import avl
t = avl.AVL()
print(t)

for i in range(4):
    t.insert(i);

print(t)
 
t.delete_min()
print(t)