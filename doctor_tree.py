class DoctorNode:
    def __init__(self,name):
        self.name=name
        self.left=None
        self.right=None



class DoctorTree:
    def __init__(self):
        self.root=None

    def insert(self,manager_name,doctor_name,side, current=None):
        if not self.root:
            print("No root doctor in tree. Please add root doctor.")
        if current is None:
            current=self.root
        if current.name==manager_name:
            new_node=DoctorNode(doctor_name)
            if side.lower()=="left":
                if current.left:
                    print(f"{manager_name} already has a left subordinate.")
                else:
                    current.left=new_node
                    print(f"{doctor_name} added under {manager_name} to the left.")
            if side.lower()=="right":
                if current.right:
                    print(f"{manager_name} already has a right subordinate.")
                else:
                    current.right=new_node
                    print(f"{doctor_name} added under {manager_name} to the right.")
            return
        if current.left:
            self.insert(manager_name,doctor_name,side,current.left)
        if current.right:
            self.insert(manager_name,doctor_name,side,current.right)
    def preorder(self,node):
        if node:
            print(node.name)
            self.preorder(node.left)
            self.inorder(node.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.name)
            self.inorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.name)




# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Smith")
    tree.insert("Dr. Smith", "Dr. Jones", "left")
    tree.insert("Dr. Smith", "Dr. Lee", "right")
    tree.insert("Dr. Jones", "Dr. Patel", "left")

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)
    print("\nInorder Traversal:")
    tree.inorder(tree.root)
    print("\nPostorder Traversal:")
    tree.postorder(tree.root)