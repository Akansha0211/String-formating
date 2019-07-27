# a="Akansha"
# b="This is %s",a
# print(b)

# ('This is %s', 'Akansha')


"""a="Akansha"
b="This is %s"%a
print(b)"""
#This is Akansha

#why we do need F strings
"""a="Akansha"
c="Aastha"
d="Vivek"
e="Aakarsh"
f="Ansh"
g="Ananya"
h="Ankita"
i="Pragya"
b="Me and my friends %s%s%s%s%s%s%s%s"%(a,c,d,e,f,g,h,i)
print(b)"""
# c="me"
# d="Akansha"
# a="This is {} {}"
# b=a.format(c,d)
# print(b)

# c="me"
# d="Akansha"
# a="This is {1} {0}"
# b=a.format(c,d)
# print(b)


#USING F STRING
# c="me"
# d="Akansha"
# e=f"THis is {c} {d} {4*65}"
# print(e)

# import math
# c="me"
# d="Akansha"
# e=f"This is {c}{d}{math.cos(65)}"
# print(e)

#F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format().


# answer = "456"
# a=f"Your answer is {answer}"
# print(a)

# answer = 456
# a=f"Your answer is {str(answer)}"
# print(a)

# print("{},My passion".format("my goal"))
# print("{} My passion".format("my goal"))

# a="This is python {}"
# b=a.format("my love")
# print(b)

#Index error is thrown when there are more placeholders then the values passed as parameters in format method
# a="{} is very {} for hackers {}"
# b=a.format("Python","useful")
# print(b)
#IndexError: tuple index out of range.


#SyntaxError: positional argument follows keyword argument
# a="{2} is a very effective for {x}"
# b=a.format("Python",x="hackers","JAVA")
# print(b)

#Keyword argument
# a="{} is a very effective for {x}"
# b=a.format("Python",x="hackers")
# print(b)

# a="{x} is a very effective for {x}"
# b=a.format("Python",x="hackers")
# print(b)


# a="{y} is a very effective for {x}"
# b=a.format("Python",x="hackers",y="JAVA")
#print(b)

# a="{0} is a very effective for {1}"
# b=a.format("Python",x="hackers")
# print(b)
#IndexError: tuple index out of range


#POSITIONAL ARGUMENTS
# a="{0} is a very effective for {1}"
# b=a.format("Python","hackers")
# print(b)

# Reverse the index numbers with the  parameters of the placeholders
# a="{1} is a very effective for {0}"
# b=a.format("Python","hackers")
# print(b)
#hackers is a very effective for Python


#index numbers of the  values to change the order that they appear in the string
# a="{0} {2} is a very effective for {1}"
# b=a.format("Python","hackers","Java")
# print(b)

# s – strings
# d – decimal integers (base-10)
# f – floating point display
# c – character
# b – binary
# o – octal
# x – hexadecimal with lowercase letters after 9
# X – hexadecimal with uppercase letters after 9
# e – exponent notation

# a=" I have secured {0:f}% which is just {1}"
# b=a.format(75.0000,"average")
# print(b)
# I have secured 100.000000% which is just average

# a=" I have secured {0:.2f}% which is just {1}"
# b=a.format(75.0000,"average")
# print(b)


# a="The {0} of 100 is {1:b}"
# b=a.format("binary", 100)
# print(b)

# a="The {0} of 100 is {1:o}"
# b=a.format("binary", 100)
# print(b)


#By default strings are left-justified within the field, and numbers are right-justified.
# <   :  left-align text in the field
# ^   :  center text in the field
# >   :  right-align text in the field

# a="{0:50}, is the computer science portal for {1:8}!"
# b=a.format("GeeksforGeeks", "geeks")
# print(b)
#GeeksforGeeks                                     , is the computer science portal for geeks   !

# print("It is {0:30} degrees outside ".format(40))
# It is                             40 degrees outside


# print("{0:^80} DOB  {1:<10}".format("Akansha", 211))
#                                    Akansha                                      DOB  211

# print("{:*^60}".format("Akansha"))
#**************************Akansha***************************


#To demonstrate organization of large data
# def unorganized(n1,n2):
#     for i in range(n1,n2):
#         print(i,i**2,i**3,i**3)
#     print()
# def organized(n1,n2):
#     for i in range(n1,n2):
#         print("{:6d}{:6d}{:6d}{:6d}".format(i,i**2,i**3,i**4))
#     print()
# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# print("{:*^60}".format("Unorganized data"))
# unorganized(a,b)
# print("{:*^60}".format("Organized data"))
# organized(a,b)

#OUTPUT
# Enter first number4
# Enter second number9
# **********************Unorganized data**********************
# 4 16 64 64
# 5 25 125 125
# 6 36 216 216
# 7 49 343 343
# 8 64 512 512
#
# ***********************Organized data***********************
#      4    16    64   256
#      5    25   125   625
#      6    36   216  1296
#      7    49   343  2401
#      8    64   512  4096

