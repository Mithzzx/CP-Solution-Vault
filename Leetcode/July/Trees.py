class Tree:
    def __init__(self,v=None):
        self.children = set()
        self.value = v
        self.parent = None
        self.level = 0

    def add_child(self,value):
        value.parent = self
        value.level = self.level + 1
        self.children.add(value)

    def print_tree(self):
        print("   "*self.level if self.level==1 else"   "*(self.level-1) + " |  "*(self.level-1) ,
              "|__" if self.level>0 else "",
              self.value)
        if self.children:
            for child in self.children:
                child.print_tree()

mytree = Tree()
mytree.value = ("Book")
c = Tree()
c.value = ("Pen")
mytree.add_child(c)
c1 = Tree()
c1.value = ("Pencil")
mytree.add_child(c1)
c11 = Tree("Colored")
c12 = Tree("Non Colored")
c1.add_child(c12)
c1.add_child(c11)

d = Tree("Ink")
c.add_child(d)
d.add_child(Tree("Blue"))
c.add_child(Tree("Gel"))

mytree.print_tree()