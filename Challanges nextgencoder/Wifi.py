from subprocess import check_output


def cmd(lst):
    return check_output(lst).decode('utf-8').split('\n')


data = cmd(['netsh', 'wlan', 'show', 'profiles'])
wifis = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]

for wifi in wifis:
    data = cmd(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear'])
    password = [line.split(':')[1][1:-1] for line in data if 'Key Content' in line]
    password = password[0] if len(password) else 'None'
    print(f'Name : {wifi}, Password : {password}')
