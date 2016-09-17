import re
import subprocess


def main():
    generate_update_list()
    with open("c:\\patches.txt") as f:
        data = f.read()
        print('Preparing to delete...')
        list_kb = map(str, re.findall(r'Package_for_KB.{39,40}', data))
        for packages in list_kb:
            #print (packages.strip())
            uninstall_updates(packages.strip(''))
            print('Uninstalled: ' + packages)
        success()


def success():
    a = 'All Patches Removed...'
    print (a)


def generate_update_list():

    try:
        subprocess.check_call('dism.exe /online /get-packages /format:table > c:\patches.txt', shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


def uninstall_updates(a):
    try:
        subprocess.check_call('dism.exe /online /remove-package /packagename:{} /quiet /norestart'.format(a), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

if __name__ == "__main__": main()

#dism /online /get-packages /format:table > patches.txt
#Package_for_KB2870699~31bf3856ad364e35~amd64~~6.2.1.1
#DISM.exe /Online /Remove-Package /PackageName:Package_for_KB2870699~31bf3856ad364e35~amd64~~6.2.1.1 /quiet /norestart