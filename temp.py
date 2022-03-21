class mystack():

    def __init__(self):
        self.mystack= list()
        

    def push(self,x):
        self.mystack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.mystack)>0:
            return self.mystack.pop()
        else:
            return None
        """
        :rtype: int
        """
        

    def top(self):
            if len(self.mystack)==0:
                pass
                #raise Exception("Queue is Empty")
            else:
                temp=self.queueList[-1]
                return temp
            """
            :rtype: int
            """
        

    def empty(self):
        if len(self.mystack)==0:
            return True
        else:
            return False
        """
        :rtype: bool
        """
        


# Your MyStack object will be instantiated and called as such:
obj = mystack()
x=["MyStack", "push", "push", "top", "pop", "empty"]
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(obj)