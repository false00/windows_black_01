import re
import subprocess
import os


def main():
    os.chdir('c:\\')
    generate_update_list()
    textfile = open('hotfix.txt')
    data = textfile.read()
    list = map(str, re.findall(r'\bKB.{7}\b',data))
    for hotfixes in list:
        print (hotfixes)
        uninstall_updates(hotfixes.strip('KB'))
    success()

def success():
    a = 'Uninstalled patches Sucessfully'
    print (a)

def generate_update_list():
    try:
        subprocess.check_call('wmic qfe list brief /format:texttablewsys > c:\\hotfix.txt', shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

def uninstall_updates(kb):
    try:
        subprocess.check_call('%windir%\SysNative\wusa.exe /uninstall /kb:{} /quiet /norestart'.format(kb), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

if __name__ == "__main__": main()
