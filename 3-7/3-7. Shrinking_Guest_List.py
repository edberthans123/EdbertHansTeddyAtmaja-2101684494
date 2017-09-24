friends = ['Dean','Edgar','Ryan']
print('hey come over and have a dinner with me,' + friends[0])
print('come over and lets eat,' + friends[1])
print('wanna have some dinner together,' + friends[2])

print('Edgar cannot come tonight')
friends[1] = 'Ulip'
print('hey come over and have a dinner with me,' + friends[0])
print('come over and lets eat,' + friends[1])
print('wanna have some dinner together,' + friends[2])

#think of three more guests to invite to dinner
print('I have found a bigger dinner table and i am going to invite some more people')
friends.insert(0,'Popeye')
friends.insert(2,'Manila')
friends.append('Lolola')
print('hey come over and have a dinner with me,' + friends[0])
print('come over and lets eat,' + friends[1])
print('wanna have some dinner together,' + friends[2])
print('hey come over and have a dinner with me,' + friends[3])
print('come over and lets eat,' + friends[4])
print('wanna have some dinner together,' + friends[5])

#found out that my new dinner table won't arrive in time for the dinner, so i only have space for two guests
print('I just found out that my dinner table will not arrive in time and i only have space for two more guests')
pupu = friends.pop()
pipi = friends.pop()
popo = friends.pop()
prpe = friends.pop()
print('sorry i got no space left for you ' + pupu + '.')
print('I have to cancel your invitation ' + pipi + '.')
print('I have no more space,next time ok? ' + popo + '.')
print('lets go out next time ok? ' + prpe + '.')
print('You can still come... I am saving a space for you ' + friends[0])
print('you are still invited so dont be late ok? ' + friends[1])

del friends[0]
del friends[0]
print(friends)
