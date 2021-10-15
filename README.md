# BJUF-tools工具包

> 这是北林学生所写的自动联网、报平安、出校申请脚本，旨在实现某种意义上的出入自由

## 运行环境
能跑起来python3和chrome的一切设备

## 组成

> connectLine.py:自动联网模块  
> init.py:初始化模块，包含了各种基本设置  
> mail.py：邮件发送模块，提供了邮件发送的支持  
> reportPeace.py: 报平安模块  
> run.py: 主程序  
> schoolExitApplication.py: 出校申请模块  
> 注：这里面大部分模块都可以单独调用，具体函数请阅读源码

## 使用方法  

在运行平台（电脑、服务器等，树莓派看下面）设备上安装chrome浏览器，在地址栏输入`chrome://settings/help`查看浏览器版本，在 [https://npm.taobao.org/mirrors/chromedriver/](https://npm.taobao.org/mirrors/chromedriver/) 下载对应版本对应系统的驱动包，下载，解压。将路径复制到init.py文件中的drive_path项中，并且完善init.py中的项目。执行`pip install -r requirements.txt`安装所需依赖后，运行run.py即可

## init.py

- internet_account:联网账号,元组,第一项为账号第二项为密码 例如 `internet_account=("1234567", "1234567")`  
- school_exit_application_users：需要出校申请的账号，列表嵌套元组，例如 `school_exit_application_users= [("12345678", "12345678"),("87654321","87654321")]`  
- report_peace_users:需要报平安的账号，列表嵌套元组，例如 `report_peace_users= [("12345678", "12345678"),("87654321","87654321")]`  
- drive_path:chromedriver驱动路径，例如`drive_path = 'D://chromedriver'`
- mail_sw:是否启用邮件发送，1为是，0为否
- mail_host:邮件发送的发送服务器，比如 `mail_host= 'smtp.qq.com'`
- mail_user:邮箱账号，比如` mail_user = '12345678@qq.com'`
- mail_pass:邮箱的授权码，注意是授权码不是密码，具体获得步骤请自行搜索，例如`mail_pass = 'qwertyuiop'`
- sender:邮件发送者，一般来说和`mail_user`是一样的
- receivers:邮件接受者，列表，比如`receivers= ['841546312@qq.com']`

# 树莓派使用方法
这里推荐使用树莓派官方系统raspberry，能少踩好多坑  
`pip3 install selenium``sudo apt-get install chromium-chromedriver`安装selenium以及驱动，`sudo apt install nodejs`安装js文件运行环境，安装好之后再执行`pip3 -r requirements.txt`安装其他依赖即可。
关于树莓派可以使用crontab工具定时执行，这也是作者的使用方法

### 此项目遵循GPL v3.0开源协议，使用此项目以及由此项目衍生的其他项目也须遵循该协议内容
