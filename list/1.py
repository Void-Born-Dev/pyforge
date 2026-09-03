courses = ["Python", "Java", "C++", "JavaScript"]
print(type(courses))#o/p: <class 'list'>

#list is collection which is ordered and changeable. Allows duplicate members.

print(len(courses))#o/p: 4 
# when we use len() function with list it will return the number of items in the list.

print(courses[0])#o/p: Python 
# individual items in a list can be accessed by referring to its index number, inside square brackets. indexing starts from 0, so the first item has index 0, the second item has index 1 etc.

print(courses[-1])#o/p: JavaScript
# negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.

print(courses[1:3])#o/p: ['Java', 'C++']
# slicing can be used to access a range of items in a list. The syntax is list[start:end] where start is the index of the first item and end is the index of the last item (exclusive).

print(courses[:3])
#o/p: ['Python', 'Java', 'C++']
#when no start index is specifies, the slice will start from the first item.

print(courses[1:])
#o/p: ['Java', 'C++', 'JavaScript']
#when no end index is specifies, the slice will end at the last item.