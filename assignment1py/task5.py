name=input("enter the string :")
for i in name:
    if i[:-3]=="ing":
        print("the string contains ing form")
    else :
        print(i.replace("[:-3]","ly"))