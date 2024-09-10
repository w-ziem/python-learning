import collections


string = 'aaaabbccdde'

acounter = collections.Counter(string)
# print(acounter)


#Cunter: return an dict with items and how many of them in a object

# print(acounter.most_common(1)[0][0])


class Point_class:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.pt = (x,y)

Point = collections.namedtuple('Point', 'x,y')

pt = Point(1,-4)

# print(pt.y)


ordered_dict = collections.OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

# print(ordered_dict)

def_dict = collections.defaultdict(0)

def_dict['a'] =1 
def_dict['b'] =2 


# print(def_dict['c'])

d = collections.deque()

d.append(1)
d.append(2)

print(d)

d.appendleft(3)


print(d)

