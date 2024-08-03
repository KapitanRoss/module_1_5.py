immutable_var = 1, 2, 3, 'apple', 'banana', 'coffee', True
print(immutable_var)
mutable_list = [11, 12, 13, 'white', 'black', 'gray', False]
mutable_list[0:3] = [111, 112, 113]
print(mutable_list)
mutable_list[3:5] = ['a', 'b', 'c']
print(mutable_list)
