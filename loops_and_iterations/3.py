# A nested loop is a loop placed inside another loop, where the inner loop runs completely for every single outer iteration.

# nested loops result in running a loop inside a loop resulting in all combinations of the items

nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc':
        print(num , letter)

        