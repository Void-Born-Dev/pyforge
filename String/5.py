message = "Hello World"

print(message[:5])#o/p: Hello
print(message[6:11])#o/p: World
print(message[0:11])#o/p: Hello World
print(message[0:11:2])#o/p: HloWrd
#here 2 is the step value. It means that we are taking every 2nd character from the string. The default step value is 1. If we don't provide any step value, it will take every character from the string.
#doubt print(message[10:2])
print(message[::1])#o/p: Hello World
