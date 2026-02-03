numbers = [10, 20, 30, 40, 50]#List
coordinates = (4, 5)#Tuples
print(numbers)
print(coordinates)

#Indexing and Slicing
a = [100,200,300,400,500,600,700,800,900]
print(a[-3:-1])     
print(a[1:5:2])
print(a[-7:-1:2])

#List Methods
fruits = ['apple', 'banana', 'cherry','mango','grape','apple']
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append('orange')
print(fruits)   
fruits.remove('banana')
print(fruits)
fruits.insert(1, 'kiwi')    
print(fruits)
fruits.pop()
print(fruits)
count = fruits.count('apple')
print(count)
fruits.remove('cherry')
print(fruits)