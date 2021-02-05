#enryption code
def encryption(pt,key,z):
 ptlist = list(pt) #take  text  string in to list 
 x=0
 ct= " "
 for i in ptlist:
     #print(x)
     
     key=(3*x)+z
     x=x+1
     print(key)
     asc = ord(i)
     asc = asc + (key % 26)
     if i.isupper():
         if asc > 90:
             asc = asc - 26
     elif i.islower():
             if asc > 122:
                 asc = asc - 26
     newch = chr(asc)
     ct = ct + newch
 return ct 


#decryption code
 
def decryption(ct,key,z):
 cflist = list(ct) #take  text  string in to list
 x=0
 pt = " "
 for i in cflist:
     key=(3*x)+z
     x=x+1
     print(key)
     asc = ord(i)
     asc = asc - (key % 26)
     if i.isupper():
         if asc <65:
             asc = asc + 26
     elif i.islower():
             if asc < 97:
                 asc = asc + 26
     newch = chr(asc)
     pt = pt + newch
 return pt 


#enter value from user 
choice = int(input("1.Encryption 2.Decryption :- "))
if choice == 1:
 pt = input("Enter any text: ")
 key = int(input("Enter key: "))
 z=int(input("Enter z: "))
 cf = encryption(pt,key,z)
 print ("orignal text: ",pt)
 print ("encrypt text:",cf)
elif choice == 2:
 cf = input("Enter any text: ")
 key = int(input("Enter key: "))
 z=int(input("Enter z: "))
 pt = decryption(cf,key,z)
 print ("orignal text: ",cf)
 print ("encrypt text:",pt) 