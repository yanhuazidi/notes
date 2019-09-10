[TOC]



## 编译

### Linux

1. 键入 *gcc hello.c*，输入回车，编译代码。
2. 如果代码中没有错误，命令提示符会跳到下一行，并生成 *a.out* 可执行文件。
3. 现在，键入 *a.out* 来执行程序。

```shell
$ gcc hello.c
$ ./a.out
Hello, World!
```

如果是多个 c 代码的源码文件，编译方法如下：

```shell
$ gcc test1.c test2.c -o main.out
$ ./main.out
```

test1.c 与 test2.c 是两个源代码文件。

**gcc** 命令如果不指定目标文件名时默认生成的可执行文件名为 **a.out(linux)** 或 **a.exe(windows)**。

可用 **gcc [源文件名] -o [目标文件名]** 来指定目标文件路径及文件名。

例如，**windows** 系统上，**gcc hello.c -o target/hello** 会在 **target** 目录下生成 **hello.exe** 文件(Linux 系统生成 hello 可执行文件)，**target** 目录必须已存在，**[源文件名] 和 -o [目标文件名]** 的顺序可互换， **gcc -o target/hello hello.c** 依然有效。

因编译器的原因，生成的 **.exe** 文件打开时会一闪而过，从而观察不到其运行的结果，这是因为 **main()** 函数结束时，DOS 窗口会自动关闭。为了避免这个问题可在 **return 0;** 前加入 **system("pause");** 语句。

```shell
#include <stdio.h>
#include <stdlib.h> 
int main()
{
   /* 我的第一个 C 程序 */
   printf("Hello, World! \n");
   system("pause");      //暂停函数，请按任意键继续...
   return 0;
}
```

使用 **gcc hello.c -o hello** 命令时，可不添加目标路径，则 **gcc** 即在当前工作目录自动生成 **hello.exe** 文件。



如果不想使用 system("pause")函数，可以直接使用cmd运行编译的可执行文件：

1、在 *.exe 文件目录下建一个 *.bat 文件(建一个文本文档，强制改后缀为 bat)。

2、用记事本(或其他编辑器)打开，写命令: cmd.exe cd [编译器生成的 *.exe 所在目录]。

3、运行这个 *.bat 就会自动定位到当前 exe 的目录了，接下来只要敲你自己生成的程序的名称，就可以看到结果而不闪退。

4、补充: 你也可以直接开 cmd 直接 cd 到当前目录，只要用 cmd 运行 *.exe 都可以看见结果，除非你自己编译的程序本身就无法运行。





## 编译步骤

**gcc 进行 c 语言编译分为四个步骤：**

1.预处理，生成预编译文件（.i 文件）：

```shell
gcc –E hello.c –o hello.i
```

2.编译，生成汇编代码（.s 文件）：

```shell
gcc –S hello.i –o hello.s
```

3.汇编，生成目标文件（.o 文件）：

```shell
gcc –c hello.s –o hello.o
```

4.链接，生成可执行文件：

```shell
gcc hello.o –o hello
```

有时候，进行调试，可能会用到某个步骤哦



## 怎样让C语言编写的程序生成exe文件运行时不显示cmd黑窗口

先

```
`#include <windows.h>`
```

然后调用

```
`ShowWindow(GetConsoleWindow(), SW_HIDE);`
```

```c
# include <stdio.h>
# include <stdlib.h>
#include <windows.h>
int main()
{   ShowWindow(GetConsoleWindow(), SW_HIDE);
    system("code D:/project/erp");
    return 0;
}
```





## 修改exe图标

### 修改快捷方式图标

用右键点击快捷方式文件：
1 出现属性菜单
2 点击属性
3 出现更改图标
4 点击更改图标
5 选择自己的图标
6 确定