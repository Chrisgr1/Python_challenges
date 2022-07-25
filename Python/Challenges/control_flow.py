# From Codecademy Beginner Python advanced challenges
#1 Create a function named in_range() that has three parameters named num, lower, and upper.The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
#2 Create a function named same_name() that has two parameters named your_name and my_name. If our names are identical, return True. Otherwise, return False.
#3 Create a function named always_false() that has one parameter named num.Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num. An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.
#4 Create a function named movie_review() that has one parameter named rating.If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"
#5 Create a function called max_num() that has three parameters named num1, num2, and num3. The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

#1 Create a function named in_range() that has three parameters named num, lower, and upper.The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

print ("triple ten", in_range(10,10,10))
print ("False - 5,10,15", in_range(5,10, 15))
print("False - 10, 100, 5", in_range(10,100,5))

#2 Create a function named same_name() that has two parameters named your_name and my_name. If our names are identical, return True. Otherwise, return False.
def same_name(your_name, my_name):
    if your_name==my_name:
        return True
    else:
        return False

print("True, Jo-Jo", same_name("Jo","Jo"))
print("False, Joe-Jo", same_name("Joe","Jo"))