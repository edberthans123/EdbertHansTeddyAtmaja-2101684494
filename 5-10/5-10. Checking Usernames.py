current_users = ['police','doctor','maid','pirate','boss']
new_users = ['police','doctor','fireman','artist','scientist']
for new in new_users:
    if new in current_users:
        print('username ' + new + ' has been taken :)')
    else:
        print('This ' + new +' username is available :)')
