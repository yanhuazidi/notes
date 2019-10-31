

[TOC]



# 打包exe工具

## pyinstaller

### 安装

```shell
pip install pyinstaller
```



### 用法

windows推荐用法

```shell
pyinstaller -w -i .\bitbug_favicon.ico .\test.py
```



用法详解

```shell
pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                   [--add-data <SRC;DEST or SRC:DEST>]
                   [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                   [--hidden-import MODULENAME]
                   [--additional-hooks-dir HOOKSPATH]
                   [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                   [--key KEY] [-d {all,imports,bootloader,noarchive}] [-s]
                   [--noupx] [--upx-exclude FILE] [-c] [-w]
                   [-i <FILE.ico or FILE.exe,ID or FILE.icns>]
                   [--version-file FILE] [-m <FILE or XML>] [-r RESOURCE]
                   [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                   [--win-no-prefer-redirects]
                   [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                   [--runtime-tmpdir PATH] [--bootloader-ignore-signals]
                   [--distpath DIR] [--workpath WORKPATH] [-y]
                   [--upx-dir UPX_DIR] [-a] [--clean] [--log-level LEVEL]
                   scriptname [scriptname ...]
```



### 位置参数(必选):

`scriptname`  要处理的脚本文件的名称或仅一个规范文件。如果指定了.spec文件，则大多数选项都是不必要的，将被忽略。

### 可选参数:

|    选项     |    全称     |                             说明                             |
| :---------: | :---------: | :----------------------------------------------------------: |
|     -h      |   --help    |                      显示帮助消息并退出                      |
|     -v      |  --version  |                   显示程序版本信息并退出。                   |
| --distpath  |     DIR     |           捆绑应用程序的放置位置（默认值：.\dist）           |
| --workpath  |  WORKPATH   | 放置所有临时工作文件的位置，.log，.pyz等等（默认值：.\build） |
|     -y      | --noconfirm |  替换输出目录（默认：specpath\dist\specname），而不要求确认  |
|  --upx-dir  |   UPX_DIR   |            upx实用程序的路径（默认：搜索执行路径             |
|     -a      |   --ascii   |        不包括Unicode编码支持（默认：如果可用，包括）         |
|   --clean   |             |         在生成之前清除pyinstaller缓存并删除临时文件          |
| --log-level |    LEVEL    | 生成时控制台消息中的详细信息量。级别可以是trace、debug、info、warn、error、critical（默认值：info）之一。 |



### 要生成什么

  -D, --onedir          创建包含可执行文件的一个文件夹包（默认）
  -F, --onefile        创建一个文件绑定的可执行文件
  --specpath DIR       存储生成的规范文件的文件夹（默认：当前目录）
  -n NAME, --name NAME  要分配给捆绑应用程序和规范文件的名称（默认值：第一个脚本的basename）



捆绑内容、搜索位置：
  --add-data <SRC;DEST or SRC:DEST>
                        Additional non-binary files or folders to be added to
                        the executable. The path separator is platform
                        specific, ``os.pathsep`` (which is ``;`` on Windows
                        and ``:`` on most unix systems) is used. This option
                        can be used multiple times.
  --add-binary <SRC;DEST or SRC:DEST>
                        Additional binary files to be added to the executable.
                        See the ``--add-data`` option for more details. This
                        option can be used multiple times.
  -p DIR, --paths DIR   A path to search for imports (like using PYTHONPATH).
                        Multiple paths are allowed, separated by ';', or use
                        this option multiple times
  --hidden-import MODULENAME, --hiddenimport MODULENAME
                        Name an import not visible in the code of the
                        script(s). This option can be used multiple times.
  --additional-hooks-dir HOOKSPATH
                        An additional path to search for hooks. This option
                        can be used multiple times.
  --runtime-hook RUNTIME_HOOKS
                        Path to a custom runtime hook file. A runtime hook is
                        code that is bundled with the executable and is
                        executed before any other code or module to set up
                        special features of the runtime environment. This
                        option can be used multiple times.
  --exclude-module EXCLUDES
                        Optional module or package (the Python name, not the
                        path name) that will be ignored (as though it was not
                        found). This option can be used multiple times.
  --key KEY             The key used to encrypt Python bytecode.

