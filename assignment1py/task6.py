text = input("Enter a string: ")
nott = text.find('not')
poor = text.find('poor')
if nott != -1 and poor != -1 and nott < poor:
    text = text[:nott] + 'good' + text[poor+4:]
print("Result:", text)
