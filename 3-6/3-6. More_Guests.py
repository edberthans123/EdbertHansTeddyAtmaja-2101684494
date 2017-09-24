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
