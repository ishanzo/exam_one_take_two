# Teach the Padawans (middle schoolers) the ways of the force.

## Your goal is to create a lesson to teach absolute beginners how to program! There are two sections you may pick from. Your students must walk away with a working program and a class average of a B on your self made assessment.

## Section 1
### Criteria to Cover in your lesson
# Hello! Welcome to Python 101! Today we will be about the learning the basics of python! Ready?
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# We all know what variables are in math. It is a symbol for a number we don't know yet.  A variable is a tool used by computer scientists, like you, to keep track of different values while they're programming.
# In python, we can store variables as a number, decimals (aka floats in python), words or characters.
# We set a variable to something by using the operator, =. Time to make a variable!
# Since we know what variables are like in math, let's solve a math problem.
# You are having a taco party and you are going to teach your computer to make the tacos!
# You need two spoons of guacamole for each taco.
# variables
# So lets make a variable for the guac needed in each taco!
 guac = 2
# That was easy!
# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Now let's make it harder.
# Some of your friends LOVE guac and they want MORE! Ana wants 5 spoons of it in her taco, Sasha wants 4 and Evan wants 10.
# Lets make an 'array' of all the spoons of guacamole your friends want. Arrays are basically lists (like creating a shopping list before you go shopping for your taco party or a list of your classmates' grades, anything!).
# There are many cool things you can do with arrays: you can append (add) things to arrays, remove values from arrays and much more! But for now, let's just stick with making arrays.
# Lets name the array "spoons_of_guac".(This a naming convention, programmers like to use in python. It's basically all lowercase with spaces as underscores)
spoons_of_guac = [5,4,10]
# 5 for Ana, 4 for Sasha and 10 for Evan
# We just made an array!
# _________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Now that we have made an array of the teaspoons of guacamole our friends want, it's time to make it a little more complicated!
# Ana is actually not allowed to eat guacamole since she is a little allergic to it but if her parents don't come to the party, she'll eat.
# You may be wondering, "how do we put this complicated statement into a piece of code???" # It's actually pretty easy once you understand what conditionals are. To write this statement in code, we will be using conditionals!
# Conditionals are how we get computers to make simple decisions by checking if a statement is true or false. Conditionals allow us to have the computer make decisions!
# In this case, we would have to make a variable called "parents" to write the statement "if Ana's parents don't come to the party, she will eat 5 teaspoons of guacamole"
# So let's make our second variable to include Ana's parents.
parent = 0
# We are setting parent to 0 so that we can change it if a parent will be present in the party. For Ana's case, we are hoping parent equals to 0 so that she can eat her 5 spoons of guacamole!
# This is an if statement, a very popular conditional in the coding world.
if parent > 0:
# Here, we are basically saying that if parent is greater than 0, meaning that if there is a parent present more than no parent present at all...
    spoons_of_guac.remove(5)
 #... then Ana's 5 teaspoons of guac will be removed from our spoons_of_guac array we created above.
 # The ".remove" is just one of the many things you can do with arrays like I said earlier. It is REMOVING the value, 5 teaspoons of guac, from the array of all the teaspoons of guac your friends will have in their taco.
    print(spoons_of_guac)
 # Here we are just printing (a common function used in coding) in the array to let the host of the taco party know how many spoons of guacamole to prepareself.
# To let Ana know of this horrible news, let's tell her "Ana, you are not allowed to eat guac. Your parents are here"
    print("Ana, you are not allowed to eat guacamole. Your parents are here!!")
# We also just used a string in our print function! The computer takes into the piece of code when you use double or single quotations.
# You can use any type of quotations you want..just as long as you are consistent!
# Now, we need to let our computer know what will happen if Ana's parents are not there at the party.
# To tell our computer this, we will be the using the else statement.
# The else statement can be combined with an if statement (elif).
# An else statement contains the piece of code that executes if the conditional statement in the if statement is not true.
# The else statement is an optional statement and there can only be one else statement following if.
# So lets tell our computer that if there is no parent present in the party, Ana will be able to have 5 spoons of guac.
elif parent == 0:
# The "==" is used for conditionals, it just means equal but in conditional statement writing.
    print(spoons_of_guac)
# Now we are just printing the original array that had Ana's 5 teaspoons of guacamole.
# Let's tell Ana the good news!!
    print("ANA, YOU CAN HAVE YOUR 5 TEASPOONS OF GUAC! ENJOY!!")
else:
    print("TACO PARTY CANCELLED")
# The else statement is just there if nothing in the if or elif statement happens.
# We just wrote our first conditional statements and we taught out computer how to make decisions!!
# ________________________________________________________________________________________________________________________________________________________________________________________________________________________
# But...we're not done yet.
# Ana, Sasha and Evan wants 5 tacos each. So how do we tell our computer that?
# Instead of writing 15 repetitive lines of code, we can just use a for loop to make things easier and simple!
# Loops are used to make sections of code repeat themselves.
# This is helpful because then it keeps programmers from needing to retype the same instructions over and over again.
# Imagine how tiring and annoying that would be!
# Loops are also helpful if you want to repeat some code until a certain condition is met but we don't need to worry about that right now.
for guac in spoons_of_guac:
# Now, the "guac" is all the values in the array "spoons_of_guac"
# We just made a variable called "five_tacos" equal to the different spoons of guac times 5 (because each person wants 5 tacos with a specific amount of spoons of guac. I know, complicated!)
    print(guac * 5)

# The computer will print the variable, "five_tacos"
# Now you know how many spoons of guacamole needed for each person.
# Have fun making tacos for your friends and make sure you get some too!

# YAYYY!!! You just learned the basics of python!!! Congratulations!!!
# To prove your super awesome coding skills you will be challenged to create a guessing game with your partner!! It is very challenging!
# Here's the challenge: Create a Guess the Number game with a for loop and an if and/or else statement Tell them if they should guess higher or lower next time.
# Requirements: Use at least one loop and conditional.
