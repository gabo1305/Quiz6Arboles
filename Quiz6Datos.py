
"""
Autor: Gabriel Solano Coronado
python 3.8.1
Arboles

"""
class node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, nod, data):
        if nod == None:
            
            nod = node(data)
        else:
            temp = nod.data
            if data < temp:
                nod.left = self.insert(nod.left, data)
            else:
                nod.right = self.insert(nod.right, data)
        return nod

    def inorder(self, nod):
        if nod == None:
            return None
        else:
            self.inorder(nod.left)
            print(nod.data)
            self.inorder(nod.right)

    def preorder(self, nod):
        if nod == None:
            return None
        else:
            print(nod.data)
            self.preorder(nod.left)
            self.preorder(nod.right)

    def postorder(self, nod):
        if nod == None:
            
            return None
        else:
            self.postorder(nod.left)
            self.postorder(nod.right)
            print(nod.data)

    def searchmin(self, nod):
        if nod == None:
            print("no hay minimo")
            return None

        else:
            minim=nod.data
            while(nod.left!=None):
                nod=nod.left
                minim=nod.data
            print(minim)
    def searchmax(self,nod):
        if nod == None:
            print("no hay maximo")
            return None
        else:
            maxim=nod.data
            while(nod.right!=None):
                nod=nod.right
                maxim=nod.data
            print(maxim)
    
        



tree = arbol()
print("prueba 1")
tree.root = tree.insert(tree.root, 5)
tree.root = tree.insert(tree.root, 7)
tree.root = tree.insert(tree.root, 1)
tree.root = tree.insert(tree.root, 3)
tree.root = tree.insert(tree.root, 6)
tree.root = tree.insert(tree.root, 7)

print("inorden")
tree.inorder(tree.root)
print("postorden")
tree.postorder(tree.root)
print("preorden")
tree.preorder(tree.root)
print("max")
tree.searchmax(tree.root)
print("min")
tree.searchmin(tree.root)

print("prueba 2")
tree1 = arbol()
tree1.root = tree.insert(tree1.root, 34)
tree1.root = tree.insert(tree1.root, 67)
tree1.root = tree.insert(tree1.root, 4)
tree1.root = tree.insert(tree1.root, 64)
tree1.root = tree.insert(tree1.root, 45)
tree1.root = tree.insert(tree1.root, 70)
tree1.root = tree.insert(tree1.root, 50)
tree1.root = tree.insert(tree1.root, 11)
tree1.root = tree.insert(tree1.root, 22)
tree1.root = tree.insert(tree1.root, 13)
print("inorden")
tree1.inorder(tree1.root)
print("postorden")
tree1.postorder(tree1.root)
print("preorden")
tree1.preorder(tree1.root)
print("max")
tree1.searchmax(tree1.root)
print("min")
tree1.searchmin(tree1.root)

print("prueba3")
f=arbol()
f.searchmin(f.root)
f.searchmax(f.root)
