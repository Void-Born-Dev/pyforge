def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# * and ** is basically allowing function to accept an arbitrary no to positional or keyword arguments

# for example this function student takes position arguments that represent that the classes that the student_info is taking the keyword argument passed in + the keywords passed in will ne random info about the student 

courses = ['Math' , 'Art']
info = { 'name': 'John' , 'age': 27}

student_info(courses, info)
#o/p (['Math', 'Art'], {'name': 'John', 'age': 27})
#{}

# here we sent our arguments in packed format 

student_info(*courses, **info)
# o/p 
# ('Math', 'Art')
# {'name': 'John', 'age': 27}