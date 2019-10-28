









[TOC]





## 安装

```shell
$ yum install git-core
#或
sudo apt-get install git
```



## 环境配置

配置工具   **git config**  用来配置或读取相应的工作环境变量, 而正是由这些环境变量，决定了 Git 在各个环节的具体工作方式和行为。

这些变量可以存放在以下三个不同的地方：

- **系统级别**    `/etc/gitconfig`文件：系统中对所有用户都普遍适用的配置。若使用 **git config** 时用 *–system* 选项，读写的就是这个文件。
- **当前用户**  `~/.gitconfig` 文件：用户目录下的配置文件只适用于该用户。若使用 **git config** 时用 *–global* 选项，读写的就是这个文件。
- **当前项目**   工作目录中的 `.git/config`  文件：这里的配置仅仅针对当前项目有效。在git项目文件夹中执行 **git config**

在 Windows 系统上，Git 会找寻用户主目录下的 *.gitconfig* 文件。主目录即 *$HOME* 变量指定的目录，一般都是 *C:Documents and Settings$USER*。此外，Git 还会尝试找寻 */etc/gitconfig* 文件，只不过看当初 Git 装在什么目录，就以此作为根目录来定位。

**适用规则**

局域级别的配置都会覆盖上层的相同配置，所以 `.git/config` 里的配置会覆盖 `~/.gitconfig` 中的同名变量。



### 常用配置命令

**查看当前配置信息**

```shell
git config --list
```
**直接查阅某个环境变量的设定**    特定的名字跟在后面即可

```shell
git config user.name
```

有时候会看到重复的变量名，那就说明它们来自不同的配置文件（比如 /etc/gitconfig 和 ~/.gitconfig），不过最终 Git 实际采用的是最后一个。

**配置用户名**

```shell
git config user.name Tedu
```

**配置邮箱**

```shell
git config user.email tarena@tedu.cn
```

**配置编辑器**

```shell
git config core.editor vscode
```

**配置免密推送**

```shell
git config credential.helper store
```

**差异分析工具 **     在解决合并冲突时使用哪种差异分析工具

Git 可以理解 kdiff3，tkdiff，meld，xxdiff，emerge，vimdiff，gvimdiff，ecmerge，和 opendiff 等合并工具的输出信息。

```shell
git config merge.tool vimdiff
```



## 获取帮助

想了解 Git 的各式工具该怎么用，可以阅读它们的使用帮助，方法有三:

```shell
git help <verb>
git <verb> --help
man git-<verb>
```

比如，要学习 config 命令可以怎么用，运行:

```shell
git help config
```



## GIT仓库管理下的文件的三种状态

对于任何一个文件，在 Git 版本管理内都只有三种状态：

- 已修改（modified） 已修改表示修改了某个文件，但还没有提交保存；
- 已暂存（staged）  已暂存表示把已修改的文件放在下次提交时要保存的清单中；
- 已提交（committed） 已提交表示该文件已经被安全地保存在本地数据库中了。

文件流转的三个工作区域：Git 的工作目录，暂存区域，以及本地仓库(远程仓库)。

![../../_images/18333fig0106-tn.png](D:\notes\alpha\version_management\git.assets\18333fig0106-tn.png)

每个项目都有一个 Git 目录（译注：如果 git clone 出来的话，就是其中 .git 的目录；如果 git clone –bare 的话，新建的目录本身就是 Git 目录。），它是 Git 用来保存元数据和对象数据库的地方。该目录非常重要，每次克隆镜像仓库的时候，实际拷贝的就是这个目录里面的数据。

基本的 Git 工作流程如下：

1. 在工作目录中修改某些文件。
2. 对修改后的文件进行快照，然后保存到暂存区域。
3. 提交更新，将保存在暂存区域的文件快照永久转储到 Git 目录中。



## 创建项目的 Git 仓库

有两种取得 Git 项目仓库的方法。

1. 在现存的目录下，通过导入所有文件来创建新的 Git 仓库。
2. 从已有的 Git 仓库克隆出一个新的镜像仓库来。

### 在工作目录中初始化新仓库

要对现有的某个项目开始用 Git 管理，只需到此项目所在的目录，执行:

```shell
$ git init
```

- 初始化后，在当前目录下会出现一个名为 `.git `的目录，所有 Git 需要的数据和资源都存放在这个目录中。
- 初始化仓库的目录中的内容即可使用git进行管理
- 目前，仅仅是按照既有的结构框架初始化好了里边所有的文件和目录，但我们还没有开始跟踪管理项目中的任何一个文件。

