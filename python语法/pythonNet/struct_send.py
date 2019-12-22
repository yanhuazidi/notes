

from socket import *
import struct

s = socket()
s.connect(('127.0.0.1',6666))

st = struct.Struct('i5sf6s')
data = st.pack(1,b'zhang',1.75,b'weiwei')

s.send(data)

s.close()