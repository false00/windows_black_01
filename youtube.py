import subprocess

#f = open('users.txt', 'r')
#for line in f.readlines():
    #line = line+line
#    print(line)
#    print(line)
    #subprocess.check_call('net user ' + '{}'.format(line) +' ' + '/add Temp1234')
with open("users.txt") as f:
    for line in f:
        try:
            subprocess.check_call('net.exe user /add {} Temp1234'.format(line), shell=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
