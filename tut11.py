#SETS
# s=set()
# print(type(s))
# s=set([1,2,3,4,5])
# s=set(s)
# s=set()
# s.pop()
# s.pop()
# s.pop()
# s.pop()

#..
# l=[9,1,2,2,2,3,4,8,1,5,3,4,5]
# s=set(l)

# s.add(255)
# s.pop()
# # s=s.union({10,20,30})
# # or
# s.update({10,20,30})
# s1=set([3,5,5,6,7,10,266,255])
# print(s1.isdisjoint(s))

l1=[1,2,3,4,5,6]
l2=[5,6,7,8,9,10]
s1=set(l1)
s2=set(l2)
print(s1)
print(s2)
l=(s1.union(s2))
print(l)
num=int(input("Enter a number\t"))
# aa=num in l
# if aa is False:
# if not aa:
if num in l:
    print("found")
else:
    print("dont exist")