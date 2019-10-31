 

[TOC]





### 操作`actions`和菜单`menus`

操作和菜单是数据库中的常规记录，通常通过数据文件声明。可以通过三种方式触发操作：

1. 通过单击菜单项（链接到特定操作）
2. 通过单击视图中的按钮（如果这些按钮连接到操作）
3. 作为对象的上下文行为

必须在XML文件中的相应菜单之前声明操作。

数据文件按顺序执行，在创建菜单之前，操作`id`必须存在于数据库中。



## 菜单	menuitem

- `id` （必填） 外部id
- `name` (必填)  在页面（菜单按钮）显示的字符
- `parent`  (子菜单必填)  父菜单外部id
- `sequence`  (选填)  同级菜单的排序优先级,默认为 10  ,越小越优先
- `web_icon` (选填)  菜单按钮背景图
- `action`   动作id
- `active`    激活,默认 true
- `groups`   权限组

### 根菜单

`static/description/icon.png`即可将使目录带背景图

```xml
<menuitem id="main_openacademy_menu" name="Open Academy weitianhua" groups="base.group_user"  web_icon="openacademy_weitianhua,static/description/icon.png"/>
```

**应用图标**

1. 'application': True
2. 所有模型加权限     .csv 文件



### 主菜单

```xml
<menuitem id="openacademy_menu" name="Open Academy weitianhua" parent="main_openacademy_menu" groups="base.group_user"/>
```



### 子菜单

```xml
<menuitem id="courses_menu" name="Courses" parent="openacademy_menu" action="course_list_action" sequence="20"/>
```

**进入app的默认视图为排第一的子菜单action视图**



## 动作视图

```xml
<record model="ir.actions.act_window" id="session_list_action">
            <field name="name">Sessions</field>
            <field name="res_model">openacademy.weitianhua.session</field>
            <field name="view_type">form</field>
            <field name="view_mode">kanban,form,calendar,gantt,graph,tree</field>
         </record>
<menuitem id="session_menu" name="Sessions" parent="openacademy_menu" action="session_list_action"/>
```

**view_mode列表为动作显示的视图,第一个为默认显示视图**





## 基础视图

### 表单	form

```xml

<record model="ir.ui.view" id="session_form_view">
        <field name="name">session.form</field>
        <field name="model">openacademy.weitianhua.session</field>
        <field name="arch" type="xml">
            <form string="Session Form">
                <sheet>
                    <group>
                        <group string="General">
                            <field name="course_id"/>
                            <field name="name"/>
                            <field name="instructor_id"/>
                        </group>
                        <group string="Schedule">
                            <field name="start_date"/>
                            <field name="duration"/>
                            <field name="seats"/>
                            <field name="taken_seats" widget="progressbar"/>
                        </group>
                    </group>
                    <label for="attendee_ids"/>
                    <field name="attendee_ids"/>
                </sheet>
            </form>
        </field>
    </record>
```



### 树视图列表  tree list

```xml
<record model="ir.ui.view" id="session_tree_view">
     <field name="name">session.tree</field>
     <field name="model">openacademy.weitianhua.session</field>
     <field name="arch" type="xml">
        <tree string="Session Tree" decoration-info="duration&lt;1" decoration-danger="duration&gt;4">
            <field name="name"/>
            <field name="course_id"/>
            <field name="duration" invisible="1"/>
            <field name="taken_seats" widget="progressbar"/>
            <field name="instructor_id"/>
            <field name="active"/>
         </tree>
      </field>
</record>
```

### 看板   kanban

```xml
<record model="ir.ui.view" id="view_openacad_session_kanban">
        <field name="name">session.kanban</field>
        <field name="model">openacademy.weitianhua.session</field>
        <field name="arch" type="xml">
            <kanban default_group_by="course_id">
                <field name="color"/>
                <templates>
                    <t t-name="kanban-box">
                        <div
                                t-attf-class="oe_kanban_color_{{kanban_getcolor(record.color.raw_value)}}
                                              oe_kanban_global_click_edit oe_semantic_html_override
                                              oe_kanban_card {{record.group_fancy==1 ? 'oe_kanban_card_fancy' : ''}}">
                            <div class="oe_dropdown_kanban">
                                <!-- dropdown menu -->
                                <div class="oe_dropdown_toggle">
                                    <i class="fa fa-bars fa-lg" title="Manage" aria-label="Manage"/>
                                    <ul class="oe_dropdown_menu">
                                        <li>
                                            <a type="delete">Delete</a>
                                        </li>
                                        <li>
                                            <ul class="oe_kanban_colorpicker"
                                                data-field="color"/>
                                        </li>
                                    </ul>
                                </div>
                                <div class="oe_clear"></div>
                            </div>
                            <div t-attf-class="oe_kanban_content">
                                <!-- title -->
                                Session name:
                                <field name="name"/>
                                <br/>
                                Start date:
                                <field name="start_date"/>
                                <br/>
                                duration:
                                <field name="duration"/>
                            </div>
                        </div>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>
```

###   日历图  	calenda

