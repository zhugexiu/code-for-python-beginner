from math import *

my_num = 5
print(str(my_num))
print(my_num)
print(pow(3, 2))

print(sqrt(36))

friends = ["Allen", "Bob", "Cindy"]
print(friends)
print(friends[2])
print(friends[-2])
print(friends[1:])
lucky_numbers = [3, 4, 5, 6]
friends.extend(lucky_numbers)
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Bob")
print(friends)
friends.pop()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)