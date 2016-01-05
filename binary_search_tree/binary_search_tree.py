
class Node(object):
    '''Node class
    '''
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        '''Recursively insert a new node in the tree
        '''
        # Base case
        if data == self.val:
            # Don't insert duplicate nodes if val already present in the tree
            return False
        elif data < self.val:
            # Smaller values always get inserted to the left
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            # Larger values always get inserted to the right
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find(self, data):
        '''Recursively find a value in the tree
        '''
        # Base case
        if data == self.val:
            return True
        elif data < self.val:
            # Look to the left for smaller values
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            # Look to the right for larger values
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False

    def preorder(self):
        # root, left, right traversal
        print str(self.val)

        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def postorder(self):
        # left, right, root traversal
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()

        print str(self.val)

    def inorder(self):
        # Left, root, right traversal
        if self.left_child:
            self.left_child.inorder()

        print str(self.val)

        if self.right_child:
            self.right_child.inorder()


class Tree(object):
    '''Interface class for Tree class
    '''
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''Relies on Node.insert() for heavy lifting
        '''
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        '''Relies on Node.find() for the heavy lifting
        '''
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root:
            self.root.preorder()

    def postorder(self):
        if self.root:
            self.root.postorder()

    def inorder(self):
        if self.root:
            self.root.inorder()
