[TOC]



## 后台的配置

### 创建后台管理员(超级用户):

```shell
./manage.py createsuperuser
Username : 输入用户名，默认为系统账户名
Email Address : 电子邮件
Password : 密码
Password(again) : 确认密码
```

**登录地址 ：`/admin`**



### Models 的基本管理

1. 在应用中的 admin.py 中注册要管理的实体类

   1. admin.py
      作用：注册要管理的Models类，只有注册后才能管理
   2. 注册Models
      `from .models import *`
      `admin.site.register(Entry)`

2. 修改Models提升可读性

   1. 重写每个实体类中的` __str__() `

      后台显示的将以` __str__ `的返回值为准

   2. 为实体类中的属性们增加字段选项 - `verbose_name`用于修改显示的字段名

      `name = models.CharField(max_length=30,verbose_name="姓名")`

   3. 通过Models类的内部类Meta定义其展现形式

      ```python
      class Author(models.Model):
      	... ...
      	class Meta:
      		db_table = ""
      		#指定该实体类映射到的表的名称(该属性设置完成后需要同步回数据库)
      		verbose_name = ""
      		#定义类在 admin 中显示的名字(单数)
      		verbose_name_plural = ""
      		#定义类在 admin 中显示的名字(复数)
      		ordering = ('-type', 'content','codename')
      		#指定数据在后台管理中显示的排序方式
      		#取值为一个列表，指定排序列，默认升序，降序使用-
      ```

      

   ### Models 的高级管理

   #### 在 admin.py 中创建高级管理类并注册

   1. 定义 EntryAdmin 类 ，继承自 admin.ModelAdmin

      ```python
      class AuthorAdmin(admin.ModelAdmin):
          pass
      ```

   2. 注册高级管理类

      `admin.site.register(Entry,EntryAdmin)`

   快速注册

   ```python
   @admin.register(Author)
   class AuthorAdmin(admin.ModelAdmin):
       pass
   ```

   

   #### 允许在 EntryAdmin 中增加的属性

   1. `list_display = ('name','age','email')`

      作用：定义在列表页上显示的字段们

      取值：由属性名组成的元组或列表

   2. `list_display_links`

      作用：定义在列表页上也能够链接到详情页的字段们

      取值：同上
      注意：取值必须要出现在list_display中

   3. `list_editable`

      作用：定义在列表页上就能够修改的字段们
      取值：同上
      注意：取值必须要出现在list_display中但不能出现在list_display_links中

   4. `readonly_fields`

      默认情况下，管理员将所有字段显示为可编辑的。此选项中的任何字段(应该是列表或元组)将按原样显示其数据，且不可编辑;它们也被排除在用于创建和编辑的ModelForm之外。请注意，在指定ModelAdmin时。字段或ModelAdmin。必须显示只读字段(否则将忽略它们)。

   5. `search_fields`

      作用：定义搜索栏中允许搜索的字段值们
      取值：同上

   6. `list_filter`

      作用：列表页的右侧在增加过滤器实现快速筛选
      取值：同上

   7. `date_hierarchy`

      作用：列表页的顶部增加一个时间选择器，
      取值：属性必须是 DateField 或 DateTimeField 的列

   8. `fields`

      作用：在详情页面中，指定要显示哪些字段并按照什么样的顺序显示
      取值：由属性名组成的元组或列表

      ```
      fields = (('url', 'title'), 'content')
      'url'和'title'将同行显示
      ```

   9. `exclude`

      作用：在详情页面中，指定不显示哪些字段
      取值：由属性名组成的元组或列表

   10. `fieldsets`

       作用：在详情页面中对字段们进行分组显示
       注意：fieldset 与 fields 不能共存

       取值：

       ```python
       fieldsets = (
       	#分组1
       	('分组名称',{
       			'fields': (('first_name', 'last_name'), 'address', 'city', 'state'),
       			'classes':('collapse',)
       	}),
       	#分组2
       	()
       )
       ```

       'classes'   :  `collapse` 折叠 and `wide`  宽