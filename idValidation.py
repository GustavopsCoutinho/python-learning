import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese))
cheese[1]=42
print (spam)
print (cheese)



bacon = 'hello'
print(bacon)
print(id(bacon))
bacon = 'would'
print(bacon)
print(id(bacon))