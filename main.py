##Credits: nuker
##Discord: @yen
##Github: yencommits

#imports
from dhooks import Webhook
import time
import os
from colorama import Fore, Back, Style
import platform
import sys
import datetime
from time import sleep
loading = 0
cmd = 'mode 50,50'
os.system(cmd)


#function load
def load():
    bar = [Fore.LIGHTCYAN_EX + "|", Fore.LIGHTCYAN_EX + "/", Fore.LIGHTCYAN_EX + "-", Fore.LIGHTCYAN_EX + "\\"]
    for _ in range(20):
        for char in bar:
            print(f"\rLoading xem please wait: {char} {Fore.RESET}", end="", flush=True)
            time.sleep(0.1)
    


#function clear
def clear():
    if platform.system() == 'Windows':
        os.system('cls & title xem.gg')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;xem.gg\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo - n - e "\033]0;xem.gg\007"''')  # change title


#function .1
def option1():
  clear()
  print(Fore.LIGHTCYAN_EX + """
                                        ,--.
                                       {    }
                                       K,   }
                                      /  ~Y`
                                 ,   /   /
                                {_'-K.__/
                                  `/-.__L._
                                  /  ' /`\_}
                                 /  ' /
                         ____   /  ' /
                  ,-'~~~~    ~~/  ' /_
                ,'             ``~~~  ',
               (                        Y
              {                         I
             {      -                    `,
             |       ',                   )
             |        |   ,..__      __. Y
             |    .,_./  Y ' / ^Y   J   )|
             \           |' /   |   |   ||
              \          L_/    . _ (_,.'(
               \,   ,      ^^""' / |      )
                 \_  \          /,L]     /
                   '-_~-,       ` `   ./`
                      `'{_            )
                          ^^\..___,.--`
      


            ██╗  ██╗███████╗███╗   ███╗
            ╚██╗██╔╝██╔════╝████╗ ████║
             ╚███╔╝ █████╗  ██╔████╔██║
             ██╔██╗ ██╔══╝  ██║╚██╔╝██║
            ██╔╝ ██╗███████╗██║ ╚═╝ ██║
            ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝                                 
""")
  print("――――――――――――――――――――――――――――――――――――――――――――――――――")
  print(Fore.RESET + "     made by " + Fore.LIGHTCYAN_EX + "yen " + Fore.RESET + "| discord: " + Fore.LIGHTCYAN_EX + "dsc.gg/uXA6hz97bR" + Fore.RESET)
  webhookurl = Webhook(input(Fore.RESET + "[spammer] webhook url:" + Fore.LIGHTCYAN_EX + " "))
  message = input(Fore.RESET + "[spammer] message:" + Fore.LIGHTCYAN_EX + " ")
  delay = int(input(Fore.RESET + "[spammer] delay:" + Fore.LIGHTCYAN_EX + " "))


  clear()
  #webhookspam
  while True:
    time.sleep(delay)
    webhookurl.send(message)
    print( "sent: " + message)
#time


#ui
e = datetime.datetime.now()
now = datetime.datetime.now()
load()
print()
print(Fore.LIGHTCYAN_EX + "[" + Fore.RESET + "+" + Fore.LIGHTCYAN_EX + "] " + Fore.RESET + "loaded xem starting ui")
time.sleep(2)
clear()
print(Fore.LIGHTCYAN_EX + """
                                        ,--.
                                       {    }
                                       K,   }
                                      /  ~Y`
                                 ,   /   /
                                {_'-K.__/
                                  `/-.__L._
                                  /  ' /`\_}
                                 /  ' /
                         ____   /  ' /
                  ,-'~~~~    ~~/  ' /_
                ,'             ``~~~  ',
               (                        Y
              {                         I
             {      -                    `,
             |       ',                   )
             |        |   ,..__      __. Y
             |    .,_./  Y ' / ^Y   J   )|
             \           |' /   |   |   ||
              \          L_/    . _ (_,.'(
               \,   ,      ^^""' / |      )
                 \_  \          /,L]     /
                   '-_~-,       ` `   ./`
                      `'{_            )
                          ^^\..___,.--`
      


            ██╗  ██╗███████╗███╗   ███╗
            ╚██╗██╔╝██╔════╝████╗ ████║
             ╚███╔╝ █████╗  ██╔████╔██║
             ██╔██╗ ██╔══╝  ██║╚██╔╝██║
            ██╔╝ ██╗███████╗██║ ╚═╝ ██║
            ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝                                  
""")
print("――――――――――――――――――――――――――――――――――――――――――――――――――")
print(Fore.RESET + "     made by " + Fore.LIGHTCYAN_EX + "yen " + Fore.RESET + "| discord: " + Fore.LIGHTCYAN_EX + "dsc.gg/uXA6hz97bR" + Fore.RESET)
print(Fore.RESET + "               connected to: " + Fore.LIGHTCYAN_EX + "nobody")


#choices
print()
print()
print(Fore.LIGHTCYAN_EX + "         1." + Fore.RESET + " Webhook Spammer")


#choice input
choice = int(input("          choice:" + Fore.LIGHTCYAN_EX + " "))
if choice == 1:
  option1()


