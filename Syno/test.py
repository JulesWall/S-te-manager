d1 = {'a':1, 'b':2}
d2 = list()
for a in d1.items():
    d2.insert(0, (a[0], a[1]))
d2 = dict(d2)

print(d2)