### 从现有仓库克隆

 使用**git clone** 命令，把该项目的 *Git* 仓库复制一份出来

克隆仓库的命令格式为 **git clone [url]** 

比如，要克隆 *Ruby* 语言的 *Git* 代码仓库 *Grit*，可以用下面的命令:

```shell
$ git clone git://github.com/schacon/grit.git
```

这会在当前目录下创建一个名为 *“grit”* 的目录，其中包含一个 *.git* 的目录，用于保存下载下来的所有版本记录，然后从中取出最新版本的文件拷贝。

如果希望在克隆的时候，自己定义要新建的项目目录名称，可以在上面的命令末尾指定新的名字:

```shell
$ git clone git://github.com/schacon/grit.git mygrit
```

唯一的差别就是，现在新建的目录成了 `mygrit`，其他的都和上边的一样。



## 检查当前文件状态

**git status** 命令

**在主分支上**

```shell
On branch master  # 在主分支上
```

**尚未提交过**

```shell
No commits yet	 #尚未提交过
```

**未跟踪状态**

```shell
Untracked files:# 未跟踪的文件：
  (use "git add <file>..." to include in what will be committed)#（使用“git add<file>..”包含将提交的内容）
  file......
nothing added to commit but untracked files present (use "git add" to track)
#没有添加到提交，但存在未跟踪的文件（使用“git add”跟踪）
```

**已暂存（git add *），未提交**

```shell
No commits yet	 #尚未提交过
Changes to be committed:  #要提交的更改：
  (use "git rm --cached <file>..." to unstage) #（使用“git rm --cached <file>..”取消暂存）
  new file: file......
```

```shell
#提交过
On branch master
Changes to be committed:#要提交的更改：
	#（使用“git reset head<file>..”取消暂存）
  	(use "git reset HEAD <file>..." to unstage)
  	new file: file......
```

**已暂存（git add *），又修改**

```shell
#已跟踪文件的内容发生了变化，但还没有放到暂存区：
Changes not staged for commit:
	#（使用“git add<file>..”更新将提交的内容）
  	(use "git add <file>..." to update what will be committed)
	#（使用“git checkout--<file>…”放弃工作目录中的更改）
  	(use "git checkout -- <file>..." to discard changes in working directory)
  	modified : file......
```

**已暂存（git add *），又修改(git reset HEAD )**

```shell
$ git reset HEAD *
Unstaged changes after reset: #重置后未暂存的更改：
M       file......
```

**已提交( git  commit -m 'imfo' )**

```shell
nothing to commit, working tree clean # 无需提交，工作树干净
```

**已提交( git  commit -m 'imfo' )，又修改**

```shell
#已跟踪文件的内容发生了变化，但还没有放到暂存区：
Changes not staged for commit:
	#（使用“git add<file>..”更新将提交的内容）
  	(use "git add <file>..." to update what will be committed)
  	#（使用“git checkout--<file>…”放弃工作目录中的更改）
  	(use "git checkout -- <file>..." to discard changes in working directory)
        modified : file......
#更改还没有添加到暂存区以供提交（使用“git add 暂存”和/或“git commit -a 跳过暂存直接提交”）
no changes added to commit (use "git add" and/or "git commit -a")
```



## 忽略某些文件

创建一个名为 **.gitignore**的文件，列出要忽略的文件**模式**。

要养成一开始就设置好 *.gitignore* 文件的习惯，以免将来误提交这类无用的文件。

文件 *.gitignore* 的格式规范如下：

- 所有空行或者以注释符号 **＃ **开头的行都会被 Git 忽略。
- 可以使用标准的 glob 模式匹配。
- 匹配模式最后跟反斜杠（/）说明要忽略的是目录。
- 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。



## 版本管理流程

**工作目录下面的所有文件都不外乎这两种状态：已跟踪或未跟踪。**

- 已跟踪的文件 : 指本来就被纳入版本控制管理的文件
- 未跟踪文件 : 它们既没有上次提交时的快照，也不在当前的暂存区域。初次克隆某个仓库时，工作目录中的所有文件都属于已跟踪文件，且状态为未修改。

![](D:\notes\alpha\version_management\git.assets\18333fig0201-tn.png)

文件的状态变化周期



