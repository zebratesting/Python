"""

d1={'name': 'John', 1: [2, 4, 3]}

print(d1.fromkeys('name'))

print(d1.items())

"""

list_countries=["India","Canada","USA"]

list_countries.append("Europe")

print("list after adding:",list_countries)

list_countries.remove("India")

print("list after removing by a value:",list_countries)

list_countries.insert(2,"UAE")
print("list after inserting a new one:",list_countries)

#Sets

set=set(list_countries)

print(set)
print(type(set))

set.update('China')

print("Set after adding a country",set)

set.remove('China')
print("Set after remving a country",set)

set.add("marshall")
print("Set after update",set)
