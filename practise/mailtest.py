from flask_mail import Message
from hello import *

msg = Message('test mail', sender='401316161@qq.com',
              recipients=['401316161@qq.com'])

# taoqiqwynvupjbohncbag
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)