## 跟踪（暂存）新文件

命令 **git add** 用于跟踪（暂存）新文件（在工作区新添加或修改，删除的文件）

```shell
git add <file>
#可以一次提交多个内容，中间用空格隔开
#提交的内容可以是文件也可以是目录
#提交所有内容用 * 表示

git rm --cached [file]   (目录加 -r ) #删除暂存区的记录
git commit -m "add some message"    #将暂存区记录的修改内容同步到本地仓库
#-m 为添加的附加信息
#当工作区和本地仓库内容一致时，git status提示工作区干净
```

**跟踪就是把目标文件快照放入暂存区域，也就是 add file into staged area **



## 查看修改

 **git diff** 命令

-  **git diff**   比较工作目录中当前文件和已暂存文件的差异，也就是修改之后还没有暂存起来的变化内容。
- **git diff -–staged **    比较已暂存文件和上次提交文件的差异



## 提交更新

提交命令 **git commit**

```shell
$ git commit
#这种方式会启动文本编辑器以便输入本次提交的说明
#使用 git config –global core.editor 命令设定你喜欢的编辑软件
```

默认的提交消息包含最后一次运行 git status 的输出，放在注释行里，另外开头还有一空行，供你输入提交说明。你完全可以去掉这些注释行，不过留着也没关系，多少能帮你回想起这次更新的内容有哪些。（如果觉得这还不够，可以用 -v 选项将修改差异的每一行都包含到注释中来。）退出编辑器时，Git 会丢掉注释行，将说明内容和本次更新提交到仓库。

**可以用 -m 参数后跟提交说明的方式，在一行命令中提交更新:**

```shell
$ git commit -m "Story 182: Fix benchmarks for speed"
```

以上提交的是放在暂存区域的快照，任何还未暂存的仍然保持已修改状态，可以在下次提交时纳入版本管理。

### 跳过使用暂存区域

**git commit** 加上 -a 选项，Git 就会自动把所有已经跟踪过又修改的文件暂存起来一并提交，从而跳过 git add 步骤:

```shell
$ git status
On branch master
Changes not staged for commit:
   	modified:   file......
$ git commit -a -m 'added new benchmarks'
[master 83e38c7] added new benchmarks
 1 files changed, 5 insertions(+), 0 deletions(-)
```



## 移除文件

### 从提交中移除文件

**不保留文件**

```shell
git rm file.txt		#从已跟踪文件清单中移除文件,并连带从工作目录中删除指定的文件
git commit -m 'delect file.txt' #保存操作
```

**保留文件**

```shell
git rm --cached file.txt	#从已跟踪文件清单中移除文件,不删除工作目录中指定的文件
git commit -m 'delect file.txt' #保存操作
```

从工作目录中手工删除文件，运行 **git status** 时就会在 *“Changes not staged for commit”* 部分（也就是未暂存清单）看到:

```shell
$ rm grit.gemspec
$ git status
# On branch master
#
# Changes not staged for commit:
#   (use "git add/rm <file>..." to update what will be committed)
#
#       deleted:    grit.gemspec
#
```

然后再运行 **git rm** 记录此次移除文件的操作:

```shell
$ git rm grit.gemspec
rm 'grit.gemspec'
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#       deleted:    grit.gemspec
```

最后提交的时候，该文件就不再纳入版本管理了。

**删除之前修改过并且已经放到暂存区域的文件**

1. 保留文件更改

   ```shell
   $ git rm --cached file.txt
   # 移除文件跟踪，保留文件更改
   $ git add file.txt
   git commit -m 'delect file.txt' #保存操作
   ```

2. 强制删除,不保留更改

   ```shell
   $ git rm -f file.txt
   #强制删除选项 -f（译注：即 force 的首字母），以防误删除文件后丢失修改的内容。
   git commit -m 'delect file.txt' #保存操作
   ```

**未提交之前恢复文件**

```shell
$ git reset HEAD file.txt	#取消暂存
$ git checkout file.txt	#撤销更改
```



## 移动(重命名)文件

```shell
$ git mv file.txt file3.txt
git commit -m 'rename file.txt' #保存操作
```

运行 **git mv** 就相当于运行了下面三条命令:

```shell
$ mv README.txt README
$ git rm README.txt
$ git add README
```

有时候用其他工具批处理改名的话，要记得在提交前删除老的文件名，再添加新的文件名。



