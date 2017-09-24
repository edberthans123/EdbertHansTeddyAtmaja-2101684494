#no username
username = []
for i in username:
    if i == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print("Hello " + i + ',thanks for logging in')
else:
    print('We need to find some users!')
