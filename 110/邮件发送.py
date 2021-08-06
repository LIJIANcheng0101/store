#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart()
message['From'] = Header("李建成", 'utf-8')  # 发送者
message['To'] = Header("贾经理", 'utf-8')  # 接收者

subject = 'Python SMTP 测试结果'
message['Subject'] = Header(subject, 'utf-8')

sender = '1322664928@qq.com'
receivers = ['2431320433@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message.attach(MIMEText('测试文件', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('银行.html', 'rb').read(),'base64', 'utf-8')
# 邮件内容
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.html"'
message.attach(att1)
try:
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpObj.login(sender,"bsptzkqfezjoigia")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")