one = 'one'
print(one == 'one')

one = 'two'
print(one == 'one')

one = 'One'
print(one == 'one')
print(one.lower() == 'one')

number = 19
print("\nIs 19 == 19?")
print(number == 19)

print("\nIs 19 == 20?")
print(number == 20)

print("\n Is 19 < 20?")
print(number < 20)

print("\n Is 19 < 18?")
print(number < 18)

print("\n Is 19 <= 19?")
print(number <= 19)

print("\n Is 19 <= 18?")
print(number <=18)

print("\n Is 19 > 17?")
print(number > 17)

print("\n Is 19 > 20?")
print(number > 20)

print("\n Is 19 >= 17?")
print(number >= 17)

print("\n Is 19 >= 20?")
print(number >= 20)


#Keyword "and"
age_0 = 30
age_1 = 42
print(age_0 and age_1 >= 38)
print(age_0 and age_1 >= 28)

#Keyword "or"
if age_0 or age_1 >= 38:
    print(True)
if age_0 or age_1 <= 30:
    print(True)

#Check whether a value is in a list
towns = ['Medan','Bali','Jambi']
print('Medan' in towns)
print('Jakarta' in towns)

#Check whether a value is not in a list
towns = ['Medan','Bali','Jambi']
town = 'Jakarta'

if town not in towns:
    print(town.title() + ' is not in the list.')
