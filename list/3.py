courses = ['History' , 'Math' , 'Physics' , 'CompSci']
print(courses)#o/p : ['History', 'Math', 'Physics', 'CompSci']

courses.insert(0,'Art')
#.insert() method is used to add an item at the specified index. The first argument is the index where the item should be inserted, and the second argument is the item to be insered
print(courses)#o/p : ['Art', 'History', 'Math', 'Physics', 'CompSci']

courses_2 = ['Art' , 'Education']
courses.insert(0,courses_2)
#here we are inserting a list inside another list. The entire list will be add as a single item at the spcified index.
print(courses)#o/p : [['Art', 'Education'], 'Art', 'History', 'Math', 'Physics', 'CompSci']

courses.extend(courses_2)
#here extend() method is used to add the elements of another list to the end of the current list. It takes an iterable (like a list) as an argument and adds each element of that iterable to the end of the list.
print(courses)# o/p: ['Art', 'Education', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']