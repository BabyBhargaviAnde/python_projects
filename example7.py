from collections import Counter    
c = Counter()  
list = [1,2,3,4,5,7,8,5,9,6,10]    
print(Counter(list) ) 
Counter({1:5,2:4}) 
list = [1,2,4,7,5,1,6,7,6,9,1]    
c = Counter(list) 
  
print(c[1])