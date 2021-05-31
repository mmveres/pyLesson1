class BookTreeNode:
    def __init__(self, book, lchild, rchild):
        self.book = book
        self.lchild = lchild
        self.rchild = rchild


class BookTree:
    def __init__(self, books=None):
        if books is None:
            self.head = None

    def add(self, book):
        node = BookTreeNode(book,None,None)
        if self.head is None:
            self.head = node
        else:
            iter_node = self.head
            while iter_node is not None:
                if node.book.udc < iter_node.book.udc:
                    if iter_node.lchild is None:
                        iter_node.lchild = node
                        break;
                    else:
                        iter_node = iter_node.lchild
                elif node.book.udc > iter_node.book.udc:
                    if iter_node.rchild is None:
                        iter_node.rchild = node
                        break;
                    else:
                        iter_node = iter_node.rchild

    def print(self):
        def move(node):
            if node is not None:
                move(node.lchild)
                print(node.book)
                move(node.rchild)

        move(self.head)

