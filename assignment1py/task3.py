b=input("write the sentence :")
word=b.split()
count_b={}
for i in word:
   if i in count_b :
      count_b[i] += 1
   else :
      count_b[i] = 1
      print(count_b)
      
      

    
