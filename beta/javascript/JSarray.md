

[TOC]



## Array  数组

数组是一种存储结构，可以存储一组数据，自动为每个元素分配下标，默认从0开始

JS的数组为异质数据类型,元素可以是任意类型

```javascript
var arr = new Array(10);
arr[0]={123:123}
arr[1]=function (){console.log(11111111);}
console.log(arr);
```



### 数组的分类

#### 索引数组

#### 关联数组

以字符串为下标的数组

1. 必须先创建一个空数组
           

   ```
    ```javascript
    var arr = new Array()
   ```
   ```

  ```
  
2. 以 arr['id']=1 的方式赋值

3. 取值 : 

   ```javascript
   arr.id  |  arr['id']  //不能以索引取关联元素 undefined
   赋值 ：arr.id=1111   |   arr['id']=88888     //不能以下标赋值
   ```

4. 关联数组可以与索引数组同时存在,索引数组元素始终在关联数组元素之前

   索引操作对应索引数组元素，关联操作对应关联数组元素,两者的增删改查互不相关，不会相互影响

   ```javascript
   var arr = new Array();
   arr['id']=1;
   console.log(arr);   // ['id':1]
   console.log(arr.id);    //1
   console.log(arr['id']); //1
   arr[0]=1111;    
   console.log(arr);   // [1111,'id':1]
   arr[0]=8888;
   console.log(arr);  //[88888, id: 1]
   arr[1]=8888;
   console.log(arr);  //[88888,88888, id: 1]
   ```



### 创建数组

1. 字面量方式

   ```javascript
   var arr = [10,'20',true];
   ```

2. 使用Array()内置构造方法创建,同时初始化

   ```javascript
   var arr = new Array();  // [empty]
   var arr = new Array(10,20,30);  //[10,20,30]
   //使用 new 关键字创建数组，只传一个number值时，表示指定数组长度。
   var arr = new Array(10);   // (10) [empty × 10]
   arr.length=10
   ```



### 使用

#### 数组元素的下标index

Array[index]

默认为每个元素自动分配下标，取值范围 0 ~ length-1

取值 ： arr[index]
赋值 ： arr[index] = value

#### length 属性

获取数组中元素个数，最大索引数组下标加 1, 不计算关联数组元素

```javascript
var arr = new Array();
arr['id']=1;   
arr['name']='wei';
console.log(arr.length);    // 0
arr[0]=111;
arr[3]=3333;
console.log(arr.length);    // 4
```

**JS 中数组长度是可以动态修改的，可以向数组任意一个位置插入元素，影响最终长度**

1. 对已有下标赋值，改变原始值为新值
2. 对不存在的下标赋值，js会在数组中指定的下标位置创建值，已有下标和新建下标之间的元素为空，长度为新建下标加 1

```javascript
var arr = [1,2,3]
arr[5] = 100;
console.log(arr)    // [1,2,3,<empty>,<empty>,100]
console.log(arr.length) // 6
```

**在数组的末尾添加元素，可以使用arr.length动态添加**

```javascript
arr[arr.length]=value
```

### 遍历数组

1. 普通 for 循环 , 只能遍历索引数组

   ```javascript
   for(var i=0;1<arr.length;i++){
       consoles.log(arr[i]);
   }
   ```

2. for in 获取元素下标,可以遍历索引数组和关联数组

   ```javascript
   for(var key in arr){
       key 为数组下标
   }
   ```

   ```javascript
   var arr = new Array();
   arr['id']=1;   
   arr['name']='wei';
   arr[0]=111;
   arr[3]=3333;
   console.log(arr);   //  (4) [111, empty × 2, 3333, id: 1, name: "wei"]
   for(var key in arr){
        console.log(key);
   } 
   //  0
   //  3
   //  id
   //  name
   ```

3. forEach()  方法可以遍历数组获取元素和下标，只能遍历索引数组

   ```javascript
   arr.forEach(function(element,index){
        console.log(element,index);
   });
   // 111  0
   // 3333 3
   ```



### 数组方法  忽略关联数组元素

#### toString()

将数组元素转换成字符串(包含句号)，返回字符串

```javascript
var s = arr.toString();
console.log(arr.toString());    //(4) [111, empty × 2, 3333, id: 1, name: "wei"]
//111,,,3333
```



#### join()

将数组中元素拼接成一个字符串，
参数: 可选，表示拼接分隔字符,默认为‘,’
返回值: 拼接后的字符串

```javascript
var s1 = arr.join("#");//(4) [111, empty × 2, 3333, id: 1, name: "wei"]
//111###3333
```



#### reverse()

var a = arr.reverse()
翻转数组元素，以倒序形式在原始数组地址上重新排列数组元素
返回值:为翻转后的数组 (原始数组也改变)



#### sort()

对数组中元素排序，默认按元素的Unicode码值升序排列
返回值: 排序后的数组 (原始数组也改变)
参数: 可选，可以是自定义的排序函数

```javascript
arr.sort(function (a,b){   // a 表示第一个数，b为第二个是
        return a-b;     // a-b表示数字比较升序,b-a为降序
}) 
```



#### concat(arr1,arr2,...) 

拼接两个或者更多的数组
返回值 ：拼接后的新数组，不改变原始数组
            arr.concat(arr1,arr2);

```javascript
var arr=[1,2,3,4,5],arr1 = [6,7,8,9];
var a = arr.concat(arr1)
console.log(a);
console.log(arr);
console.log(arr1);
//[1, 2, 3, 4, 5, 6, 7, 8, 9]
//[1,2,3,4,5]
//[6,7,8,9]
```



#### slice(start,end)  数组切片    [包含start,不包含end)

参数 : 一个或两个数值
返回值 : 截取的数组

var a = arr.slice(index)    截取从 index 到最后
var a = arr.slice(index1,index2)    截取从 index1 到 index2
var a = arr.slice(-index)      从倒数第index到最后
var a = arr.slice(-index1,-index2)      从倒数第index1到倒数第index2

start 超过数组下标时 返回 []



#### splice(start: number[, deleteCount?: number]\[,replace1,replace2...]) 

在指定下标处删除或插入一个或多个元素（删除包含下标元素，插入在下标元素之后插入）

参数 ： start  元素下标,可以为负数,-1 为倒数第一个
             deleteCount  删除的个数(缺省默认删除到最后，为0表示不删除,只插入元素)
             replace  在下标处插入元素,可以有多个元素(缺省不插入元素)
返回值 : 删除的元素组成的数组,不删除元素为[],改变原始数组

```javascript
1.
var arr =[1,2,3,4,5,6,7,8,9];
var b =arr.splice(1,1)
console.log(b);     // [2]
console.log(arr);   //  [1, 3, 4, 5, 6, 7, 8, 9]

