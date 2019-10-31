

## 启动配置

**odoo.conf**

```python
[options]
addons_path = odoo\addons,addons,public,
admin_passwd = admin
csv_internal_sep = ,

data_dir = C:\Users\Administrator\AppData\Local\OpenERP S.A\Odoo


http_host='0.0.0.0'
http_port=8069
http_enable = True
http_interface = 
longpolling_port=8072


pg_path=E:\postgresql\11\bin
db_host=localhost
db_port=5432
db_name=erp
db_user=odoo
db_password=odoo
db_maxconn = 64
db_sslmode = prefer
db_template = template0

#without_demo=True
demo=True
#load_language=zh_CN

email_from = False
geoip_database = /usr/share/GeoIP/GeoLite2-City.mmdb

import_partial = 
limit_memory_hard = None
limit_memory_soft = None
limit_request = None
limit_time_cpu = None
limit_time_real = None
limit_time_real_cron = None


list_db = True
log_db = False
log_db_level = warning
log_handler = :INFO
log_level=warn
logfile = None
logrotate = False
max_cron_threads = 2
osv_memory_age_limit = 1.0
osv_memory_count_limit = False
pidfile = None
proxy_mode = False
reportgz = False
server_wide_modules = base,web


smtp_server = localhost
smtp_port = 25
smtp_ssl = False
smtp_user = False
smtp_password = False


syslog = False
test_enable = False
test_file = False
test_tags = None
translate_modules = ['all']
unaccent = False

without_demo = False
workers = None
```









## VScode 配置

**settings.json**

```json

{
    //使用这个，所以自动完成/转到定义将与python扩展
    "python.autoComplete.extraPaths": [
        "${workspaceRoot}/odoo/addons",
        "${workspaceRoot}/odoo"],

    "python.linting.pylintPath": "pylint", //可选：如果您有环境路径，则使用Python的路径“
    "python.pythonPath": "env\\Scripts\\python.exe",
    "python.linting.enabled": true,

    //加载pylint_odoo
    "python.linting.pylintArgs": ["--load-plugins", "pylint_odoo"],
    "python.formatting.provider": "yapf",   //一键美白代码格式
    //"python.formatting.yapfPath“：”可选：如果你有环境路径，使用Python的路径“，
    //“python.linting.pep8Path”：“可选：如果您有环境路径，则使用Python的路径”，
    "python.linting.pep8Enabled": false,

    //添加这个自动保存选项，以便在编辑时pylint会播放错误
    //它只会显示文件保存的错误
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 500,

    //下面将在编辑器中隐藏已编译的文件/添加其他文件以将其从编辑器中隐藏
    "files.exclude":{
        "**/*.pyc": true
    },
    "python.linting.pylintEnabled": true,
    "restructuredtext.confPath": "",
    "restructuredtext.experimental": true
}
```

**launch.json**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "odoo",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "pythonPath": "${workspaceRoot}/env/Scripts/python.exe",
            "program": "${workspaceRoot}/odoo-bin",
            "cwd": "${workspaceRoot}",
            // "env": {},
            // "envFile": "${workspaceRoot}/.env",
            "args": [
                "-c",
                "${workspaceRoot}/odoo.conf",
                // "-u",
                //"om_purchase",
                //"om_purchase_quotation",
                //"om_purchase_requisition_portal",
                //"om_purchase_delivery",
                //"om_info_pages",
                //"om_portal_product",
                //"om_payment_alipay"
                //"website_payment_weixin",
                //"kwn_pos_restaurant",
                //"antex_membership,antex_membership_payment"
                ],
        }
    ],
    "compounds": []
}
```













