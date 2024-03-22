import os
import sys
import time
# Nama file flag untuk menandai apakah skrip telah dijalankan sebelumnya

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

clear_screen()      

from art import *
from colorama import Fore, Style

def blue_text_art(text):
    ascii_art = text2art(text)
    return f"{Fore.BLUE}{ascii_art}{Style.RESET_ALL}"  
banner = ""
teks = "DARKVORTEX"
teks_dengan_warna = blue_text_art(teks)
print(teks_dengan_warna)

 print("""\033[92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[91m[\033[92m::\033[91m] \033[93mTool Created by mr-patrix    
\033[91m[\033[92m::\033[91m] \033[93mVersion : 1.0.0
\033[92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
\033[91m [\033[92m1\033[91m] \033[93mDEFACE WEB
\033[91m [\033[92m2]\033[91m \033[93mcreate html files

 """)
pil = input(" [-] choose : ")
if pil ==('1'):
  os.system("python bot.py ")
if pil ==('2'):
i = str(input("  \033[91m[-] \033[93mhtml name : "))                       
p = str(input("""

  \033[91m[-]\033[93m your html script : """))

dos = ("%s.html"%(i))

nama_file = (""+ dos)

konten_html = (f''+ p)

with open(nama_file, "w") as file:
    file.write(konten_html)

print(f"html file with name '{nama_file}' it has been successfully created!")
os.system("python dv.py ")