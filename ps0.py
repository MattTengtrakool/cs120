#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None
    
#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    count = 1
    if v != None:
        if v.left != None:
            calculate_sizes(v.left)
            count += v.left.size 
        if v.right != None:
            calculate_sizes(v.right)
            count += v.right.size
    v.size = count
    return

## This program has an O(N) runtime as it calls calculate size only once per descendant node. Thus for the amount of descendant nodes referenced as N, the program will run O(N) times.


#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)

def find_vertex(r):
    compsize = r.size / 2
    def recursiveFind(vert):
        if vert is not None:
            print("vertex size")
            print(vert.size)
            if vert.size <= compsize:
                print("hi")
                return vert.parent
            else:
                lefts = 0
                rights = 0
                if vert.left is not None:
                    lefts = vert.left.size
                if vert.right is not None:
                    rights = vert.right.size
                if lefts > rights:
                    return recursiveFind(vert.left)
                else:
                    return recursiveFind(vert.right)
        
    
    return recursiveFind(r)

## this program has an O(H) runtime where h is the height of the tree. This is because for each row, the recursive function recursiveFind judges each child of the binary parent and chooses the larger of the two childs to traverse into. This continues until it reaches a child that has size less than n/2. As a result, recursive find would only be called h times, one for each of the larger children in the tree thus equaling the height in the worst possible case.