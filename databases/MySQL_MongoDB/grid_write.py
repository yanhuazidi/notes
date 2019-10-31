from pymongo import MongoClient
import gridfs 

#获取数据库对象
conn = MongoClient('localhost',27017)
db = conn.grid

#获取文件集合对象
fs = gridfs.GridFS(db)

#将本地文件读取出来写入到数据库中
with open('img_5.jpg','rb') as f:
    fs.put(f.read(),filename='mm.jpg')

conn.close()


