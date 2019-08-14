import copy
f = ["asdf"]
a = {"a": {'hi':'asf'}}
b = copy.deepcopy(a)
b['a']['hi'] += 'hi'
print(a['a']['hi'])
print(b['a']['hi'])