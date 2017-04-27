#! /home/python35/bin/python

import smtplib
from email.mime.text import MIMEText
import sys

# for remote debug
#import pydevd
#pydevd.settrace('192.168.27.92', port=10088, stdoutToServer=True, stderrToServer=True)


mail_host = 'mail.abc.com'	    #配置邮箱host
mail_user = 'zhangsan'	    #用户名
mail_pass = 'XXXXX'
mail_postfix = 'xyz.cn'	    #邮箱后缀



def send_mail(to_list, subject, content):
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user+'@'+mail_postfix, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])