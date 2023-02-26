#::::::::::===== Task 5 ====:::::::::
#Question 1: Design a calculator that take two inputs from the user and perform mathematical operations
print("Enter first number ")
a=int(input())
print("Enter second number")
b=int(input())
add=a+b
sub=a-b
multi=a*b
division=a/b
floar_division=a//b
print("The sum of",a, " and ", b, " is = ", add)
print("The difference of",a,"and ",b," is = ", sub)
print("The multiplication of",a, "and",b,"is = ", multi)
print("The division of",a,"and",b,"is = ", division) 
print("The floar division of ",a,"and",b,"is = ",floar_division)

#Question 2: Take two arguments from user and check whether they are equal or not
print("Enter first number ")
a=input()
print("Enter another number ")
b=input()
print(a==b)

#Question 3: Design a system that calculate the area of plot
# area =length * width
print("Enter the length of a plot ")
lenght=int(input())
print("Enter width of the plot ")
width=int(input())
Plot_area=width*lenght
print("The area of the plot is = ",Plot_area)

#Question 4: Design a BMI system both in metric unit and Us unit
#Metric Unit
print("Enter Your weight")
w=float(input())
print("Enter Your  height in centimeter ")
h=float(input())
height=(h*h)*(100*100)
bmi=w/height
print("Your BMI is = " ,bmi)


#BMI In US unit
print("Enter Your weight in lbs")
w=float(input())
print("Enter Your  height in inches ")
h=float(input())
bmi=w/(h**2) * 703
print("Your BMI is = " ,bmi)
'''Question 5: Create a program that convert:
 User weight in kG into pounds 
 height meter into inches
 Radian to degree '''
 
print("Enter The weight in Kg ")

w=float(input())
pound=w*2.205
print("The Weight in Pound is = " , pound)

print("Enter the height in Meter ")
h=float(input())
inh=h*39.37
print("Your height in Inches is = " ,inh)

print("Enter angle in Radian ")
r=float(input())
degree=r*57.3
print("Your angle in degree is = " ,degree)



