name1=input("enter the string :")
name2=input("enter the another string :")
new_string1= name1[:2] + name2[2:]
new_string2= name2[:2] + name1[2:]
result = new_string1 + " " + new_string2
print(result)