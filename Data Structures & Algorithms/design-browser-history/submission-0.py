class ListNode:
    def __init__(self, link):
        self.link = link
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.left = ListNode("dummyLeft")
        self.right = ListNode("dummyRight")
        self.left.next = ListNode(homepage) 
        self.left.next.prev = self.left
        self.right.prev = self.left.next
        self.left.next.next = self.right
        self.cur = self.left.next 
        

    def visit(self, url: str) -> None:
        node, next, prev = ListNode(url), self.right, self.cur 
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        self.cur = node

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev != self.left:
            self.cur = self.cur.prev
            steps -=1
        return self.cur.link        

        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next != self.right:
            self.cur = self.cur.next
            steps -=1
        return self.cur.link        

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)