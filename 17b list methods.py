x=[1,2,3,'A','b',5.8,'b']
x1=[5,6,7]
print("index",x.index('b'))
print("count",x.count('b'))
print("pop last element",x.pop())
print("pop specific element",x.pop(3))
x.insert(3,'sandeep')
print("insert elements",x)
x.extend(x1)
print("extend",x)
x.append(x1)
print("append",x)
x.remove(5.8)
print("remove",x)
x.reverse()
print("reverse",x)
x1.sort()
print("sort in ascending",x1)
x1.sort(reverse=True)
print("sort in descending",x1)
