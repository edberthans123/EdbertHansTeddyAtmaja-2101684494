cities =['Jakarta','Medan','Jambi']
print(cities)
print(cities[0])
print(cities[1].title())
print(cities[2].lower())
print(cities[1].upper())
print(cities[0].lstrip())
print(cities[2].rstrip())
print(cities[0].strip())
message = "I want to go to " + cities[2] + '.'
print(message)
cities[0] = 'Pontianak'
print(cities)
cities.append('Jakarta')
print(cities)
cities.insert(0, 'Bali')
print(cities)
del cities[0]
print(cities)
pop = cities.pop()
print(cities)
print(pop)
print('Wanna go to ' + pop + '?')
cities.remove('Pontianak')
print(cities)
a = 'Medan'
cities.remove(a)
print(cities)
print('Can we go to ' + a + ' next week?')
cities.append('Jakarta')
cities.append('Bali')
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
cities.reverse()
print(cities)
print(len(cities))
print(cities[-1])