**rm  mv  的用法和shell命令rm mv 相同，操作后直接commit 同步到本地仓库**



## 查看提交历史

**git log**

默认不用任何参数的话，git log 会按提交时间列出所有的更新，最近的更新排在最上面。

```shell
$ git log
commit ca82a6dff817ec66f44342007202690a93763949  #全球唯一版本号
Author: Scott Chacon <schacon@gee-mail.com>	#作者的名字和电子邮件地址
Date:   Mon Mar 17 21:52:11 2008 -0700	#提交时间

    changed the version number	#提交说明

```

 **--pretty** 选项，可以指定使用完全不同于默认格式的方式展示提交历史。

- `oneline` 将每个提交放在一行显示，这在提交数很大时非常有用

  ```shell
  $ git log --pretty=oneline 
  5e92f8634d2247ca72eed4519458c2df1afbacbb (HEAD -> master) rename
  37236ec0bfb9a810b81796645783a8ba2fce8cea init
  ```

-  `short`   隐藏提交时间

  ```shell
  $ git log --pretty=short
  commit 5e92f8634d2247ca72eed4519458c2df1afbacbb (HEAD -> master)
  Author: weitianhua <weitianhua@antexgroup.cn>
  
      rename
  ```

- `full`    显示提交者

  ```shell
  $ git log --pretty=full
  commit 5e92f8634d2247ca72eed4519458c2df1afbacbb (HEAD -> master)
  Author: weitianhua <weitianhua@antexgroup.cn>
  Commit: weitianhua <weitianhua@antexgroup.cn>
  
      rename
  ```

- `fuller`   全部显示

  ```shell
  $ git log --pretty=fuller
  commit 5e92f8634d2247ca72eed4519458c2df1afbacbb (HEAD -> master)
  Author:     weitianhua <weitianhua@antexgroup.cn>
  AuthorDate: Mon Oct 28 19:01:00 2019 +0800
  Commit:     weitianhua <weitianhua@antexgroup.cn>
  CommitDate: Mon Oct 28 19:01:00 2019 +0800
  
      rename
  ```

- format   可以定制要显示的记录格式，这样的输出便于后期编程提取分析

  ```shell
  $ git log --pretty=format:"%h - %an, %ar : %s"
  ca82a6d - Scott Chacon, 11 months ago : changed the version number
  085bb3b - Scott Chacon, 11 months ago : removed unnecessary test code
  a11bef0 - Scott Chacon, 11 months ago : first commit
  ```

  | 选项 | 说明                                       |
  | ---- | ------------------------------------------ |
  | %H   | 提交对象（commit）的完整哈希字串           |
  | %h   | 提交对象的简短哈希字串                     |
  | %T   | 树对象（tree）的完整哈希字串               |
  | %t   | 树对象的简短哈希字串                       |
  | %P   | 父对象（parent）的完整哈希字串             |
  | %p   | 父对象的简短哈希字串                       |
  | %an  | 作者（author）的名字                       |
  | %ae  | 作者的电子邮件地址                         |
  | %ad  | 作者修订日期（可以用 -date= 选项定制格式） |
  | %ar  | 作者修订日期，按多久以前的方式显示         |
  | %cn  | 提交者(committer)的名字                    |
  | %ce  | 提交者的电子邮件地址                       |
  | %cd  | 提交日期                                   |
  | %cr  | 提交日期，按多久以前的方式显示             |
  | %s   | 提交说明                                   |

**-p** 选项展开显示每次提交的内容差异，用**-2** 则仅显示最近的两次更新,在做代码审查，或者要快速浏览其他协作者提交的更新都作了哪些改动时，就可以用这个选项。

```shell
$ git log -p -2
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number

diff --git a/Rakefile b/Rakefile
index a874b73..8f
```

**–stat**，仅显示简要的增改行数统计

```shell
$ git log --stat
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number

 Rakefile |    2 +-
 1 files changed, 1 insertions(+), 1 deletions(-)
```

结合 **–-graph 选项**，可以看到开头多出一些 ASCII 字符串表示的简单图形，形象地展示了每个提交所在的分支及其分化衍合情况。

```shell
$ git log --pretty=format:"%h %s" --graph
* 2d3acf9 ignore errors from SIGCHLD on trap
*  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
|\
| * 420eac9 Added a method for getting the current branch.
* | 30e367c timeout code and tests
* | 5a09431 add timeout protection to grit
* | e1193f8 support for heads with slashes in them
|/
* d6016bc require time for xmlschema
*  11d191e Merge branch 'defunkt' into local
```

