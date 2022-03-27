from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

d = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(d, c, sep='\n')

print('*' * 50)
d = deque([i for i in range(5)])
d.append(5)
d.appendleft(6)
print(d)

print('*' * 50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)

print('*' * 50)
with open('log.txt', 'r', encoding='utf-8') as f:
    last_ten = dequ(f, 10)

print(last_ten)