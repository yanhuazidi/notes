#coding=utf-8
'''逻辑门
与门(AND gate)有两个输入端，每一个都可以是0 或者1（代表假或者真）。
    如果输入值都是1，则输出是1。如果输入值有一个是0 或者两个都是0，那么输出是0。
或门(OR gate)同样也有两个输入端，如果输入有一个1 或者两个都是1，
    那么输出1。只有两个输入都是0，结果才是0。
非门(NOT gate)与其它两个门不同的是它只有一个输入端，输出值刚好与输入值相反。如果输入0，
'''


class LogicGate:
    def __init__(self,label):
        self.label = label  #标签区别不同的逻辑
        self.output = None

    def getLabel(self):
        '''获取实例标签'''
        return self.label

    def getOutput(self):
        '''根据逻辑类别输出'''
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    '''双输入逻辑门类'''
    def __init__(self,label):
        LogicGate.__init__(self,label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        '''B输入口'''
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    '''单输入逻辑门类'''
    def __init__(self,label):
        LogicGate.__init__(self,label)
        self.pin = None

    def getPin(self):
        '''一个输入口'''
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
    '''and 逻辑门类'''
    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):
        pinA = self.getPinA()
        pinB = self.getPinB()
        if pinA==1 and pinB==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    '''or 逻辑门类'''
    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):
        pinA = self.getPinA()
        pinB = self.getPinB()
        if pinA==1 or pinB==1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    '''not 逻辑门类'''
    def __init__(self,label):
        UnaryGate.__init__(self,label)

    def performGateLogic(self):
        pin = self.getPin()
        if pin ==0:
            return 1
        else:
            return 0


class Connector:
    '''单连接器类,实现两个逻辑门类的连接'''
    def __init__(self, fgate, tgate):
        '''fromgate与togate是两个逻辑门实例'''
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


if __name__=='__main__':
    # g1 = AndGate("G1")
    # print(g1.getOutput())
    # g2 = OrGate("G2")
    # print(g2.getOutput())
    # g3 = NotGate("G3")
    # print(g3.getOutput())
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())