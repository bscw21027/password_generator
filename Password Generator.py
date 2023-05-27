import random
p=[]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


n_let = int(input(" Enter the number of letters : "))
n_num= int ( input ( " Enter the number of Numbers : ")) 
n_sym= int ( input ( " Enter the number of Symbols : ")) 
 
for i in range(0,n_let):
   p += random.choice(letters)
for i in range(0,n_num):
   p += random.choice(numbers)
for i in range(0,n_sym):
   p += random.choice(symbols)
pas=""  
pal=""  
for i in p:
    pas+=i
print(f"\n Your randomly generated password (EASY) : {pas}")
random.shuffle(p)
for i in p:
    pal+=i
print(f"\n Your randomly generated password (HARD) : {pal}")    













   