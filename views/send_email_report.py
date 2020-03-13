import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from views.find_report import get_report

#发送邮件服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/授权密码
user = '976946614@qq.com'
password = 'cushduhnhuunbdib'
#发送邮箱
sender = '976946614@qq.com'
#接收邮箱
receiver =[ '563092666@qq.com','m15952973055@163.com']
#邮件主题
subject = "Python send email test"
#邮件正文
msg = MIMEText('<html><h2>上午好</h2><p>那神周爷爷，</p></html>','html','utf-8')
msg['subject'] = Header(subject,'utf-8')
msg['from'] = sender
msg['to'] = ';'.join(receiver)
new_report = get_report()[0]
send_report = open(new_report, "rb").read()

att = MIMEText(send_report, "base64", 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="%s"'%get_report()[1]
#连接发送邮件
msgroot = MIMEMultipart('releted')
msgroot ['subject'] = subject
msgroot.attach(att)
try:
    smtp = smtplib.SMTP('smtp.qq.com')
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msgroot.as_string())
    print("邮件发送成功")
    smtp.quit()
except smtplib.SMTPException as e:
    print('error', e)