# Сортировка методом поиска
import lib.random_array as random_array

myArray = random_array.create(0,100,10)

print(myArray)

n = len(myArray)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if myArray[j] < myArray[min_index]:
            min_index = j
    myArray[i], myArray[min_index] = myArray[min_index], myArray[i]


print(myArray)

