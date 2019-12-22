import re
import sys,os

def sys_argv():
    if len(sys.argv)<2:
        PORT = input("请输入端口:")
    else:
        PORT = sys.argv[1]
    return PORT

def files():
    _file = input("文件路径:")
    if os.path.exists(_file):
        print("======")
        with open(_file,'rb') as f:
            rb_file = f.read()
        s_file = rb_file.decode('utf-8')
        L = s_file.split('\r\n\r\n')
        return L

def regexfunc(PORT,_file):
    pattern = '^'+PORT+' '
    for s in _file:
        if re.findall(pattern,s):
            s1 = re.findall(r'address is \d+.\d+.\d+.\d+/\d+',s)
            return s1
    else:
        print("未匹配到此端口")

def main():
    PORT = sys_argv()
    fileL= files()
    s = regexfunc(PORT,fileL)
    print(s)

if __name__=="__main__":
    main()
    


