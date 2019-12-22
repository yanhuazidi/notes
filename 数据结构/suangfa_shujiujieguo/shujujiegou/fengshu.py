#coding:utf-8
'''
分数数据类型


不支持对float运算,左运算(可自己补全)
作者:魏天华
'''

class FengShu:
    zuixiaofenzi = False
    def __init__(self,zi,mu):
        if not isinstance(zi,int):
            raise TypeError('不期待的数值类型 %s'%zi)
        if not isinstance(mu,int):
            raise TypeError("不期待的数值类型 %s"%mu)
        if mu == 0 :
            raise ZeroDivisionError('分母不能为零')
        self.zi = zi
        self.mu = mu

    def __str__(self):
        x = self.__gongyueshu()
        self.zi = int(self.zi/x)
        self.mu = int(self.mu/x)
        if self.zi ==0:
            return str(0)
        if self.mu ==1:
            return str(self.zi)
        var = self.__zuixiaofenzi()
        return var
    
    def __gongyueshu(self):
        x,y = self.zi,self.mu
        while y:
            tmp = x%y
            x,y = y,tmp
        return x

    def __zuixiaofenzi(self):
        if self.__class__.zuixiaofenzi == True and self.zi > self.mu:
            return str(self.zi//self.mu)+'|'+str(self.zi%self.mu)+'/'+str(self.mu)
        else:
            return str(self.zi)+'/'+str(self.mu)

    def __add__(self,other):
        other = self.__intzhuanghuan(other)
        addzi = self.zi * other.mu + self.mu *other.zi
        addmu = self.mu * other.mu
        return FengShu(addzi,addmu)
        
    def __sub__(self,other):
        other = self.__intzhuanghuan(other)
        addzi = self.zi * other.mu - self.mu *other.zi
        addmu = self.mu * other.mu
        return FengShu(addzi,addmu)

    def __mul__(self,other):
        other = self.__intzhuanghuan(other)
        addzi = self.zi * other.zi
        addmu = self.mu * other.mu
        return FengShu(addzi,addmu)
    
    def __truediv__(self,other):
        other = self.__intzhuanghuan(other)
        addzi = self.zi * other.mu
        addmu = self.mu * other.zi
        return FengShu(addzi,addmu)

    def __lt__(self,other):
        other = self.__intzhuanghuan(other)
        l = self.zi*other.mu
        r = self.mu*other.zi
        if l < r:
            return True
        else:
            return False

    def __le__(self,other):
        other = self.__intzhuanghuan(other)
        l = self.zi*other.mu
        r = self.mu*other.zi
        if l <= r:
            return True
        else:
            return False

    def __gt__(self,other):
        other = self.__intzhuanghuan(other)
        l = self.zi*other.mu
        r = self.mu*other.zi
        if l > r:
            return True
        else:
            return False
        
    def __ge__(self,other):
        other = self.__intzhuanghuan(other)
        l = self.zi*other.mu
        r = self.mu*other.zi
        if l >= r:
            return True
        else:
            return False

    def __eq__(self,other):
        other = self.__intzhuanghuan(other)
        l = self.zi*other.mu
        r = self.mu*other.zi
        if l == r:
            return True
        else:
            return False

    def __ne__(self,other):
        other = self.__intzhuanghuan(other)
        l = self.zi*other.mu
        r = self.mu*other.zi
        if l != r:
            return True
        else:
            return False

    def __float__(self):
        return self.zi/self.mu
    
    def __int__(self):
        return int(self.zi/self.mu)

    def __bool__(self):
        return bool(self.zi)

    def get(self):
        return self.__str__()

    def __intzhuanghuan(self,intnumber):
        if isinstance(intnumber,FengShu):
            return intnumber
        elif isinstance(intnumber,int):
            intnumber = FengShu(intnumber,1)
            return intnumber
        else:
            raise TypeError("不期待的数值类型 %s"%intnumber)

if __name__=='__main__':
    import unittest
    class FengShuTest(unittest.TestCase):
        def setUp(self):
            self.a = FengShu(3,7)
            self.b = FengShu(5,7)
        def test_init(self):
            var = FengShu(1,2)
            self.assertEqual(var.get(),'1/2')
        def test_add(self):
            var = self.a + self.b
            self.assertEqual(var.get(),'8/7')
    unittest.main()
    # a = FengShu(4,6)
    # print(a)
    # b = FengShu(2,3)
    # c = a+b
    # print(c)
    # d = a-b
    # print(d)
    # d = a-c
    # print(d)
    # d = a/b
    # print(d)
    # print(a>b)
    # print(a==b)
    # print(a!=b)
    # print(float(c))
    # print(bool(a))
    # print(int(c))
    # d = a - 4
    # print(d)
    # a = FengShu(7,3)
    # FengShu.zuixiaofenzi=True
    # print(a)