import datetime
from gmail import GMail,Message
time_now = datetime.datetime.now()

html_content = '''
<p>ch&agrave;o sếp&nbsp;</p>
<p>h&ocirc;m nay em bị ốm , anh cho em nghỉ l&agrave;m .em phải đi gặp b&aacute;c sĩ&nbsp;</p>

'''
mail = GMail("sonnguyentl1810@gmail.com","18101998son")
msg = Message("Nghi om",to ="doanhtuan7198@gmail.com",html=html_content)
if time_now.hour > 7:
    mail.send(msg)
else:
    print("chưa đến 7 h")