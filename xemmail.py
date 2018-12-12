from gmail import GMail,Message
from random import randint

sick_list = ["thuong han","kiet li","tieu chay"]
x = randint(0,len(sick_list)-1)
sickness = sick_list[x]
#1 chon 1  ngau nhien benh



html_template = '''

<p>chao xep,</p>
<p>sang nay em bi om xep cho em nghi om nha&nbsp;</p>
<p>em bi {{sick_list[x]}}</p>


'''
html_content = html_template.replace("{{sick_list[x]}}",sickness)
#2 tu benh ket hop voi html_template ra 1 html_content
#3 goi y google: string replace



mail = GMail("sonnguyentl1810@gmail.com","18101998son")
# msg = Message("Alo", to ="c4e.techkidsvn@gmail.com",text="chao anh huy")
msg = Message("Alo",to ="thaisonnguyentl@gmail.com",html=html_content)
mail.send(msg)