#!/usr/bin/env python
import os
import sys
from time import sleep
import socket
#///////////bANNER
"""

          __        _______ _     ____ ___  __  __ _____ 
          \ \      / / ____| |   / ___/ _ \|  \/  | ____|
           \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
            \ V  V / | |___| |__| |__| |_| | |  | | |___  _   _   _ 
             \_/\_/  |_____|_____\____\___/|_|  |_|_____|(_| |_| |_)
                                               

                        Script Crearor: 
     _   _    _____ _    ____    _____  ___     ___    _   _    _    
    | | / \  |  ___/ \  |  _ \  |_   _|/ \ \   / / \  | \ | |  / \   
 _  | |/ _ \ | |_ / _ \ | |_) |   | | / _ \ \ / / _ \ |  \| | / _ \  
| |_| / ___ \|  _/ ___ \|  _ <    | |/ ___ \ V / ___ \| |\  |/ ___ \ 
 \___/_/   \_\_|/_/   \_\_| \_\   |_/_/   \_\_/_/   \_\_| \_/_/   \_\
                                                                     
Tell: +989170118221   		  Mail: PowerInfoSSL@Gmail.com





"""
##
bn='Easy Use FireWall Version 0.01'
print bn
#//////////////////////////
#/////////////////////////
#////////////////////////
#///////////////////////
#//////////////////////
#/////////////////////
#////////////////////
#///////////////////
#//////////////////
#/////////////////
#////////////////
#///////////////
#//////////////
#/////////////
#////////////
#///////////
#//////////
#/////////
#////////
#///////
#//////
#/////
#////
#///
#//
#/
#*********************************************Check File's Desaniation
def fck(name,data=''):
    if os.path.exists(name)==False:
        o=open(name,'w')
        print 'File %s Rebuilding...' % name
        if data!='':
            o.write(data)
        o.close()

#*********************************************'Show IPTables Data
def sh_ipt(ch='INPUT'):
    dd=[]
    de=''
    if ch=='INPUT':
        nuu=0
        sst=os.popen('iptables -L INPUT')
        d=sst.readlines()
        for i in d:
            de +=i
        return de
    if ch=='OUTPUT':
        nuu=0
        sst=os.popen('iptables -L OUTPUT')
        d=sst.readlines()
        for i in d:
            de +=i
        return de
#***********************************************Key Defain 
def key_p(str_d=''):
    #if str_d!='':
    raw_input('Press any key to continue...')
    #else:
	#	raw_input(str_d)
#**********************************************Really Check File
fck('blk-ip')
#''''''''''''''Read IP File
def op(addr):
    fl=[]
    ipl=[]
    f1=open(addr,'r+')
    s=f1.readlines()
    ipl2=[]
    #*********************************************Menu Item
    #/////////////Remove Empty Line's
    for i in range(0,len(s)):
        if len(s[i])>=4:
            ipl2.append(s[i].rstrip())
            #print 'added ',s[i]
    #**********************************************Close File Opened & Return Valu's
    f1.close()
    return ipl2
#**************************************************Write Data to the File's
def wr_f(d1,d2):
    #**********************************************Check Value Alredy Exist or not
    print 'Checking Uniq Data....'
    ww=op(d1)
    if d2 in ww:
        #print '______________________________\n\n            ERROR\n      This Host Alredy Exist .\n______________________________\n'
        #raw_input('Press any Key to Continue...')
        dn=1
        return
    f=open(d1,'aw')
    f.write(d2+'\n')
    f.close()
    print 'File Upgraded'
    print '*****your Data: '+d2
#*****************Save Data to The IPTables
def file_op(stt):
    print "\n\n***********************************************\n\n"
    ws=op(stt)
    for i in ws:
        print "[+]  "+i



#*****************Defain Execute Script
def exe(a='-A',ch=' INPUT',d=' -s'):
    if ch=='INPUT':
        os.system('iptables '+a+ch+d+i+' -j LOG --log-prefix \"Blocked Input IP Address '+i+' .\"')
        os.system('iptables '+a+ch+d+i+' -j DROP')
    if ch=='OUTPUT':
        os.system('iptables '+a+ch+d+i+' -j LOG --log-prefix \"Blocked Output IP Address '+i+' .\"')
        os.system('iptables '+a+ch+d+i+' -j DROP')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\SHOW MENU////////////////////////////
#*********************************************Router OS Migration Menu
fck('blk-ip','q')
ss=1
while 1:
    #ee +=1
    #print 'port number is %s' % ee
    try:
        o=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        o.bind(('localhost',80))
        o.listen(10)
        print 'Streeming(Presess CTR+C to Stop Black list Auto Builder) ...'
        h,(a,aa)=o.accept()
        h.close()
        print a
        wr_f('blk-ip',a)
        wr_f('black-ip',a)
        ss=1
    except:
        if ss==1:
            print '\n Try to Enabling...\n Presess CTR+C to Stop Black list Auto Builder'
            sleep(5)
            ss=0
