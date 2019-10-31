







```c
//dlltest.c
int Double(int x)
{
    return x * 2;
}
```

下面的命令行将这个代码编译成 dll

```shell
gcc dlltest.c -shared -o dlltest.dll -Wl,--out-implib,dlltest.lib
```


其中 -shared 告诉gcc dlltest.c 文件需要编译成动态链接库。-Wl 表示后面的内容是ld 的参数，需要传递给 ld。 --out-implib,dlltest.lib 表示让ld 生成一个名为 dlltest.lib 的导入库。

如果还需要 .def 文件，则上面的命令行可以写为：

```shell
gcc dlltest.c -shared -o dlltest.dll -Wl,--output-def,dlltest.def,--out-implib,dlltest.a
```

```c
//main.c
#include <stdio.h>
int Double(int x);
int main(void)
{
        printf("Hello :%d\n", Double(333));
        return 0;
}
```

```shell
gcc main.c dlltest.lib -o main.exe
```

实际上，如果我们的dll文件只是被MinGW gcc使用。都不需要生成 dlltest.lib。直接在编译的时候将 dlltest.dll 加进去就行了。

```shell
gcc main.c dlltest.dll -o main.exe
```



如果在程序中动态加载dll。那么代码可以这么写：

//m2.c
define UNICODE 1

#include <windows.h>
#include <stdio.h>

```c
typedef int (*INT_FUNC)(int);
int main(void)
{
	INT_FUNC db;
	HINSTANCE hInstLibrary = LoadLibrary(L"dlltest.dll");
	printf("LoadLibrary\n");
	db = (INT_FUNC)GetProcAddress(hInstLibrary, "Double");
	printf("Hello :%d\n", db(333));
	FreeLibrary(hInstLibrary); 
	return 0;
}
```

编译的时候更不需要dlltest.lib 了，甚至都不需要 dlltest.dll

```shell
gcc m2.c -o m2.exe
```



https://www.cnblogs.com/chengjian-physique/p/9835924.html