| 选项           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| -p             | 按补丁格式显示每个更新之间的差异。                           |
| –stat          | 显示每次更新的文件修改统计信息。                             |
| –shortstat     | 只显示 –stat 中最后的行数修改添加移除统计。                  |
| –name-only     | 仅在提交信息后显示已修改的文件清单。                         |
| –name-status   | 显示新增、修改、删除的文件清单。                             |
| –abbrev-commit | 仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。            |
| –relative-date | 使用较短的相对时间显示（比如，“2 weeks ago”）。              |
| –graph         | 显示 ASCII 图形表示的分支合并历史。                          |
| –pretty        | 使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。 |



### 限制输出长度

**-<n>** 选项的写法，其中的 n 可以是任何自然数，表示仅显示最近的若干条提交。

按照时间作限制的选项，比如 –since 和 –until。下面的命令列出所有最近两周内的提交:

```
$ git log --since=2.weeks
```

你可以给出各种时间格式，比如说具体的某一天（“2008-01-15”），或者是多久以前（“2 years 1 day 3 minutes ago”）。

还可以给出若干搜索条件，列出符合的提交。用 –author 选项显示指定作者的提交，用 –grep 选项搜索提交说明中的关键字。（请注意，如果要得到同时满足这两个选项搜索条件的提交，就必须用 –all-match 选项。否则，满足任意一个条件的提交都会被匹配出来）

另一个真正实用的git log选项是路径(path)，如果只关心某些文件或者目录的历史提交，可以在 git log 选项的最后指定它们的路径。因为是放在最后位置上的选项，所以用两个短划线（–）隔开之前的选项和后面限定的路径名。

表 2-3 还列出了其他常用的类似选项。

| 选项            | 说明                         |
| --------------- | ---------------------------- |
| -(n)            | 仅显示最近的 n 条提交        |
| –since, –after  | 仅显示指定时间之后的提交。   |
| –until, –before | 仅显示指定时间之前的提交。   |
| –author         | 仅显示指定作者相关的提交。   |
| –committer      | 仅显示指定提交者相关的提交。 |

来看一个实际的例子，如果要查看 Git 仓库中，2008 年 10 月期间，Junio Hamano 提交的但未合并的测试脚本（位于项目的 t/ 目录下的文件），可以用下面的查询命令:

```
$ git log --pretty="%h - %s" --author=gitster --since="2008-10-01" \
   --before="2008-11-01" --no-merges -- t/
5610e3b - Fix testcase failure when extended attribute
acd3b9e - Enhance hold_lock_file_for_{update,append}()
f563754 - demonstrate breakage of detached checkout wi
d1a43f2 - reset --hard/read-tree --reset -u: remove un
51a94af - Fix "checkout --track -b newbranch" on detac
b0ad11e - pull: allow "git pull origin $something:$cur
Git 项目有 20,000 多条提交，但我们给出搜索选项后，仅列出了其中满足条件的 6 条。
```

## 使用图形化工具查阅提交历史

有时候图形化工具更容易展示历史提交的变化，随 Git 一同发布的 gitk 就是这样一种工具。它是用 Tcl/Tk 写成的，基本上相当于 git log 命令的可视化版本，凡是 git log 可以用的选项也都能用在 gitk 上。在项目工作目录中输入 gitk 命令后，就会启动图 2-2 所示的界面。

![../../_images/18333fig0202-tn.png](D:\notes\alpha\version_management\git.assets\18333fig0202-tn.png)

图 2-2. gitk 的图形界面 上半个窗口显示的是历次提交的分支祖先图谱，下半个窗口显示当前点选的提交对应的具体差异。











    放弃工作区的修改
        git checkout -- [file]
    
    恢复仓库文件到工作区
        git checkout [file]



版本控制命令
    回到之前版本
        git reset --hard HEAD^  回到上一个版本

        HEAD 后几个^ 表示回到之前的几个版本
    
    通过 commit_id 回到指定的版本
        git reset --hard commit_id
    
    查看操作日志    上面的最新
        git reflog 
        *获取到操作记录后可以根据commit_id去往较新的版本

