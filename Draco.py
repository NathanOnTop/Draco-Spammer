from turtle import clear; import time; import os; import requests
from pystyle import Add, Colors, Colorate, Center, Write
from dhooks import Webhook

os.system("cls && title 𝓓𝓻𝓪𝓬𝓸 𝓢𝓹𝓪𝓶𝓶𝓮𝓻")

bannerLOL = (f"""


·▄▄▄▄  ▄▄▄   ▄▄▄·  ▄▄·           .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
██▪ ██ ▀▄ █·▐█ ▀█ ▐█ ▌▪▪         ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
▐█· ▐█▌▐▀▀▄ ▄█▀▀█ ██ ▄▄ ▄█▀▄     ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█•█▌▐█ ▪▐▌▐███▌▐█▌.▐▌    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
▀▀▀▀▀• .▀  ▀ ▀  ▀ ·▀▀▀  ▀█▄▀▪     ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
                                                     
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



