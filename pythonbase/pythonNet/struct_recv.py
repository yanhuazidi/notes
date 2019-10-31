

from socket import *
import struct

s = socket()
s.bind(("0.0.0.0",6666))
s.listen(5)

st = struct.Struct('i5sf6s')

print("等待连接...")
c,addr = s.accept()
print("数据：")
data = c.recv(1024)
data = st.unpack(data)
print(data)

c.close()
s.close()