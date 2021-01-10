import subprocess
import re
import platform

def addr():
    print('[+] Select Network: ')
    subprocess.call("ifconfig | expand | cut -c1-8 | sort | uniq -u | awk -F: '{print $1;}'",shell=True)
    network=str(input('>>> '))
    return network

address=str(input('[+] Custom Mac Address: '))
x = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", address)
if x: 
    if platform.system()=='Darwin':
        network = addr()
        print('[+] Changing MAC Address...')
        try:
            subprocess.call('sudo ifconfig '+network+' ether '+x.group(),shell=True)
        except :
            print("[-] Please Try Again")
    elif platform.system()=='Linux':
        network = addr()
        print('[+] Changing MAC Address...')
        try:
            subprocess.call('ifconfig '+network+' down',shell=True)
            subprocess.call('ifconfig '+network+' hw ether '+x.group(),shell=True)
            subprocess.call('ifconfig '+network+' up',shell=True)
        except :
            print("[-] Please Try Again")
    elif platform.system()=='Windows':
        user=str(input('>>Enter Username:'))
        pwd=str(input('>>Enter Password:'))
        print('[+] Changing MAC Address...')
        try:
            subprocess.call("reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\ControlClass\{4D36E972-E325-11CE-BFC1-08002BE10318}_0002 /v NetworkAddress /d "+x.group().replace(':','')+" /f",shell=True)
        except :
            print("[-] Please Try Again")
    else:
        print("[-] MAC Address can't be changed for this system")
else: print('[-] Enter valid MAC Address or type --help for assistance')

