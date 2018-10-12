# Create a function to help Mr. James plan for a donut celebration

arr = [90,80,66,75,88]
def donut_celeb(arr):
    ## Input: Exam Scores for all students
# Conditions
    for avg in arr:
        add = sum(arr)
        average = add/len(arr)
        print(average)
    ## Output: How many donuts
        donuts = len(arr)
## If the class average is an A, every student gets a donut
        if average >= 90:
            return donuts
## If the class average is a B, every student gets a half donut. Make sure not to round half donuts up. Return the float.
        elif 90 > average >= 80:
            half_donut = donuts/2
            return half_donut
## If the class average is a C, every student gets 1/3 of a donut. Make sure not to round up, but to return the float
        elif 80 > average >- 70:
            third_donut = donuts/3
            return third_donut
## If the class average is a D, every student will give Mr. James a half donut.
        elif 70 > average >= 60:
            return half_donut
        else:
            break
print(donut_celeb(arr))
# Step One
## Create a flow chart for your algorithm

# Step Two
## Create your function. Fully comment out you code.

# Step Three
## Beta test your function with another group. How can you make you function better?
# By making it less repetitive.
