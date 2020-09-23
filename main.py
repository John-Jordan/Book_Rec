import random

print('This is a book recommendation application')
print('Genres available: history, autobiography, science fiction, non-fiction, children')
selection = input('Please select one of the listed genres to recieve a recommendation: ')

history = ['history book 1', 'history book 2', 'history book 3']
autobiography = ['auto book 1', 'auto book 2', 'auto book 3']
science_fiction = ['sci fi book 1', 'sci fi book 2', 'sci fi book 3']
non_fiction = ['non fiction book 1', 'non fiction book 2', 'non fiction book 3']
children = ['children book 1', 'children book 2', 'children book 3']

if selection == 'history':
  print(random.choice(history))
elif selection == 'autobiography':
  print(random.choice(autobiography))
elif selection == 'science fiction':
  print(random.choice(science_fiction))
elif selection == 'non fiction':
  print(random.choice(non_fiction))
elif selection == 'children':
  print(random.choice(children))
else:
  print('Please select a genre from the list.')