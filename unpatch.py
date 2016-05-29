import re
import subprocess


def main():
    generate_update_list()
    convert_encoding()
    with open("c:\\hostfix-utf8.txt") as f:
        data = f.read()
        print('Preparing to delete')
        list_kb = map(str, re.findall(r'\bKB.{7}\b', data))
        for hotfixes in list_kb:
            #print (hotfixes.strip('KB'))
            uninstall_updates(hotfixes.strip('KB'))
            print('Uninstalled: ' + hotfixes)
        success()


def convert_encoding():
    sourceEncoding = 'utf-16-le'
    targetEncoding = 'utf-8'
    source = open('c:\\hotfix.txt')
    target = open('c:\\hostfix-utf8.txt', "w")

    target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))


def success():
    a = 'All Patches Removed...'
    print (a)


def generate_update_list():

    try:
        subprocess.check_call('wmic qfe list brief /format:texttablewsys > c:\hotfix.txt', shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


def uninstall_updates(a):
    try:
        subprocess.call('%windir%\System32\wusa.exe /uninstall /kb:{} /norestart /quiet'.format(a), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

if __name__ == "__main__": main()
