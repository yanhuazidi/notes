
https://www.cnblogs.com/yyds/p/7072492.html



# shake_128([string]) -> SHAKE object
#      |  
#      |  Return a new SHAKE hash object.
#      |  
#      |  Methods defined here:
#      |  
#      |  __new__(*args, **kwargs) from builtins.type
#      |      Create and return a new object.  See help(type) for accurate signature.
#      |  
#      |  copy(self, /)
#      |      Return a copy of the hash object.
#      |  
#      |  digest(self, /, length)
#      |      Return the digest value as a string of binary data.
#      |  
#      |  hexdigest(self, /, length)
#      |      Return the digest value as a string of hexadecimal digits.
#      |  
#      |  update(self, obj, /)
#      |      Update this hash object's state with the provided string.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  block_size
#      |  
#      |  digest_size
#      |  
#      |  name

#     md5 = openssl_md5(...)
#         Returns a md5 hash object; optionally initialized with a string
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示

#由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的
#常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
   return md5(password + 'the-Salt')
如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
        get_md5(password + username + 'the-Salt')
    
#     new = __hash_new(name, data=b'', **kwargs)
#         new(name, data=b'') - Return a new hashing object using the named algorithm;
#         optionally initialized with data (which must be bytes).
    
#     pbkdf2_hmac(...)
#         pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) -> key
        
#         Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as
#         pseudorandom function.
    
#     sha1 = openssl_sha1(...)
#         Returns a sha1 hash object; optionally initialized with a string
        SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
    
#     sha224 = openssl_sha224(...)
#         Returns a sha224 hash object; optionally initialized with a string
    
#     sha256 = openssl_sha256(...)
#         Returns a sha256 hash object; optionally initialized with a string
    
#     sha384 = openssl_sha384(...)
#         Returns a sha384 hash object; optionally initialized with a string
    
#     sha512 = openssl_sha512(...)
#         Returns a sha512 hash object; optionally initialized with a string



#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，
#把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
#要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
#但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。

user_password='wei'

from hashlib import sha1,sha512	# 加密模块

s1 = sha1() #创建并返回一个sha1对象，<sha1 HASH object @ 0x000002A4C25FFA58>
print(s1.hexdigest())   #以十六进制返回sha1对象  da39a3ee5e6b4b0d3255bfef95601890afd80709
print(s1.digest())   #以二进制返回sha1对象  b'\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t'
print(s1.block_size)    #返回  64
print(s1.digest_size)   #  20
print(s1.name)      #  sha1



s1.update(user_password.encode("utf8"))  #用给定的字符串修改sha1对象
print(s1.hexdigest())   #8fa8838ab83387ae867845f542b9fe9ca04873f0

s2 = s1.copy()  #返回sha1对象的副本，操作不会改变原对象
s3 = s1    #增加对sha1对象的引用，操作会改变原对象


s5 = sha1()
s5.update('wei'.encode("utf8"))
if s5.hexdigest()==s1.hexdigest():
    print('-----------------------')

s512 = sha512()
print(s512.hexdigest())

