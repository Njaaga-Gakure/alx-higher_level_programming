#!/usr/bin/python3

a = "School"
b = 9
c = 9.7
d = [1, "c", {"key": "value"}, 6]
e = {"name": "brian", "age": 26}
class User:
	pass
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(User))
print(type(e))

if type(a) == str:
	print(a)
else:
	print(b)
print(id(a))
