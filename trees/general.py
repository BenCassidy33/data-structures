class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        """
            parent
            /    \
        child    child
        """
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p != None:
            level += 1
            p = p.parent
        return level
        
    def print_tree(self):
        spaces = ' ' * self.get_level() * 5
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()
                
    def print_level(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_level(level)
        
root = TreeNode("Grandpa")

dad = TreeNode("Dad")
dad.add_child(TreeNode("Me"))
dad.add_child(TreeNode("Brother"))
dad.add_child(TreeNode("Sister"))

aunt = TreeNode("Aunt")
aunt.add_child(TreeNode("Cousin 1"))
aunt.add_child(TreeNode("Cousin 2"))
aunt.add_child(TreeNode("Cousin 3"))

uncle = TreeNode("Uncle (Hardened Criminal)")
uncle.add_child(TreeNode("Adult Cousin"))
uncle.add_child(TreeNode("Nerd Cousin"))
uncle.add_child(TreeNode("Boring Cousin"))

root.add_child(dad)
root.add_child(aunt)
root.add_child(uncle)

root.print_tree()