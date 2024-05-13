#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:45
# Author    : smart
# @File     : send_email_base.py
# @Software : PyCharm
import smtplib

from email.mime.text import MIMEText

#邮件的内容
msg = MIMEText('周末不想上课!','plain','utf-8')
#发件人
msg['From'] = '3176547952@qq.com'
#收件人
msg['To'] = '3176547952@qq.com'
#邮件标题
msg['Subject'] = '邮件标题'

smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('3176547952@qq.com','wlqxddltpcxmdgje')
smtp.sendmail("3176547952@qq.com","3176547952@qq.com",msg.as_string())
smtp.quit()