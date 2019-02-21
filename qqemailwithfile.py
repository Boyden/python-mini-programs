import smtplib, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#设置服务器所需信息
#qq邮箱服务器地址
mail_host = 'smtp.qq.com'  
#qq用户名
mail_addr = input('Please input your email address:')
#密码(部分邮箱为授权码) 
mail_pass = getpass.getpass('Please input your email password:')  
#邮件发送方邮箱地址
mail_user = mail_addr.split('@')[0]
sender = mail_addr
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
rec_addr = input('Please input receiver email address:')
receivers = [rec_addr]  

#设置email信息
#邮件内容设置
message = MIMEMultipart()
#邮件主题       
message['Subject'] = 'title' 
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]

with open('test.html', 'rt') as f:
	content = f.read()
part1 = MIMEText(content,'html','utf-8')

with open('test.txt','r')as h:
    content2 = h.read()
#设置txt参数
part2 = MIMEText(content2,'plain','utf-8')
#附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
#添加照片附件
with open('test.jpg','rb')as fp:
    picture = MIMEImage(fp.read())
    #与txt文件设置相似
    picture['Content-Type'] = 'application/octet-stream'
    picture['Content-Disposition'] = 'attachment;filename="1.png"'
#将内容附加到邮件主体中
message.attach(part1)
message.attach(part2)
message.attach(picture)

#登录并发送邮件
try:
    # smtpObj = smtplib.SMTP() 
    #连接到服务器
    # smtpObj.connect(mail_host,25)
    smtpObj = smtplib.SMTP_SSL(mail_host, port=465)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误