

[TOC]





## 安装

以下部分将指导您如何在不同的操作系统上安装 GNU 的 C/C++ 编译器。这里同时提到 C/C++，主要是因为 GNU 的 gcc 编译器适合于 C 和 C++ 编程语言。

### UNIX/Linux 上的安装

如果您使用的是 **Linux 或 UNIX**，请在命令行使用下面的命令来检查您的系统上是否安装了 GCC：

```shell
$ gcc -v
```

如果您的计算机上已经安装了 GNU 编译器，则会显示如下消息：

```shell
Using built-in specs.
Target: i386-redhat-linux
Configured with: ../configure --prefix=/usr .......
Thread model: posix
gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)
```



### Mac OS 上的安装

如果您使用的是 Mac OS X，最快捷的获取 GCC 的方法是从苹果的网站上下载 Xcode 开发环境，并按照安装说明进行安装。一旦安装上 Xcode，您就能使用 GNU 编译器。

Xcode 目前可从 [developer.apple.com/technologies/tools/](http://developer.apple.com/technologies/tools/) 上下载。



### Windows 上的安装

为了在 Windows 上安装 GCC，您需要安装 MinGW。MinGw 是 Minimal GNU on Windows 的缩写，允许在 GNU/Linux 和 Windows 平台生成本地的 Windows 程序而不需要第三方运行时库。本文主要介绍 MinGw 的安装和使用。

1. 为了安装 MinGW，请访问 MinGW 的主页 [www.mingw.org](http://www.mingw.org/)，进入 MinGW 下载页面，下载最新版本的 MinGW 安装程序， mingw-get-setup.exe (86.5 kB)

2. 运行 mingw-get-setup.exe (86.5 kB) ,点击“运行”，continue等，注意记住安装的目录，如 **C:\MinGw**,下面修改环境变量时还会用到。

3. 修改环境变量: 选择计算机—属性---高级系统设置---环境变量，在系统变量中找到 Path 变量，在后面加入 min-gw的安装目录，如 **C:\MinGw\bin**

4. 在开始菜单中，点击“运行”，输入 **cmd**,打开命令行:输入 **mingw-get.exe**,如果弹出 MinGw installation manager 窗口，说明安装正常。此时，关闭 MinGw installation manager 窗口，否则接下来的步骤会报错

5. .在cmd中输入命令 **mingw-get install gcc**,等待一会，gcc 就安装成功了。如果想安装 g++,gdb,只要输入命令 **mingw-get install g++** 和 **mingw-get install gdb**

   在 cmd 中输入命令 **gcc test.c**

   在当前目录下会生成 a.exe 的可执行文件，在 cmd 中输入 a.exe 就可以执行程序了。

   如果想调试程序，可以输入 gdb a.exe

   进入 gdb 的功能，使用 gdb 常用的命令就可以调试程序了。





## vscode配置

Win10下使用 vscode 编译 c 语言，安装好 MinGW 后，在里面找到 mingw32-gcc.bin, mingw32-gcc-g++.bin, 以及 mingw32-gdb.bin 第一个是 c 语言文件的编译器，第二个是 c++ 的，第三个是用来调试编译后文件的。然后设置好环境变量，编写好 .c 文件，在 vscode 中打开 .c 文件所在的文件夹（注意是文件夹），然后配置 launch.json 文件如下所示：

```json
{

    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceRoot}/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceRoot}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "C:\\MinGW\\bin\\gdb.exe",//安装路径
            "preLaunchTask": "gcc",//tasks.json里面的名字
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
            
        }
    ]
}
```

tasks.json文件如下所示：

```json
{

    "version": "2.0.0",
    "tasks": [
        {
            "label": "gcc",
            "type": "shell",
            "command": "gcc",
            "args": [
                "-g", "${file}","-o","${fileBasenameNoExtension}.exe"
            ],
            "group":{
                "kind": "build",
                "isDefault": true
            }
        }

    ]
}
```

c_cpp_properties.json

```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**",
                "c:/mingw/bin/../lib/gcc/mingw32/8.2.0/include/c++",
                "c:/mingw/bin/../lib/gcc/mingw32/8.2.0/include/c++/mingw32",
                "c:/mingw/bin/../lib/gcc/mingw32/8.2.0/include/c++/backward",
                "c:/mingw/bin/../lib/gcc/mingw32/8.2.0/include",
                "c:/mingw/bin/../lib/gcc/mingw32/8.2.0/../../../../include",
                "c:/mingw/bin/../lib/gcc/mingw32/8.2.0/include-fixed"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "intelliSenseMode": "msvc-x64"
        }
    ],
    "version": 4
}
```





