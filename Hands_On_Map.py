#Making a map 
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = map(lambda x, y: x + y, numbers1, numbers2)
print(list(output))

#Using a map

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def sq(n):
    return n*n
output2 = list(map(sq, numbers))
print(output2)