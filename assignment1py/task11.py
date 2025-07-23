lst = [(1, 'a'), (2, 'b'), (3, 'c')]
a, b = zip(*lst)
print("Unzipped lists:", list(a), list(b))
