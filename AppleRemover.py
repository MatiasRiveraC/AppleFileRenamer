from mutagen.easyid3 import EasyID3
import os
import time
import subprocess
from colorama import Fore

def appleRemover(fileName):
    ti_m = os.path.getmtime(fileName)
    m_ti = time.ctime(ti_m)
    t_obj = time.strptime(m_ti)
    audio = EasyID3(fileName)
    title = audio['title']
    artist = audio['artist']
    joinName =  f"{title[0]} - {artist[0]}.mp3"
    
    os.rename(r''+fileName, r''+joinName)
    print(f"File: {fileName}{Fore.GREEN} OK{Fore.RESET}")
    print(f"{fileName} changed to {joinName}")
    #changeFileDate(joinName, t_obj, fileName)
    
def changeFileDate(joinName, t_obj, ogFileName): # WORK IN PROGRESS
    months = {1:"January",2:"February",3:"March",4:"April",5:"May",
              6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",
              12:"December"}
    year = t_obj.tm_year
    month = t_obj.tm_mon
    day = t_obj.tm_mday
    hour = t_obj.tm_hour
    minute = t_obj.tm_min
    sec = t_obj.tm_sec
    currPath = os.getcwd()
    cmdCreation = f"(Get-Item '{currPath}\{joinName}').CreationTime=('{day} {months[month]} {year} {hour}:{minute}:{sec}'"
    cmdLastWrite = f"(Get-Item '{currPath}\{joinName}').LastWriteTime=('{day} {months[month]} {year} {hour}:{minute}:{sec}'"
    cmdAccessTime = f"(Get-Item '{currPath}\{joinName}').LastAccessTime=('{day} {months[month]} {year} {hour}:{minute}:{sec}'"
    
    #run(cmdCreation)
    #run(cmdLastWrite)
    #run(cmdAccessTime)

    
    
    
def run(cmd):
    completed = subprocess.run(["powershell.exe", cmd], capture_output=True)
    return completed


def main():
    arr = os.listdir()
    extensions = ['.mp3']
    for song in arr:
        for extension in extensions:
            if extension in song:
                try:
                    appleRemover(song)
                except:
                    print(f"File: {song}{Fore.RED} ERROR{Fore.RESET}")
            else:
                print(f"File: {song}{Fore.RED} ERROR{Fore.RESET}")


if __name__ == "__main__":
    main()

