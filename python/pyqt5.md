

[TOC]



PyQt5的简介
       Qt是跨平台的C++库，实现高层次的API访问的许多方面现代桌面和移动系统。这些包括定位和定位服务、多媒体、NFC和蓝牙连接、基于铬的Web浏览器以及传统的UI开发。pyqt5是一套全面的Python绑定QT V5。这是35多个扩展模块的实施使Python作为一种替代的应用程序开发语言C++在所有支持的平台包括iOS和Android。pyqt5也可以嵌入在C++应用程序允许应用程序的配置或提高这些应用程序的功能的用户。

   QtCreator(一个IDE)和QtDesigner(一个设计UI)的区别：QtCreator里集成了QtDesigner，QtCreator里有：Editor, Assistant, Designer, Debuger。因此，Qt Creator是一个IDE(只是一个开发环境而已，简单来说就是一个编写代码的地方，就像visual C++ 6.0一样。其实不用这个环境，用VS也可以的，大家有兴趣可以尝试一下)，也就是一个集成开发环境，里面有代码编写器，编译器，调试器，还有图形设计器QtDesigner，有了它你可以写软件。而Qt Designer是用来设计界面的，只能设计图形，是个图形设计器！

Qt 是一个跨平台的 C++图形用户界面库，由挪威 TrollTech 公司于1995年底出品。它既可以开发GUI程序，也可用于开发非GUI程序，比如控制台工具和服务器。Qt是面向对象的框架，使用特殊的代码生成扩展（称为元对象编译器(Meta Object Compiler, moc)）以及一些宏，Qt很容易扩展，并且允许真正地组件编程。2008年，Qt Company科技被诺基亚公司收购，Qt也因此成为诺基亚旗下的编程语言工具。2012年，Qt被Digia收购。2014年4月，跨平台集成开发环境Qt Creator 3.1.0正式发布，实现了对于iOS的完全支持，新增WinRT、Beautifier等插件，废弃了无Python接口的GDB调试支持，集成了基于Clang的C/C++代码模块，并对Android支持做出了调整，至此实现了全面支持iOS、Android、WP,它提供给应用程序开发者建立艺术级的图形用户界面所需的所有功能。基本上，Qt 同 X Window 上的 Motif，Openwin，GTK 等图形界 面库和 Windows 平台上的 MFC，OWL，VCL，ATL 是同类型的东西。



```
mainLayout->setMargin(30);  //表示控件与窗体的左右边距
mainLayout->setSpacing(40); //表示各个控件之间的上下间距
```



### QT中的setGeometry (0, 0, 30, 35) 四个参数：

从屏幕上（0，0）位置开始（即为最左上角的点），显示一个30*35的界面（宽30，高35）。

想要setGeometry有效，控件就不能在布局里。
如果使用了布局，控件大小有布局自动控制。





## 组件

### QCheckBox复选框控件

它有两个状态:打开和关闭，他是一个带有文本标签（Label）的控件。复选框常用于表示程序中可以启用或禁用的功能。

```python
def initUI(self):
	cb = QCheckBox('Show title', self)#在我们的示例中,我们将创建一个复选框,将切换窗口标题。
	cb.move(20, 20)
	cb.toggle()#这是QCheckBox的构造行数
	cb.stateChanged.connect(self.changeTitle)
#我们将自定义的changeTitle()方法连接到stateChanged信号。这个方法会切换窗体的标题。
def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
```



### 开关按钮 Toggle button

ToggleButton是QPushButton的一种特殊模式。它是一个有两种状态的按钮：按下与未按下。通过点击在这两种状态间来回切换。这种功能在某些场景会很实用。

```python
def initUI(self):    
    self.col = QColor(0, 0, 0)       
    redb = QPushButton('Red', self)
    redb.setCheckable(True)
    redb.move(10, 10)
 
    redb.clicked[bool].connect(self.setColor)
 
    greenb = QPushButton('Green', self)
    greenb.setCheckable(True)
    greenb.move(10, 60)
 
    greenb.clicked[bool].connect(self.setColor)
 
    blueb = QPushButton('Blue', self)
    blueb.setCheckable(True)
    blueb.move(10, 110)
 
    blueb.clicked[bool].connect(self.setColor)
 
    self.square = QFrame(self)
    self.square.setGeometry(150, 20, 100, 100)
    self.square.setStyleSheet("QWidget { background-color: %s }" %  self.col.name())
        
    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('Toggle button')
    self.show()
        
        
def setColor(self, pressed):
    source = self.sender()
    if pressed:
        val = 255
    else: val = 0
                        
    if source.text() == "Red":
        self.col.setRed(val)                
    elif source.text() == "Green":
        self.col.setGreen(val)             
    else:
        self.col.setBlue(val) 
            
	self.square.setStyleSheet("QFrame { background-color: %s }" %self.col.name())  
```











## 布局

PyQt5布局有两种方式，绝对定位和布局类

### 绝对定位

程序指定每个控件的位置和大小(以像素为单位)。

绝对定位有以下限制:

- 如果我们调整窗口，控件的大小和位置不会改变
- 在各种平台上应用程序看起来会不一样
- 如果改变字体，我们的应用程序的布局就会改变
- 如果我们决定改变我们的布局,我们必须完全重做我们的布局

```python
lbl1 = QLabel('Zetcode', self)
lbl1.move(15, 10)
```

我们使用move()方法来控制控件的位置。



### 框布局 Boxlayout

我们使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。



### 表格布局 QGridLayout





## 主窗口

QMainWindow 类提供了一个主要的应用程序窗口。你用它可以让应用程序添加状态栏,工具栏和菜单栏。













