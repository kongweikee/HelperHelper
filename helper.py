import os
import pyperclip
from configparser import ConfigParser
import requests as rq
from time import sleep

jav = ""
m3u8url = ""
nowPasted = ""
lastPasted = ""
downloaded = []
command = ""
tool_GitHubReleaseUrl = "https://github.com/nilaoda/N_m3u8DL-CLI/releases/latest"


def init():
    config = ConfigParser()
    if not os.path.exists("init.config"):
        print("Can Not Find Configuration File, Would You Like To Start the Guidance?")
        print("1.Yes\t2.Why Not?\t3.Sure")
        input(">>>")
        config.add_section("setting")
        config.set("setting", "toolPath", input("Please Enter Your Tools Path: "))
        config.set("setting", "downloadPath", input("Please Enter Your Download Path: "))
        print("Please Enter Your Proxy Address: ")
        print("e.g.: http://127.0.0.1:1080 or socks5://127.0.0.1:1080)")
        print("If Your Do Not Want To Use Proxy You Just Need To Press Enter")
        proxy = input(">>>")
        if proxy != None:
            config.set('setting', 'proxies', proxy)
        else:
            config.set('setting', 'proxies', "")
        config.write(open("init.config", "w+"))

    config.read("init.config", encoding="UTF-8")
    toolPath = config['setting']['toolPath']
    downloadPath = config['setting']['downloadPath']
    proxy = config['setting']['proxies']

    conf = {
        'toolPath': toolPath,
        'downloadPath': downloadPath,
        'proxies': {
            'http': proxy,
            'https': proxy,
        }
    }
    return conf


def CheckVersion():
    try:
        version = rq.get(tool_GitHubReleaseUrl, proxies=conf['proxies']).url.split("/")[-1]
        return version
    except:
        return "2.9.7"


def FindAndDownloadTool():
    conf['version'] = CheckVersion()
    if not os.path.exists(conf['toolPath'] + "/" + "ffmpeg.exe"):
        try:
            print("\nTrying To Download ffmpeg")
            open(conf['toolPath'] + "/ffmpeg.exe", 'wb').write(
                rq.get("https://github.com/nilaoda/N_m3u8DL-CLI/releases/download/2.2.0/ffmpeg.exe",
                       proxies=conf['proxies']).content)
            print("\nDownload Finished!\n")
        finally:
            None
    if not os.path.exists(conf['toolPath'] + "/" + f"N_m3u8DL-CLI_v{conf['version']}.exe"):
        try:
            print("\nTrying To Download N_m3u8DL")
            downloadUrl = f"https://github.com/nilaoda/N_m3u8DL-CLI/releases/download/{conf['version']}/N_m3u8DL-CLI_v{conf['version']}.exe"
            open(conf['toolPath'] + f"/N_m3u8DL-CLI_v{conf['version']}.exe", 'wb').write(
                rq.get(downloadUrl, proxies=conf['proxies']).content)
            print("\nDownload Finished!\n")
        finally:
            None


def ListeningPaste():
    global nowPasted
    global lastPasted
    global m3u8url
    global jav
    nowPasted = pyperclip.paste()
    if lastPasted == "" or lastPasted != nowPasted:
        lastPasted = nowPasted
    if lastPasted.split("#")[0].split(".")[-1] == "m3u8":
        try:
            m3u8url = lastPasted.split("#")[0]
            jav = lastPasted.split("#")[1]
        except:
            return False
        else:
            return True
    else:
        return False


def Download(url, digital):
    if digital not in downloaded:
        print(f"\nFounded: {digital}\nNow Start Download...\n")
        downloaded.append(jav)
        command = conf['toolPath'] + fr"\N_m3u8DL-CLI_v{conf['version']}.exe" + " " + fr'"{url}" --workDir "{conf["downloadPath"]}" --saveName "{digital}" --enableDelAfterDone'
        print(command + "\n")
        os.system(command)


if __name__ == '__main__':
    conf = init()
    FindAndDownloadTool()
    print("\nLaunched Successfully!\nNow Listening the Clipboard......\n")
    while True:
        if ListeningPaste():
            Download(m3u8url, jav)
        sleep(1)

