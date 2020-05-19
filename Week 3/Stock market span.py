"""
Explanation
Compare today's price with the last element of the stack and add the count to the answer 
print the answer

"""


class StockSpanner:

    def __init__(self):
        self.stack=[]
        
    def next(self, price: int):
        self.ans=1
        
        if price==None:
            return price
        
        
        while self.stack and self.stack[-1][0]<=price:
            self.ans+=self.stack.pop()[1]
            
        self.stack.append([price,self.ans])
        
        
        
        return self.ans


