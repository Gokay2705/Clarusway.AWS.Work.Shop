# Efficient Python program to print all non- 
# repeating elements. 
  
def firstNonRepeating(products, n): 
      
    # Insert all array elements in hash 
    # table 
    mp={} 
    for i in range(n): 
        if products[i] not in mp: 
            mp[products[i]]=0
        mp[products[i]]+=1
          
    # Traverse through map only and 
    for x in mp: 
        if (mp[x]== 1): 
            print(x,end=", ") 
              
# Driver code 

products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

n = len(products) 
print(firstNonRepeating(products, n)) 