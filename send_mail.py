import smtplib
import colorama
import os
import random
from colorama import Fore, Back, Style
from prompt_toolkit import prompt


os.system('cls' if os.name == 'nt' else 'clear')

header = """
███╗   ███╗ █████╗ ██╗██╗        ██████╗███████╗███╗  ██╗██████╗ ███████╗██████╗    ██████╗ ██╗   ██╗   █████╗ ██╗     ███████╗██╗  ██╗
████╗ ████║██╔══██╗██║██║       ██╔════╝██╔════╝████╗ ██║██╔══██╗██╔════╝██╔══██╗   ██╔══██╗╚██╗ ██╔╝  ██╔══██╗██║     ██╔════╝╚██╗██╔╝
██╔████╔██║███████║██║██║       ╚█████╗ █████╗  ██╔██╗██║██║  ██║█████╗  ██████╔╝   ██████╦╝ ╚████╔╝   ███████║██║     █████╗   ╚███╔╝ 
██║╚██╔╝██║██╔══██║██║██║        ╚═══██╗██╔══╝  ██║╚████║██║  ██║██╔══╝  ██╔══██╗   ██╔══██╗  ╚██╔╝    ██╔══██║██║     ██╔══╝   ██╔██╗ 
██║ ╚═╝ ██║██║  ██║██║███████╗  ██████╔╝███████╗██║ ╚███║██████╔╝███████╗██║  ██║   ██████╦╝   ██║     ██║  ██║███████╗███████╗██╔╝╚██╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ╚═════╝ ╚══════╝╚═╝  ╚══╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
"""

colorama.init()
print(Fore.GREEN + "\n" + header + "\n")

toaddress = input("To address (separated by space) : ")
toaddress = toaddress.split(' ')
nombre_mail = len(toaddress)

username = "email@gmail.com" # change this
password = "your password" # change this
number = int(input("Number of message : "))

message = input("Votre message : ")

smtp = smtplib.SMTP('smtp.gmail.com:587')
smtp.starttls()
smtp.login(username,password)

integer = 0
while integer != nombre_mail:
    print("\nMessage to :", toaddress[integer])
    for i in range(number):
        mail_address = toaddress[integer]
        smtp.sendmail(username,mail_address,message)
        print("[-]", i + 1,': message sent')
    print("[+] All emails have been sent to", toaddress[integer], "\n----------------------------\n")
    integer += 1
print("[+] All emails have been sent to all mail address")

smtp.quit()