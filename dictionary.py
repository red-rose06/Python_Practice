country = ('a', 'b', 'c', 'd')
continent = 'have fun'

d = dict.fromkeys(country, continent)

print(d)

d['key'] = 'value'
print(d)

del d['b']
print(d)

d.pop('a')
print(d)

d.update({"c":"one", "2":"two"})
print(d)