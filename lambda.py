
#SORTED
points2D = [(1,12), (15,1), (5, -1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0]+x[1])
# print(points2D)
# print(points2D_sorted)


#MAP
a=[1,2,3,4]
b= map(lambda x: x*2, a)
# print(list(b))

c = [x*2 for x in a]

print(c)

#FILTER
even = filter(lambda x: x%2==0, a)
# print(list(even))

even_comprehension = [x for x in a if x%2==0]

# print(even_comprehension)

#REDUCE
from functools import reduce
prod_a = reduce(lambda x,y: x*y, a)

print(prod_a)


wyraz = 'abcdefg'
dashed = reduce(lambda x,y: x+"-"+y, wyraz)

print(dashed)

