
story = '''_______! he said ________ as he jumped into his convertible
     ______ and drove off with his ___________ wife.'''
print(story)

values = {'noun':'','verb':'','adjective':''}


values['noun'] = input("\nEnter a noun (Person, Place or Thing): ")
values['verb'] = input("\nEnter a verb (action): ")
values['adjective'] = input("\nEnter a adjective (describes a noun): ")

print(values['noun'])
print(values['verb'])
print(values['adjective'])


filledStory = "{}! he said {} as he jumped into his convertible {} and drove off  \n with his {} wife.".format(values['noun'], values['verb'], values['noun'],values['adjective']) 


print(filledStory)


