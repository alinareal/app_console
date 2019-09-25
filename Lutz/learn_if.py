choice = 'ham'
print {'spam': 1.25,
       'ham': 1.99,
       'eggs': 0.99,
       'bacon': 1.10}[choice]

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print branch.get('spam', 'Bad choice')
print branch.get('bacon', 'Bad choice')

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

print(6 or 7)

a = 'love'
b = 'good' if a else 'bad'
print(b)
print(bool('ffff'))
print([2, 4, 4][True])
