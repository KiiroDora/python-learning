strr = "aaaaaaaaaaaaaaaaaaaaaa"
kume = set(strr)
print(kume)

kume2 = set([1,2,3,4,5])
kume2.discard(3)

kume3 = set([2,4,5,6,7,8,9])

print(kume2)
print(kume2.difference(kume3))