2.
var b =arr.splice(1,0,'aaa','bbb')
console.log(b);   //[]
console.log(arr); //[1, "aaa","bbb", 2, 3, 4, 5, 6, 7, 8, 9]

3. 
var b =arr.splice(1,0,[10,23])
// [1, [10,23], 2, 3, 4, 5, 6, 7, 8, 9]
```



#### includes() 方法

用来判断一个数组是否包含一个指定的值，如果是返回 true，否则false。

语法:

```js
arr.includes(searchElement)
arr.includes(searchElement, fromIndex)
```

| 参数            | 描述                                                         |
| :-------------- | :----------------------------------------------------------- |
| *searchElement* | 必须。需要查找的元素值。                                     |
| *fromIndex*     | 可选。从该索引处开始查找 searchElement。如果为负值，则按升序从 array.length + fromIndex 的索引开始搜索。默认为 0。 |

如果fromIndex 大于等于数组长度 ，则返回 false 。该数组不会被搜索:

如果 fromIndex 为负值，计算出的索引将作为开始搜索searchElement的位置。如果计算出的索引小于 0，则整个数组都会被搜索。



### 数组的进出栈操作

数组采用栈结构存储

栈: 只有一个出入口，数据按顺序存入，先进后出
队列: 先进先出

#### 操作数组尾部元素

1. push(data)
        在数组的末尾添加元素，多个元素之间使用逗号隔开
        返回值 : 新数组的长度
        注意 : 直接向数组添加元素，原始数组会被改变
   
2. pop(data)
        移除数组末尾元素
        返回值: 移除的数组元素
        注意: 原始数组会被改变

#### 操作数组的头部元素

1. 在数组的头部追加元素
   unshift();
   参数: 一个或多个元素
   返回值 : 数组长度
2. 移除数组头部元素
   shift();
   返回值: 被移除的元素



### 二维数组

数组中每个元素都是数组
Array[[],[],[]]

访问:
        Array[index]\[index];

## 数组属性

| 属性                                                         | 描述                             |
| :----------------------------------------------------------- | :------------------------------- |
| [constructor](https://www.runoob.com/jsref/jsref-constructor-array.html) | 返回创建数组对象的原型函数。     |
| [length](https://www.runoob.com/jsref/jsref-length-array.html) | 设置或返回数组元素的个数。       |
| [prototype](https://www.runoob.com/jsref/jsref-prototype-array.html) | 允许你向数组对象添加属性或方法。 |

------

## Array 对象方法

| 方法                                                         | 描述                                                 |
| :----------------------------------------------------------- | :--------------------------------------------------- |
| [concat()](https://www.runoob.com/jsref/jsref-concat-array.html) | 连接两个或更多的数组，并返回结果。                   |
| [copyWithin()](https://www.runoob.com/jsref/jsref-copywithin.html) | 从数组的指定位置拷贝元素到数组的另一个指定位置中。   |
| [entries()](https://www.runoob.com/jsref/jsref-entries.html) | 返回数组的可迭代对象。                               |
| [every()](https://www.runoob.com/jsref/jsref-every.html)     | 检测数值元素的每个元素是否都符合条件。               |
| [fill()](https://www.runoob.com/jsref/jsref-fill.html)       | 使用一个固定值来填充数组。                           |
| [filter()](https://www.runoob.com/jsref/jsref-filter.html)   | 检测数值元素，并返回符合条件所有元素的数组。         |
| [find()](https://www.runoob.com/jsref/jsref-find.html)       | 返回符合传入测试（函数）条件的数组元素。             |
|                                                              |                                                      |
| [findIndex()](https://www.runoob.com/jsref/jsref-findindex.html) | 返回符合传入测试（函数）条件的数组元素索引。         |
|                                                              |                                                      |
| [forEach()](https://www.runoob.com/jsref/jsref-foreach.html) | 数组每个元素都执行一次回调函数。                     |
| [from()](https://www.runoob.com/jsref/jsref-from.html)       | 通过给定的对象中创建一个数组。                       |
|                                                              |                                                      |
| [includes()](https://www.runoob.com/jsref/jsref-includes.html) | 判断一个数组是否包含一个指定的值。                   |
| [indexOf()](https://www.runoob.com/jsref/jsref-indexof-array.html) | 搜索数组中的元素，并返回它所在的位置。               |
| [isArray()](https://www.runoob.com/jsref/jsref-isarray.html) | 判断对象是否为数组。                                 |
| [join()](https://www.runoob.com/jsref/jsref-join.html)       | 把数组的所有元素放入一个字符串。                     |
| [keys()](https://www.runoob.com/jsref/jsref-keys.html)       | 返回数组的可迭代对象，包含原始数组的键(key)。        |
| [lastIndexOf()](https://www.runoob.com/jsref/jsref-lastindexof-array.html) | 搜索数组中的元素，并返回它最后出现的位置。           |
| [map()](https://www.runoob.com/jsref/jsref-map.html)         | 通过指定函数处理数组的每个元素，并返回处理后的数组。 |
| [pop()](https://www.runoob.com/jsref/jsref-pop.html)         | 删除数组的最后一个元素并返回删除的元素。             |
| [push()](https://www.runoob.com/jsref/jsref-push.html)       | 向数组的末尾添加一个或更多元素，并返回新的长度。     |
|                                                              |                                                      |
| [reduce()](https://www.runoob.com/jsref/jsref-reduce.html)   | 将数组元素计算为一个值（从左到右）。                 |
|                                                              |                                                      |
| [reduceRight()](https://www.runoob.com/jsref/jsref-reduceright.html) | 将数组元素计算为一个值（从右到左）。                 |
| [reverse()](https://www.runoob.com/jsref/jsref-reverse.html) | 反转数组的元素顺序。                                 |
| [shift()](https://www.runoob.com/jsref/jsref-shift.html)     | 删除并返回数组的第一个元素。                         |
| [slice()](https://www.runoob.com/jsref/jsref-slice-array.html) | 选取数组的的一部分，并返回一个新数组。               |
| [some()](https://www.runoob.com/jsref/jsref-some.html)       | 检测数组元素中是否有元素符合指定条件。               |
| [sort()](https://www.runoob.com/jsref/jsref-sort.html)       | 对数组的元素进行排序。                               |
| [splice()](https://www.runoob.com/jsref/jsref-splice.html)   | 从数组中添加或删除元素。                             |
| [toString()](https://www.runoob.com/jsref/jsref-tostring-array.html) | 把数组转换为字符串，并返回结果。                     |
| [unshift()](https://www.runoob.com/jsref/jsref-unshift.html) | 向数组的开头添加一个或更多元素，并返回新的长度。     |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-array.html) | 返回数组对象的原始值。                               |