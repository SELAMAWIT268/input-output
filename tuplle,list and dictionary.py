# I. Find length of tuple without len()
t = (1,2,3,4,5)
count = 0
for _ in t:
    count += 1
print(count)

# II. Max & Min of tuple
nums = (4,7,1,9,3)
print(max(nums), min(nums))

# III. Remove duplicates
lst = [1,2,2,3,4,4,5]
lst = list(set(lst))
print(lst)

# IV. Square elements
lst = [1,2,3,4,5]
squares = [x**2 for x in lst]
print(squares)

# V. Merge dictionaries
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
merged = {d1, d2}
print(merged)

# VI. Swap keys/values
d = {'a':1,'b':2,'c':3}
swapped = {v:k for k,v in d.items()}
print(swapped)

# VII. Fibonacci with memoization
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n<=1: return n
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
print(fib(10))

# VIII. Pythagorean triplets
n=20
triplets = [(a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a*a+b*b==c*c]
print(triplets)

# IX. Shopping cart
cart = {}
def add_item(item,price,qty):
    cart[item] = cart.get(item,0)+qty*price
def total():
    return sum(cart.values())

add_item("apple",10,2)
add_item("banana",5,3)
print(cart, total())

# X. Dictionary-based cache (LRU)
from collections import OrderedDict
class LRUCache:
    def init(self,max_size=3):
        self.cache=OrderedDict()
        self.max_size=max_size
    def get(self,key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    def put(self,key,value):
        self.cache[key]=value
        self.cache.move_to_end(key)
        if len(self.cache)>self.max_size:
            self.cache.popitem(last=False)

cache=LRUCache(2)
cache.put(1,1); cache.put(2,2)
print(cache.get(1))
cache.put(3,3) # evicts 2
print(cache.get(2))

# XI. Tuple even numbers
def even_tuple(t):
    return tuple(x for x in t if x%2==0)
print(even_tuple((1,2,3,4,5,6)))

# XII. Sort list of tuples by second element
data=[('a',3),('b',1)]
data.sort(key=lambda x:x[1])
print(data)

# XIII. Flatten nested list
def flatten(lst):
    res=[]
    for i in lst:
        if isinstance(i,list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res
print(flatten([[1,2],[3,4]]))

# XIV. Remove all occurrences
lst=[1,2,3,2,4,2]
lst=[x for x in lst if x!=2]
print(lst)

# XV. Invert dictionary (duplicates handled)
d={'a':1,'b':2,'c':1}
inv={}
for k,v in d.items():
    inv.setdefault(v,[]).append(k)
print(inv)

# XVI. Student with highest average
marks={"John":[80,90,70],"Jane":[85,95,100]}
best=max(marks.items(), key=lambda x: sum(x[1])/len(x[1]))
print(best[0])