```xml
<record model="ir.ui.view" id="session_calendar_view">
        <field name="name">session.calendar</field>
        <field name="model">openacademy.weitianhua.session</field>
        <field name="arch" type="xml">
            <calendar string="Session Calendar" date_start="start_date" date_stop="end_date" color="instructor_id">
                <field name="name"/>
            </calendar>
        </field>
</record>
```

###  甘特图		gantt

```xml
 <record model="ir.ui.view" id="session_gantt_view">
    <field name="name">session.gantt</field>
    <field name="model">openacademy.weitianhua.session</field>
    <field name="arch" type="xml">
        <gantt string="Session Gantt"
               date_start="start_date" date_delay="hours"
               default_group_by='instructor_id'>
            <!-- <field name="name"/> this is not required after Odoo 10.0 -->
        </gantt>
    </field>
</record>
```

### 柱状图         graph


```xml
<record model="ir.ui.view" id="openacademy_session_graph_view">
    <field name="name">session.graph</field>
    <field name="model">openacademy.weitianhua.session</field>
    <field name="arch" type="xml">
        <graph string="Participations by Courses">
            <field name="course_id"/>
            <field name="attendees_count" type="measure"/>
        </graph>
    </field>
</record>
```





```xml
<?xml version="1.0" encoding="utf-8"?>
<openerp> 
    <!-- model 是对应的数据库表, id是你建立的view的id，这个是表单页-->  
    <record model="ir.ui.view" id="view_d_note"> 
      <!-- name 是你这个view的名字 -->  
      <field name="name">笔记本</field>  
      <!-- type是这个view的类型， form是表单类型，tree是列表类型-->  
      <field name="type">form</field>  
      <!-- 这里的model对应的是你自己建立的模型的名字 -->  
      <field name="model">demonote.demonote</field>  
      <!-- arch里面是你要包含的模型的各种数据 -->  
      <field name="arch" type="xml"> 
        <!-- 该表单的名字 和对应的版本号（这里还不清楚一般和odoo版本对应就行）-->  
        <form string="笔记" version="8.0"> 
          <!-- col有多少列 -->  
          <group col="1"> 
            <!-- 下面就是字段名字 -->  
            <field name="title"/>  
            <field name="date"/>  
            <field name="context"/>  
            <field name="type"/>  
            <!-- 这里因为是一对多的关系 inherit_id就是你要引用的view的id -->  
            <!-- 我在下面还未comment创建了一个view -->  
            <field name="comments" inherit_id="view_d_note_comment"/> 
          </group> 
        </form> 
      </field> 
    </record>  
    <!-- 这个是对应的列表页 -->  
    <record model="ir.ui.view" id="view_d_note_tree"> 
      <field name="name">笔记本列表</field>  
      <field name="model">demonote.demonote</field>  
      <field name="arch" type="xml"> 
        <tree> 
          <field name="title"/>  
          <field name="date"/>  
          <field name="comments" inherit_id="view_d_note_comment_tree"/> 
        </tree> 
      </field> 
    </record>  
    <!-- 评论的表单页 -->  
    <record model="ir.ui.view" id="view_d_note_comment"> 
      <field name="name">评论</field>  
      <field name="type">form</field>  
      <field name="model">comment.comment</field>  
      <field name="arch" type="xml"> 
        <form string="笔记" version="8.0"> 
          <group col="1"> 
            <field name="context"/>  
            <field name="time"/> 
          </group> 
        </form> 
      </field> 
    </record>  
    <!-- 评论的列表页 -->  
    <record model="ir.ui.view" id="view_d_note_comment_tree"> 
      <field name="name">评论列表</field>  
      <field name="model">comment.comment</field>  
      <field name="arch" type="xml"> 
        <tree> 
          <field name="context"/>  
          <field name="time"/> 
        </tree> 
      </field> 
    </record>  
    <!-- 这个是对应的右上角的search -->  
    <record model="ir.ui.view" id="view_d_note_search"> 
      <field name="name">查询</field>  
      <field name="model">demonote.demonote</field>  
      <field name="arch" type="xml"> 
        <search string="笔记"> 
          <!-- 可搜索的内容 -->  
          <field name="title"/>  
          <field name="context"/> 
        </search> 
      </field> 
    </record>  
    <!-- 这个是添加列表页和表单页相互转化的动作-->  
    <record model="ir.actions.act_window" id="action_d_note_contract"> 
      <field name="name">切换</field>  
      <field name="res_model">demonote.demonote</field>  
      <field name="view_type">form</field>  
      <field name="view_mode">form,tree</field>  
      <field name="view_id" ref="view_d_note_tree"/> 
    </record>  
    <!-- 这个是菜单页面，也就是你生成后能在最上面看到的那一栏-->  
    <menuitem id="demo" name="demonote" sequence="2"/>  
    <menuitem id="demo_note_sub" name="demonote管理" sequence="2" parent="demo"/>  
    <!-- 对应的action，点击后能进入 view_d_note_tree-->  
    <menuitem id="demo_denote_sub_sub" name="测试demonote" sequence="2" parent="demo_note_sub" action="action_d_note_contract"/> 
   
</openerp>

```

