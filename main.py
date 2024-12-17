# Love Calculator 
print("Welcome to the Love Calculator")

#Adding the variables to program
name1 = input("What is the first name ? \n")
name2 = input("What is the second name ? \n")

#Put together the both name in lower case
combine_name = str(name1).lower() + str(name2).lower()

#Counting
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
true = t + r + u + e

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")
love = l + o + v + e

#fist digit is "true" , the second digit is "love"
love_score = int(str(true) + str(love))

#Conditions 
if love_score < 10 or love_score > 90 :
    print("Say bye bye, you are always gonna be only friends")
else:
    if love_score>= 40 and love_score <= 50 :
        print("You are good together")
    else:
        print(f"Your score is : {love_score}")
        
# Fim da linha 
