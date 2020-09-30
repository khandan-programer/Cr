import time

import sys

import os

import webbrowser

import warnings

from colorama import init , AnsiToWin32 , Fore , Back

init(wrap=False)

stream = AnsiToWin32(sys.stderr).stream
print ("")
def logo():
    print (Fore.GREEN, '''
    
                    _|_|_|_|_|_|_|               
                   |                                       
                  _|                         |                       
                   |                         |   //                  
                  _|                         |  //
                   |                         |//
                  _|                         |
                    _|_|_|_|_|_|_|           |
                    ''', file=stream)


def Target():
    URL = input("Enter your target =>>")

    instagram = webbrowser.open("instagram.com/" + URL)

    if instagram == "Page Not Found . Instagram":
        print (Fore.RED, "Instagram page Not Found")
    
    time.sleep(3)

    telegram = webbrowser.open("t.me/" + URL)

    time.sleep(3)

    facebook = webbrowser.open("facebook.com/" + URL)

    time.sleep(3)

    aparat = webbrowser.open("aparat.com/" + URL)

    time.sleep(3)

    youtube = webbrowser.open("youtube.com/" + URL)

    time.sleep(3)

    google = webbrowser.open(URL)
    print ("")
    print (Fore.GREEN, "Founding page .....", file=stream)

print ("")

logo()

Target()

print ("")
