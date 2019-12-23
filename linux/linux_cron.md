





## 周期性计划任务

1. 进入周期性计划任务

   $ crontab -e 
     按 4 

   1. 设置周期性计划任务

   ------

   分  时  日  月  周
   分 : 0-59
   时 : 0-23
   日 : 1-31
   月 : 1-12
   周 : 0-6

   - : 所有可能值
     , : 指定多个时间点
       1,5 * * * * : 01分和05分(分钟)
     / : 指定时间间隔频率
       */10 * * * * : 每隔10分钟
       */10 * 1,5 1 * : 1月1号和1月5号每隔10分钟

   - : 指定一个时间段
     0 0-6/1 * * * : 0-6点之间每隔1个小时

   1. 每分钟执行1次01.py

   - - - - - pyhon3 绝对路径

   1. 每个周末的0点0分执行backup.py

   0 0 * * 0,6 python3 /backup.py

   1. 每天18:00-23:00之间,每小时执行01.py

   0 18-23/1 * * * python3 /01.py

2. awk的使用(按行去执行动作)

3. 语法格式 : awk [选项] '动作' 文件列表

4. 用法 : Linux命令 | awk [选项] '动作'

5. 使用示例

   1. awk '{print "abc"}' a.sh
      1. df -h | awk '{print $1}'
         1. awk -F ":" '{print $2}' a.sh
            a.sh内容
            echo:123
            echo:456
                   4. 显示本机的IP地址 
                      `ifconfig | head -2 | tail -1 | awk '{print $2}' | awk -F ":" '{print $2}'`
                   5. nginx的访问日志
                      /var/log/nginx/access.log
   2. 把访问过自己的IP地址给输出来
      awk '{print $1}' access.log
   3. 统计有多少个IP访问过我
      awk '{print $1}' access.log | sort | uniq | wc -l
   4. 统计每个IP地址访问的次数,把访问最多的前2个IP输出出来
      awk '{print $1}' access.log | sort | uniq -c | sort -rnk 1 | head -2
      1. sort的参数
   5. sort : 排序
   6. sort | uniq -c : 去重,统计每行次数
   7. sort -n : 以数值方式来排序
   8. sort -n -k 1 : 按照第1列来排序
   9. sort -r  : 倒序排列