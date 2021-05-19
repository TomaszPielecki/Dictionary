Person = {
    'firstName': 'Tomasz',
    'secondName': 'Pielecki',
    'age': 34,
    'country': 'poland',
    'town': 'Kartuzy',
    'Job': 'Car driver',
    'status': 'student'
}
Person2 = {
    'firstName': 'Janusz',
    'secondName': 'Wierzbicki',
    'age': 54,
    'country': 'poland',
    'town': 'Malbork',
    'Job': 'Bus diriver',
    'status': 'worker'
}
print(Person)
print(Person2)
print(Person['firstName'], ':', Person['town'])
print(Person2['firstName'], ':', Person2['town'])
# dodanie pola do person2
Person2['car'] = 'Vw polo'

print(Person2['firstName'], ':', Person2['town'], ':', Person2['car'])
