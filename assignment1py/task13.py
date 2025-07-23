d={'a':3,'b':1,'c':2}
asc=dict(sorted(d.items(),key=lambda items:items[1]))
desc=dict(sorted(d.items(),key=lambda items:items[1],reverse=True))
print("asecending",asc)
print("desecending",desc)