### 如何生成:
  -d {all,imports,bootloader,noarchive}, --debug {all,imports,bootloader,noarchive}
                        Provide assistance with debugging a frozen
                        application. This argument may be provided multiple
                        times to select several of the following options.

                        - all: All three of the following options.
    
                        - imports: specify the -v option to the underlying
                          Python interpreter, causing it to print a message
                          each time a module is initialized, showing the
                          place (filename or built-in module) from which it
                          is loaded. See
                          https://docs.python.org/3/using/cmdline.html#id4.
    
                        - bootloader: tell the bootloader to issue progress
                          messages while initializing and starting the
                          bundled app. Used to diagnose problems with
                          missing imports.
    
                        - noarchive: instead of storing all frozen Python
                          source files as an archive inside the resulting
                          executable, store them as files in the resulting
                          output directory.

  -s, --strip           Apply a symbol-table strip to the executable and
                        shared libs (not recommended for Windows)
  --noupx               Do not use UPX even if it is available (works
                        differently between Windows and *nix)
  --upx-exclude FILE    Prevent a binary from being compressed when using upx.
                        This is typically used if upx corrupts certain
                        binaries during compression. FILE is the filename of
                        the binary without path. This option can be used
                        multiple times.



### Windows和Mac OS X特定选项
  -c, --console, --nowindowed
                       打开标准I/O的控制台窗口（默认）。在Windows上，如果第一个脚本是“.pyw”文件，则此选项无效。
  -w, --windowed, --noconsole
                        Windows和Mac OS X：不要为标准I/O提供控制台窗口。在Mac OS X上，这也会触发构建OS X.app捆绑包。在Windows上，如果第一个脚本是“.pyw”文件，则将设置此选项。在*nix系统中忽略此选项。

  -i <FILE.ico or FILE.exe,ID or FILE.icns>, --icon <FILE.ico or FILE.exe,ID or FILE.icns>
                        FILE.ico: 将该图标应用于Windows可执行文件
                        FILE.exe,ID,从exe中提取ID为的图标。
                        FILE.icns: 将图标应用于Mac OS X上的.app捆绑包

### Windows特定选项:
  --version-file FILE   add a version resource from FILE to the exe
  -m <FILE or XML>, --manifest <FILE or XML>
                        add manifest FILE or XML to the exe
  -r RESOURCE, --resource RESOURCE
                        Add or update a resource to a Windows executable. The
                        RESOURCE is one to four items,
                        FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE can be a data file
                        or an exe/dll. For data files, at least TYPE and NAME
                        must be specified. LANGUAGE defaults to 0 or may be
                        specified as wildcard * to update all resources of the
                        given TYPE and NAME. For exe/dll files, all resources
                        from FILE will be added/updated to the final
                        executable if TYPE, NAME and LANGUAGE are omitted or
                        specified as wildcard *.This option can be used
                        multiple times.
  --uac-admin           Using this option creates a Manifest which will
                        request elevation upon application restart.
  --uac-uiaccess        Using this option allows an elevated application to
                        work with Remote Desktop.



### Windows并排程序集搜索选项（高级）:
  --win-private-assemblies
                        Any Shared Assemblies bundled into the application
                        will be changed into Private Assemblies. This means
                        the exact versions of these assemblies will always be
                        used, and any newer versions installed on user
                        machines at the system level will be ignored.
  --win-no-prefer-redirects
                        While searching for Shared or Private Assemblies to
                        bundle into the application, PyInstaller will prefer
                        not to follow policies that redirect to newer
                        versions, and will try to bundle the exact versions of
                        the assembly.

### Mac OS X特定选项:
  --osx-bundle-identifier BUNDLE_IDENTIFIER
                        Mac OS X .app bundle identifier is used as the default
                        unique program name for code signing purposes. The
                        usual form is a hierarchical name in reverse DNS
                        notation. For example:
                        com.mycompany.department.appname (default: first
                        script's basename)

### 很少使用的特殊选项:
  --runtime-tmpdir PATH
                        Where to extract libraries and support files in
                        `onefile`-mode. If this option is given, the
                        bootloader will ignore any temp-folder location
                        defined by the run-time OS. The ``_MEIxxxxxx``-folder
                        will be created here. Please use this option only if
                        you know what you are doing.
  --bootloader-ignore-signals
                        Tell the bootloader to ignore signals rather than
                        forwarding them to the child process. Useful in
                        situations where e.g. a supervisor process signals
                        both the bootloader and child (e.g. via a process
                        group) to avoid signalling the child twice.