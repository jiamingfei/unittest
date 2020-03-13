import smtplib
from email.mime.text import MIMEText
from email.header import Header
from views.my_case import getGroupDatas
#发送邮件服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/授权密码
user = '976946614@qq.com'
password = 'cushduhnhuunbdib'
#发送邮箱
sender = '976946614@qq.com'
#接收邮箱
receiver = 'm15952973055@163.com'
#邮件主题
subject = "Python send email test"
#邮件正文
msg = MIMEText('<html><h2>上午好</h2><p>那神周爷爷，</p></html>','html','utf-8')
msg['subject'] = Header(subject,'utf-8')
#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
print(getGroupDatas("request")[1])
