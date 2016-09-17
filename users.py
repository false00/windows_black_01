import subprocess

def main():
    with open("c:\\users.txt") as f:
        for line in f:
            create_win_users(line)

def create_win_users(line):
    try:
        subprocess.check_call('net.exe user /add {}'.format(line), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

if __name__ == "__main__": main()
