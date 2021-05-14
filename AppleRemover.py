from mutagen.easyid3 import EasyID3
import os
import subprocess
from colorama import Fore

def appleRemover(fileName):
    audio = EasyID3(fileName)
    title = audio['title']
    artist = audio['artist']
    joinName =  f"{title[0]} - {artist[0]}.mp3"
    os.rename(r''+fileName, r''+joinName)
    print(f"File: {fileName}{Fore.GREEN} OK{Fore.RESET}")
    print(f"{fileName} changed to {joinName}")


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

