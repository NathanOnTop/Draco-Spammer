from turtle import clear; import time; import os; import requests
from pystyle import Add, Colors, Colorate, Center, Write
from dhooks import Webhook

os.system("cls && title ๐๐ป๐ช๐ฌ๐ธ ๐ข๐น๐ช๐ถ๐ถ๐ฎ๐ป")

bannerLOL = (f"""


ยทโโโโ  โโโ   โโโยท  โโยท           .โโ ยท  โโโยท โโโยท โข โ โ ยท. โข โ โ ยท. โโโ .โโโ  
โโโช โโ โโ โยทโโ โโ โโ โโชโช         โโ โ. โโ โโโโ โโ ยทโโ โโโโโชยทโโ โโโโโชโโ.โยทโโ โยท
โโยท โโโโโโโ โโโโโ โโ โโ โโโโ     โโโโโโ โโโยทโโโโโ โโ โโโโโยทโโ โโโโโยทโโโโชโโโโโ 
โโ. โโ โโโขโโโโ โชโโโโโโโโโโ.โโ    โโโโชโโโโโชยทโขโโ โชโโโโ โโโโโโโโ โโโโโโโโโโโโโโขโโ
โโโโโโข .โ  โ โ  โ ยทโโโ  โโโโโช     โโโโ .โ    โ  โ โโ  โโชโโโโโ  โโชโโโ โโโ .โ  โ
                                                     
""")
text = " A Webhook Spammer\n Made By Termed$#0001\n"
x = Add.Add(bannerLOL, text, 3)
print(Colorate.Horizontal(Colors.blue_to_cyan, str(x), 1))
print('');print('')

webhook = input(Colorate.Horizontal(Colors.blue_to_cyan,"webhook?: "))
message = input(Colorate.Horizontal(Colors.blue_to_cyan,"Message to spam?: "))
name = input(Colorate.Horizontal(Colors.blue_to_cyan,"Webhook Username?: "))
profile = input(Colorate.Horizontal(Colors.blue_to_cyan,"Webhook Image?: "))
print(Colorate.Horizontal(Colors.blue_to_cyan, "Thanks For using My tool! :)"))
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

webhookPlayload = {
            'content': message,
            'username': name,
            'avatar_url': profile,
        }


while True:
            try:
                time.sleep(0.5)
                r = requests.post(webhook, json=webhookPlayload)
                if r.status_code == 204:
                    print(Colorate.Horizontal(Colors.red_to_yellow, "[+] Message Sent!"))
                else:
                    print(Colorate.Horizontal(Colors.red_to_green, "[+] Ratelimit!"))
            except requests.exceptions.MissingSchema:
                print("False Webhook Url! ")
                exit()