标签管理
    什么是标签: 即在当前工作位置添加快照，保存项目的版本信息，
                一般用于项目版本的迭代

    创建标签
        git tag v1.0 [-m '标签信息']
        默认会在最新的commit_id处打标签
    
    查看所有标签
        git tag
    
    查看标签具体信息 
        git show 标签号
    
    在某个指定commig_id处打标签
        git tag v0.9 [commit_id]
    
    回到某个标签的版本
        git reset --hard v0.9
    
    删除某个标签
        git tag -d 标签号  

保存临时工作区
    创建临时工作区
        git stash

        *将工作区修改内容暂时封存，恢复到最近一个干净状态
    
    查看保存的工作区
        git stash list
    	>>>stash@{0}: WIP on dev: f52c633 add merge
    	上面的最新
    	
    应用某一个工作区
    	一是用	git stash apply	恢复上一个工作区，
    		也可以指定某个工作区: git stash apply stash@{index}  
    	
    	但是恢复后，stash内容并不删除，你需要用git stash drop来删除
    	
    	二是应用上一个工作区，并删除当前的
    		git stash pop
    
    删除工作区
        git stash drop stash@{index}  删某一个
        git stash clear   删所有

分支管理
    分支即每个人在获取原有分支(master)代码的基础上，作为自己的工作环境，单独开发，
    不会影响其他分支操作，开发完成后再统一合并到主线分支

    好处：安全，不影响其他人工作，自己控制进度
    问题：冲突，减低耦合度可以有效的减少冲突

查看当前分支
    git branch

    前面带 * 代表当前正在工作的分支

创建分支
    git branch [branch_name]
    分支是复制的本地仓库，如果工作区不干净，则分支与主分支不一样

切换工作分支
    git checkout [branch]

    git checkout -b [branch] 创建并切换到新的分支 

合并某分支到当前分支
    git merge [branch_name]

删除分支
    git branch -d [branch]
    普遍删除，只有分支合并后才能删

    强制删除未合并分支
    git branch -D [branch]

查看分支提交情况
	git log --graph --pretty=oneline --abbrev-commit

远程仓库的
    在远程主机上的仓库。
    git 是分布式的，每一台主机上的git结构基本相同，只是把其它主机上
       的git 仓库叫做远程仓库

创建共享仓库:
    1.创建目录
        mkdir [dirname]
    
    2.设置仓库文件夹的属主
        chown [yonghu:yonghuzu] [dirname]
    
    3.创建共享仓库
        git init --bare [aid.git]
    
    4.设置git 项目文件夹属组
        chow -R [yonghu:yonghuzu] [aid.git]

添加远程仓库
    在项目文件夹中执行
	默认 库名 origin
    git remote add origin [tarena@127.0.0.1:/home/tarena/gitrepo/aid.git]
	指定 库名 github
	git remote add github git@github.com:michaelliao/learngit.git
	
查看远程库信息	
	git remote -v

向远程主机推送分支
    git push -u origin [master]
    输入对方密码

从远程主机获取项目
    在指定文件夹内(普通文件夹)
	
	默认clone 主分支
	git clone [tarena@127.0.0.1:/home/tarena/gitrepo/aid.git]
	
	clone 指定分支
	git clone -b dev http://10.1.1.11/service/tmall-service.git


​	
​	
指定本地dev分支与远程origin/dev分支的链接，根据提示，设置dev和origin/dev的链接：
​	$ git branch --set-upstream-to=origin/dev dev
​	Branch 'dev' set up to track remote branch 'dev' from 'origin'.

将代码同步到远程主机
    git push 远程仓库名 分支名

从远程仓库拉取代码到本地
    git pull(直接合并到本地分支)
    git fetch(创建新的分支,需要自己合并)

删除已有的远程仓库
    git remote rm [origin]


github
    开源的项目社区网站，提供丰富的开源项目，也为用户提供项目管理服务

    git 是gitbub 唯一指定的代码管理工具
    
    网址 : https://github.com
    
    创建新的仓库 : 右上角 +    --》 new repository -->填写信息
    
    操作github：
        1.git remote 连接远程仓库
        2.通过 git push 上传代码
        
         * github 就是一个远程仓库


多人协作的工作模式通常是这样：

	首先，可以试图用git push origin <branch-name>推送自己的修改；
	
	如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
	
	如果合并有冲突，则解决冲突，并在本地提交；
	
	没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送就能成功！
	
	如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，
	用命令git branch --set-upstream-to <branch-name> origin/<branch-name>。	


​    
