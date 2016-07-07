##Solution to log puzzle-part A.Problem posted at "https://developers.google.com/edu/python/exercises/log-puzzle" 
import urllib
import re
import os
import webbrowser
import sys
path=raw_input("Enter the directory where you want to save?")
text=open("animal_code.google.com").read()

#method1
#m=re.findall(r"GET\s([\w\/\.\-]+\.jpg)",text)

##method 2
#m=re.findall(r"GET\s([\S]+\.jpg)",text)

###method 3
m=re.findall(r"GET\s(.+\.jpg)",text)

usefullink=sorted(set(m),)   #to ignore the repeatitions

rpath=os.path.abspath(path)
if not os.path.exists(rpath):
    os.mkdir(rpath)

#creating output file
ofile=open(os.path.join(path,"index.html"),'w')

ofile.write("<html><body>\n")


#for link in usefullink:
 #   print link
for i in range(0,len(usefullink)):
    down_link="https://"+"code.google.com"+usefullink[i]
    print "Retrieving...",down_link
    urllib.urlretrieve(down_link,os.path.join(path,"img"+str(i)))
    ofile.write("<img src=%s>" % down_link)
ofile.write("\n</body></html>\n")
ofile.close()


print "All images downloaded in " , os.path.abspath(path)
print ".\n.\n.\n"
print "Images joined"

choice=raw_input("Do you want to open joined image using default browser(Y or N) ")
if(choice[0]=='y' or 'Y'):
    path2file=os.path.join(path,"index.html")
    print path2file
    webbrowser.open(path2file)
else:
    sys.exit()


