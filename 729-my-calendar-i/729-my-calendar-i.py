import bisect
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    
    def insertNode(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right =  node
                return True
            return self.right.insertNode(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insertNode(node)
        else:
            return False
                
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insertNode(Node(start , end))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)