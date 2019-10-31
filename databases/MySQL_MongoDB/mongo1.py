from pymongo import MongoClient


conn = MongoClient('localhost',27017)

db = conn.stu

myset = db['class4']

print(dir(myset))
myset.insert_many([{'name':'张铁林','king':'乾隆'},
                {'name':'张国立','king':'康熙'}])
myset.insert_one({'name':'任贤齐','role':'令狐冲'})
myset.insert({'name':'古天乐','role':'杨过'})
myset.insert({'name':'李若彤','role':'小龙女'})
myset.insert({'name':'刘亦菲','role':'王语嫣'})
myset.save({'_id':1,'role':'郭靖','name':'李亚鹏'})

cursor = myset.find({'role':{'$exists':True}},{'_id':0})
for i in cursor:
    print(i)
print(cursor.next())
for i in cursor.skip(1).limit(2):
    print(i)
for i in cursor.sort([('name',1),('role',-1)]):
    print(i)

d = myset.find_one({'$or':[{'role':{'$exists':False}},{'name':"古天乐"}]})
print(d)

myset.update_one({'king':{'$exists':True}},\
            {'$set':{'name':'陈小春','king':'韦小宝'}})
myset.update_many({'king':{'$exists':True}},{'$rename':{'king':'role'}})
myset.update({'name':'张国立'},{'$set':{'name':'张卫健','role':'张三丰'}})
myset.update({'name':'高圆圆'},{'$set':{'role':'周子若'}},upsert=True)

myset.delete_one({'name':'高圆圆'})
myset.delete_many({'role':'韦小宝'})
myset.remove({'name':'张卫健'})

print(myset.find_one_and_update({'role':'萧峰'},{'$set':{'name':'黄日华'}}))




conn.close()