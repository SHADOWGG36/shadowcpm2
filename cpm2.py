import colorama
import sys
import os
import threading, requests, ctypes, random, json, time, base64, sys, re
import random
from colorama import Fore, Back, Style
from colorama import Fore, Style
from time import strftime
from colorama import init, Fore
from pystyle import Write,Colors
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
nmh = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'

from pystyle import Colors, Write, Colorate, Center

# Tạo văn bản ASCII art
banner_text = """
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░
"""

# Tạo dải màu chuyển từ tím sang cyan
colored_art = Colorate.Vertical(Colors.purple_to_blue, banner_text)

# In ra văn bản với dải màu
print(Center.XCenter(colored_art))

text = """
\033[1;31m════════════════════\033[1;31m[ \033[1;32mThông Tin \033[1;31m] \033[1;31m═════════════════
\033[1;32mTool:\033[1;33m Car Parking Multiplayer 2 
\033[1;32mFacebook:\033[1;33m Sha Dow
\033[1;32mZalo:\033[1;33m 0869326484
\033[1;32mTikTok:\033[1;33m shadowgg_2k16
\033[1;31m════════════════════\033[1;31m[ \033[1;32mTài Khoản \033[1;31m] \033[1;31m═════════════════
\033[1;34mTên:\033[1;35m SHADOW
\033[1;34mID:\033[1;35m ND81748
\033[1;34mTiền:\033[1;35m 50000000
\033[1;34mCoin:\033[1;35m 0
\033[1;31m╔════════\033[1;31m[ \033[1;32mMENU HACK \033[1;31m]══════\033[1;31m╗
\033[1;31m║\033[1;33m[01]     \033[1;37mBuff Tên Dài      \033[1;31m║
\033[1;31m║\033[1;33m[02]     \033[1;37mChỉnh Sửa ID      \033[1;31m║
\033[1;31m║\033[1;33m[03]     \033[1;37mbuff Tiền         \033[1;31m║
\033[1;31m║\033[1;33m[04]     \033[1;37mRank King         \033[1;31m║
\033[1;31m║\033[1;33m[05]     \033[1;37mMở Tất Cả Slot Xe \033[1;31m║
\033[1;31m║\033[1;33m[06]     \033[1;37mThoát Acc         \033[1;31m║
\033[1;31m║\033[1;33m[07]     \033[1;37mThoát Tool        \033[1;31m║
\033[1;31m╚═══════════════════════════\033[1;37m\033[1;31m╝
"""

print(text)
chon = input("nhập số: ")
if chon == '08':
    print('THOÁT THÀNH CÔNG')
    exit()
else:
    print('CHỨC NĂNG CHƯA HỖ TRỢ')
    exit()