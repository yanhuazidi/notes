使用 forms 模块处理表单
	1.forms模块的作用
		通过forms模块，允许将表单与class结合(表单与实体类结合)，允许通过class生成表单
	2.使用forms模块
		1.在应用中创建 forms.py 文件
		2.导入forms模块
			from django import forms
		3.创建class，一个class对应生成一个表单
			class ClassName(forms.Form):
				pass
        4.创建属性
			一个属性对应到表单中生成一个控件

                            TOPIC_CHOICE = (
                            ('1','好评'),
                            ('2','中评'),
                            ('3','差评'),
                            )
    
                            #表示评论内容的表单控件的class
                            #控件1-评论标题-文本框
                            #控件2-电子邮箱-邮件框
                            #控件3-评论内容-Textarea
                            #控件4-评论级别-下拉选择框
                            #控件5-是否保存-复选框
                            class RemarkForm(forms.Form):
                            #评论标题
                            # forms.CharField() - 文本框
                            # label : 控件前的文本标签
                            subject = forms.CharField(max_length=30,label='标题')
                            #电子邮箱
                            # forms.EmailField() - Email框
                            # label : 控件前的文本标签
                            email = forms.EmailField(label='邮箱')
                            #品论内容
                            # widget=Textarea : 将当前的单行文本框变为多行文本域
                            message = forms.CharField(label='内容',widget=forms.Textarea)
                            #品论级别
                            # forms.ChoiceField() - 下拉列表框
                            # choices : 表示当前下拉列表框中的数据,取值为元组或列表
                            topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
                            #是否保存-复选框
                            isSaved = forms.BooleanField(label='是否保存')


​		
	3.在模板中解析 form 对象
		1.注意
			在模板中，需要：
				1.自定义 <form></form>
				2.自定义 提交按钮
		2.处理方法
			1.在 views 中创建 form 的对象并发送到模板上
				form = RemarkForm()
				return render(request,'xxx.html',locals())
			2.在模板中进行解析
				1.手动解析
					{% for field in form %}
						{{field}} :
							表示的就是form对象中的一个独立属性
							表示的也就是一个独立的控件
						{{field.label}}:
							表示的是控件中的label的值
					{% endfor %}
				2.自动解析
					1.{{form.as_p}}
						将form对象中的每个属性使用p标记包裹起来再显示
					2.{{form.as_ul}}
						将form对象中的每个属性使用li标记包裹起来，再显示
						注意：必须手动提供<ol> 或 <ul>
					3.{{form.as_table}}
						将form对象中的每个属性用tr标记包裹起来，再显示
						注意：必须手动提供<table>
	                
	                    eg:
	                        {% comment '手动解析' %}
	                        <form action="/06-form/" method="post">
	                        {% csrf_token %}
	                        {% for field in form %}
	                            <p>/
	                            {{ field.label }}:{{ field }}
	                            </p>
	                        {% endfor %}
	                        <p>
	                            <input type="submit">
	                        </p>
	                        </form>
	                        {% endcomment %}
	
	                        {% comment '自动解析- {{ form.as_p }}' %}
	                        <form action="/06-form/" method="post">
	                        {{ form.as_p }}
	                        <p>
	                            <input type="submit">
	                        </p>
	                        </form>
	                        {% endcomment %}
	
	                        {% comment '自动解析- {{ form.as_ul }}' %}
	                        <form action="/06-form/" method="post">
	                        <ol>
	                            {{ form.as_ul }}
	                            <li>
	                            <input type="submit">
	                            </li>
	                        </ol>
	                        </form>
	                        {% endcomment %}


4.通过 From 类自动获取表单数据
    1. 通过 forms.Form  的子类的构造器接收表单数据
        form = RemarkForm(request.POST)

    2. 必须使 form 通过验证之后再取值
         form.is_valid()
            返回 True: 提交的数据已通过所有验证，允许取值
            返回 False : 提交的数据未通过验证，无法取值
    
    3. 获取表单的数据
        通过 : form.cleaned_data 来表示提交的数据(为字典)

5. forms 模块的高级处理
    将  Models 和 Forms 结合到一起使用
        1. 在 forms.py 中创建 class ,继承自 forms.ModelForm
        2. 创建内部类 Meta , 用于关联 Model
            1. model : 指定要关联的实体类
            2. fields : 指定要从Model中取哪些属性生成控件
                1. 取值 "__all__"
                    全部属性都要生成控件
                2. 取值 为一个列表
                    将允许生成控件的属性名放在列表中
                    ["","",""]
                3. labels : 指定每个属性所关联的 label
                    取值为字典
                    labels = {
                        '属性名':"label文本"
                        ...
                    }