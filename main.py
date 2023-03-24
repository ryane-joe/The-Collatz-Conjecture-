#change x to whatever num u want to start w 
x = 7
#make this while loop a while True loop to just keep printing instead of quitting once the number has reached 1
while x != 1:
    #checks if the number is even
    if x % 2 == 0:
      #if number is even then divides by two and prints it
        x = x/2
        print(x)
   #checks if number is odd     
    elif x % 2 != 0:
      #if odd, multiplies by three and adds one, then prints
        x = x *3 +1
        print(x)
    
 '''
 THe collatz Conjecture is that any positive number, when applying the rules :
 if even then divide by two
 and if that number odd then multiply by 3 and add one if even, repeat even rule
 following these rules, it ensures that the loop always ends in a repetative loop of the number first reaching 1, then increasing to 4, then reducing to 2, reaching 1 and so on
 '''
#MADE BY RYANE
