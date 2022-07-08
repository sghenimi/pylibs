import random, statistics as sc
"""
Création de Array
"""
#array1 = random.sample(range(1, 20), 6)
#array2 = random.sample(range(1, 20), 7)
array1 = [13, 2, 14, 5, 15, 19]
array2 = [16, 13, 19, 3, 9, 7, 4]

"""
Affichage des Arrays
"""
print("Liste1 : ", array1)
print("Liste2 : ", array2)

"""
Trie des Arrays
"""
array1.sort()
array2.sort()
print(array1)
print(array2)

sum1 = sum(array1)
sum2 = sum(array2)
print(sum1, sum2)

avg1 = 
avg2 = sc.mean(array2)
print(avg1, avg2)


