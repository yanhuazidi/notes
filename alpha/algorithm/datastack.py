# -*- coding: utf-8 -*-

def index_decorator(fun):
    def waref(self,index,*args,**kwargs):
        assert isinstance(index,int),'index must int'
        assert 0 <= index < self.__class__.conut ,'index overflow length'
        return fun(self,index,*args,**kwargs) 
    return waref

class Node:
    __slots__=['data','next']
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Stack:
    conut=0
    def __init__(self):
        self.head=Node()

    def add(self,data):
        if not self.head.data:
            self.head.data=data
        else:
            cur = self.head
            while True:
                if not cur.next:
                    node = Node(data)
                    cur.next = node
                    break
                else:
                    cur = cur.next
        self.__class__.conut = self.__class__.conut +1

    
    def index(self,data,defult=None):
        if not self.head.data:
            return None
        else:
            i = 0
            cur = self.head
            while True:
                if data==cur.data:
                    return i
                else:
                    i+=1
                    cur = cur.next
                    if not cur:
                        return defult


    # @index_decorator
    def __getitem__(self,index):
        cur = self.head
        print(index.start)
        for _ in range(index):
           cur = cur.next
        else:
            return cur.data

    # @index_decorator
    def __setitem__(self,index,data):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        else:
            cur.data = data

    # @index_decorator
    def __delitem__(self,index):
        prev = None
        cur = self.head
        next = self.head.next
        for _ in range(index):
            prev = cur
            cur = cur.next
            next = cur.next
        else:
            prev.next=next
            del cur
            
    
    def __len__(self):
        return self.__class__.conut

    def __str__(self):
        reself = []
        if not self.head:
            return 'Stack:'+str(reself)
        cur = self.head
        while True:
            reself.append(cur.data)
            if not cur.next:
                return 'Stack:'+str(reself)
            else:
                cur = cur.next
    
    __repr__ = __str__



if __name__=='__main__':
    s = Stack()
    s.add('wei')
    s.add('wei1')
    s.add('wei2')
    s.add('wei3')
    s.add('wei4')
    print(s[1:3])
        






