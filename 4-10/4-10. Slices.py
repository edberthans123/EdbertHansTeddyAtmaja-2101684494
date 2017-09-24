Pizzas =['Meat lover','Tuna','Pepperoni']
a = Pizzas[0]
b = Pizzas[1]
c = Pizzas[2]
for i in Pizzas:
    print(i + ' is really tasty.')

print('You cannot buy happiness, but you can buy Pizzas')

print('The first three items in the list are:')
for i in Pizzas[:3]:
    print(i)

print('Three items from the middle of the list are:')
Pizzas.append('Presto')
Pizzas.append('Cheese')
for i in Pizzas[1:4]:
    print(i)

print('The last three items in the list are:')
for i in Pizzas[2:5]:
    print(i)
