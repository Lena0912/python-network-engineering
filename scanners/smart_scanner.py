import os

critical_hosts = ['8.8.8.8', '1.1.1.1']
test_hosts = ['10.255.255.1']

all_hosts = critical_hosts + test_hosts

for ip in all_hosts:
    print(f'--- Scanning {ip} ---')

    response = os.system(f'ping -c 1 {ip} > /dev/null')

    if response == 0:
        print(f'STATUS: {ip} is UP. Everything is fine.')
    else:
        if ip in critical_hosts:
            print(f'!!! ALERT: Critical host {ip} is DOWN! Call the Team Lead!')
        else:
            print(f'NOTICE: Test host {ip} is down. No action needed.')
