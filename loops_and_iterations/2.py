# In Python, break and continue are loop control statements used to alter the normal flow of a loop. They let you stop a loop early or skip parts of it based on specific conditions.


# break: Instantly exits and terminates the loop entirely, even if the condition is still true or the sequence isn't finished.

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('found!')
        break
    print(num)

#o/p :     
#1
#2
#found! 
# the loop will be stopped one the condition is met when using break 




#continue: Skips the rest of the code in the current iteration and jumps straight to the next cycle of the loop.

for num in nums:
    if num == 3:
        print('found!')
        continue
    print(num)

#o/p :
# 1
# 2
# found!
# 4
# 5    

# the loop will not break but if will skip the remaining code bloak in the third iteration 
