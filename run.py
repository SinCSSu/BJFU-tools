import schoolExitApplication as sea
import connectLine
import reportPeace as rp
import mail
import init
import datetime
import codecs
from prettytable import PrettyTable

if connectLine.connect() != 1:
    f = open("errorlog.log", "w")
    f.write("connect error")
    f.close()
    exit()

ls_1 = sea.run()
ls_2 = rp.run()

content = PrettyTable()
content.field_names = ["用户", "应用", "状态"]
for us in ls_1:
    if us[1] == 1:
        content.add_row([us[0], "出校申请", "成功"])
    elif us[0] == 0:
        content.add_row(us[0], "出校申请", "超时")
    else:
        content.add_row(us[0], "出校申请", "失败")
for us in ls_2:
    if us[1] == 1:
        content.add_row([us[0], "报平安", "成功"])
    elif us[0] == 0:
        content.add_row(us[0], "报平安", "超时")
    else:
        content.add_row(us[0], "报平安", "失败")
# content = "|用户|应用|状态|\n"
# for us in ls_1:
#     content += "|{}|{}|{}|\n".format(us[0], "出校申请", us[1])
#
# for us in ls_2:
#     content += "|{}|{}|{}|\n".format(us[0], "报平安", us[1])

if init.mail_sw == 1:
    mail.send_mail(content.get_string())
tm = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
with codecs.open("log.log", "a+", "utf-8") as f:
    f.write(tm + '\n' + content)
