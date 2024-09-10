from itertools import product

a = ['w',2]
b= [3,4]
c= [True, False]

prod = product(a,b,c, repeat=2)

# print(list(prod))

from itertools import permutations
a=[1,2,5,3]

perm = permutations(a,2)

# print(list(perm))

from itertools import combinations

com = combinations(a,2)

# print(list(com))

from itertools import combinations_with_replacement

cwr = combinations_with_replacement(a,2)
# print(list(cwr))


from itertools import accumulate
import operator

acc = accumulate(a, func=operator.mul)

# print(a)
# print(list(acc))


from itertools import groupby

# def smaller_than_3(x):
#     return x<3


b = [1,2,3,4]

group_obj = groupby(b,key=lambda x: x<3)

for key, value in group_obj :
    # print(key, list(value))
    pass


persons = [{"name" : 'Tim', "age": 18}, {"name": "Lisa", "age": 30}, {"name":"Carol", "age":18}]

adults = groupby(sorted(persons, key=lambda x: x['age']), key=lambda person : person['age'])

for k, w in adults:
    # print(k, list(w))
    pass


#infinite iterators

from itertools import count, cycle, repeat

for i in count(10, 2):
    # print(i)
    if i == 20: break
    
t = [1,2,3]    
for i in repeat(t,4):
    print(i)
    
    
