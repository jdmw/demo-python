fruits = ['apple','banana','pear','kiwi']
squares = [1,4,9,16]
print(squares[-1])
print(squares[:]) # [1, 4, 9, 16, 25]: a shadow copy
print(squares + [36, 49, 64, 81, 100]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value
print(cubes) # [1, 8, 27, 64, 125]
cubes.append(216)  # add the cube of 6

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
len(letters)
letters # ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
