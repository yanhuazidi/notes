'''排序算法'''

import time

def jishi(fun):
    def jishu(self):
        t = time.time()
        for _ in range(100):
            fun(self)
        t1 = time.time()-t
        print('时间为:%s'%str(t1))
    return jishu

class PaiXu:
    def __init__(self,data):
        self.data = data
    # 1.冒泡排序
    #     基本思路：1.相邻元素两两比较，前者大于后者则交换(大者排后)
    #             2.第一次遍历，从第一对数据到最后一对数据，将最大值上浮到顶端
    #             3.后面继续将未排序的部分重复上步骤，依次上浮最大值
    #             4.每次扫描的元素越来越少，直到不再发生交换为止
    #         评价：时间复杂度：

    @jishi
    def bubble(self):
        '''冒泡排序'''
        for n in range(len(self.data)-1):
            for i in range(len(self.data)-1-n):
                if self.data[i] > self.data[i+1]:
                    self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
        return self.data

    # 2.插入排序：
    #     基本思路：首元素自然有序，取出下一个元素，对排序的序列从后向前扫描
    #             若扫描有序数据大于被取出的元素，则该有序数据后移，
    #             若扫描的有序数据小于被取出的元素，在该有序数据后面插入被取出的元素，
    #             若扫描的所有有序数据大于被取出出的元素，则有序数据的头部插入被取出的元素
    #             再取出下一个元素，继续重复之前的步骤，直到所有元素都有序为止
    
    @jishi                    # 时间：O(n2)    空间:o(1)
    def insertion(self):
        '''插入排序'''
        for n in range(1, len(self.data)):
            tmp = self.data[n]
            for i in range(n, -1, -1):
                if self.data[i-1] < tmp or i == 0:
                    break
                else:
                    self.data[i] = self.data[i - 1]
            self.data[i] = tmp
        return self.data

    # 3.快速排序：
    #     算法描述：从待排序的序列中任意选择一个基准
    #             将所有小于基准的元素、等于和所有大于基准的元素进行分组，小于部分
    #             放基准前面，大于部分放基准后面
    #             再以递归的方式，对基准之前和基准之后的分组继续操作，直到每个组的
    #             元素不多于一个为止

    #         时间：O(nlogn)  若每次都能均匀分组则快速排序速度是最快的
    @jishi
    def quick(self):        #递归深度不能超过１０００
        '''快速排序'''
        def __quick(data):
            if len(data) < 2:
                return data
            mark = data[0]
            smaller = [x for x in data if x < mark]
            equal = [x for x in data if x == mark]
            bigger = [x for x in data if x > mark]
            return __quick(smaller) + equal + __quick(bigger)
        data = list(self.data)
        L = __quick(data)
        return L

    # 4.选择法排序
    #     算法描述：每次选择出未排序序列段中的最大值(或最小值)的元素，与未排序序列段最前面元素交换，一直到全部排序
    @jishi
    def xuanzi(self):
        '''选择排序'''
        for x in range(len(self.data)-1):
            _min = self.data[x]
            for i in self.data[x:]:
                if _min>i:
                    _min = i
            else:
                self.data[self.data.index(_min)] = self.data[x]
                self.data[x] = _min
        return self.data
        
    # 5.交换法排序
    #     算法描述：选择第一位数，与其后的数一一比较，当有数符合条件这交换位置，让交换位置的数(换为第一位)继续向后比较
    #             遍历一次后，再第二位数开始以上操作，直到最后一位数。
    @jishi
    def jiaohuan(self):
        '''交换排序'''
        x = 0
        while x<len(self.data):
            for i in self.data[x:]:
                if self.data[x]>i:
                    self.data[self.data.index(i)] = self.data[x]
                    self.data[x] =i
                    break
            else:
                x+=1
        return self.data

    # 6.折半法排序(二分法)
    #     算法描述(升序)：选择序列中间值(位置中间的)，从两端[0] 和 [-1]开始分别与中间元素比较。
    #             左侧第一个元素与中间值比较，
    #             小于则取第二个元素比较，大于则交换位置;右侧相反，小于交换位置，大于不换。
    #             第一次排序后，分左右侧分别折半递归排序，直到完成。
    # @jishi
    # def zheban(self):
    #     '''折半排序'''
    #     data =list(self.data)
    #     def __zheban(data):
    #         if len(data)<2:
    #             return data
    #         mark =len(data)//2
    #         for il in range(mark):
    #             if data[il]>data[mark]:
    #                 data[il],data[mark] = data[mark],data[il]
    #         for ir in [-x for x in range(1,mark)]:
    #             if data[ir]<data[mark]:
    #                 data[ir],data[mark] = data[mark],data[ir]
    #         smaller = data[:mark]
    #         bigger = data[mark:]
    #         return __zheban(smaller) + __zheban(bigger)
    #     return __zheban(data)


if __name__=="__main__": 
    import os   
    import random


    L=[]
    for i in range(500):
        L.append(random.randint(1,1000000))

    # L=[1,5,6,8,2,6,8,9,7,4,3,0]
 
    data = PaiXu(L)

    pid = os.fork()
    if pid ==0:
        pid = os.fork()
        if pid==0:
            pid = os.fork()
            if pid==0:
                pid = os.fork()
                if pid==0:
                    pid = os.fork()
                    if pid==0:
                        data.bubble()
                        print('冒泡:')
                    elif pid>0:
                        data.jiaohuan()
                        print("交换:")
                elif pid>0:
                    data.insertion()
                    print('插入:')
            elif pid>0:
                data.quick()
                print("快速:")
        elif pid>0:
            data.xuanzi()
            print("选择:")
    elif pid>0:
        os.wait()




