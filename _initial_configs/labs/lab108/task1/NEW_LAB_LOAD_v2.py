
#!/usr/bin/env python

import telnetlib
import threading
import os.path
import time
import sys
import os


print("""
Script works under following conditions:
1) <!!!> YOU MUST PUT in FOLDER CFG-files (!)ONLY(!) for NODEs used in LAB, DONT CHANGE FILENAMEs!!!
2) <!!!> DONT Forget power-on these NODEs
""")
print("""  
This is your current Working Directory:"""
,os.getcwd())

input("""

Dou you PUT CFGs to this folder ?
If true, PRESS Enter Button:

""")


IP = input("""
           
====>Enter IP-Address your UNL VM:""")

print("""
(!!!) wait about 100 Seconds  and DONT TOUCH your KEYBOARD at this TIME, dear SIR/MISS/MISSIS/""")




def open_telnet_conn(IP , TELNET_PORT, router_file):
    try:
            #Define telnet parameters

        TELNET_TIMEOUT = 5
        READ_TIMEOUT = 5
        
        #Connection to SW and Router
        connection = telnetlib.Telnet(IP, TELNET_PORT, TELNET_TIMEOUT)
        
        #Executing command for erasing startup purposes
        
        output = connection.read_until(b"no:", READ_TIMEOUT)
        connection.write(("no\n").encode('ascii'))
        time.sleep(3)
        connection.write(("enable\n").encode('ascii'))
        time.sleep(1)
        connection.write(("\r\n").encode('ascii'))
        time.sleep(1)
        
        connection.write(("write\n").encode('ascii'))
        time.sleep(1)

        
        connection.write(("enable\n").encode('ascii'))
        time.sleep(1)
        connection.write(("erase startup-config\n").encode('ascii'))
        time.sleep(1)
        connection.write(("\r\n").encode('ascii'))
        time.sleep(1)
        
        #Executing commands for reloading purposes        
        connection.write((" reload\n").encode('ascii'))
        time.sleep(1)
        connection.write(("\r\n").encode('ascii'))
        time.sleep(30)
        
      
        #Say NO to VODKA AHAHAHA
        output = connection.read_until(b"no:", READ_TIMEOUT)
        connection.write(("no\n").encode('ascii'))
        time.sleep(3)
        
        #output = connection.read_until(b"down:", READ_TIMEOUT)
        connection.write(("\r\n").encode('ascii'))
        time.sleep(2)
        
        connection.write(("enable\n").encode('ascii'))
        time.sleep(1)
 

        connection.write(("configure terminal\n").encode('ascii'))
        time.sleep(3)

        
        for each_line in router_file.readlines():
            connection.write((each_line + '\n').encode('ascii'))
            time.sleep(0.5)
        time.sleep(1)
        
                
        connection.write(("write\n").encode('ascii'))
        time.sleep(1)

        connection.close()
        
    except  IOError:
        print ("PLS CHECK,MAYBE YOU LOAD NONEEDED FILES to the FOLDER, OR FILES WITH BAD CHANGED/BAD NAMES")


LIST= []
a = []
for each_file in os.listdir():
     if each_file.endswith('.txt'):
        a.append(each_file)
        
        
for each_element in a:
    if each_element == "r1.txt" :
        r1 = open("r1.txt", "r")
        LIST.append(('32769', r1))
        
     
    if each_element == "r2.txt" :
        r2 = open("r2.txt", "r")
        LIST.append(('32770', r2))
         

    if each_element == "r3.txt" :
        r3 = open("r3.txt", "r")
        LIST.append(('32771', r3))
         

    if each_element == "r4.txt" :
        r4 = open("r4.txt", "r")
        LIST.append(('32772', r4))
         
     
    if each_element == "r5.txt" :
        r5 = open("r5.txt", "r")
        LIST.append(('32773', r5))
         

    if each_element == "r6.txt" :
        r6 = open("r6.txt", "r")
        LIST.append(('32774', r6))
         

    if each_element == "r7.txt" :
        r7 = open("r7.txt", "r")
        LIST.append(('32775', r7))
         
     
    if each_element == "r8.txt" :
        r8 = open("r8.txt", "r")
        LIST.append(('32776', r8))
         


    if each_element == "r9.txt" :
        r9 = open("r9.txt", "r")
        LIST.append(('32777', r9))
         
     
    if each_element == "r10.txt" :
        r10 = open("r10.txt", "r")
        LIST.append(('32778', r10))
         


    if each_element == "sw1.txt" :
        sw1 = open("sw1.txt", "r")
        LIST.append(('32779', sw1))
         
     
    if each_element == "sw2.txt" :
        sw2 = open("sw2.txt", "r")
        LIST.append(('32780', sw2))



    if each_element == "sw3.txt" :
        sw3 = open("sw3.txt", "r")
        LIST.append(('32781', sw3))
         

    if each_element == "sw4.txt" :
        sw4 = open("sw4.txt", "r")
        LIST.append(('32782', sw4))
         



def create_threads():
    threads = []
    for TELNET_PORT,router_file in LIST:
        th = threading.Thread(target = open_telnet_conn, args = (IP, TELNET_PORT, router_file, ))   
        th.start()
        threads.append(th)
        
    for th in threads:
        th.join()

create_threads()

time.sleep(25)
print ("""
(!!!) OK, NOW YOU CAN START WORK with Loaded LAB""")






