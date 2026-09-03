greeting = "Hello"
name = "Michael"

#different ways to concatenate strings in python


message = greeting + ", " + name
print(message)#o/p: Hello, Michael

message = "{}, {}".format(greeting, name)
print(message)#o/p: Hello, Michael

message = f"{greeting}, {name}"
print(message)#o/p:Hello, Michael

print(dir(name))#this will give you all the methods that can be used with the string data type.
#o/p: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle...',

print(help(str))#this will give you all the methods that can be used with the string data type along with their description.

