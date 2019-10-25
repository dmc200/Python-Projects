greeting = "Hello"
name = 'Michael'

# Use replace() function
# my_message = my_message.replace('World', 'Universe')

# Concat Strings
# message = greeting + ', ' + name + '.  Welcome!'

# message = '{}, {}. Welcome!'.format(greeting, name)

# f-string's
message = f'{greeting}, {name.upper()}. Welcome!'

# get methods applied to that var. dir()
# get everything! from help()
print(dir(name))
print(help(str))
print(help(str.replace))
print(message)
