"""
@Author  :Priya Babu

@Date    :23-02-2023

@Content :String slicing other functions
"""

# mystr = "JESUS I AM SRy"
# print(mystr)

# #lets look for slicing
# print(mystr[4])
# print(mystr[1:4])#here 1 is the starting point and 4-1 is the end point
# """
# notes:
# $To find the length use the function len()
# $ String can also indexed in negative way

# 0   1  2  3  4 5  6  7  8  9  10 11 12 13 14 15 16
# --|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
#                                 -5   -4  -3 -2   -1

# """

# '''

# MORE TO KNOW ON STRING..
# IN THE CODE BELOW IF U ONLY PUT A SINGLE QUOTE IT WILL SHOW U ERROR IF U WANT TO PRINT PUT 3 SINGLE OR 
# DUBLE QUOTE
# '''
# a="""
# hai how r u
# u look greak
# sexy
# huma
# miss u
# rahul"""

# print(a)

# """
# If u want to print or grt each values idividually u have to work with it using a for loop"""

# for i in a:
#     print(i)#Here we can use either character or i inorder to get the values

#     """
# SLICING IN DETAIL

#     """
NM = "Priya"
print(NM[:])

    # """
    # IF NO VALUES ARE PROVIDED FOR SLICING AUTOMATICALLY IT WILL BE THE START AND THE END VALUES
    # """

    # THEIR IS ALSO NEGATIVE SLICING PRESENT Ex
print(NM[-4:-5])#As for here total string length - 1 is the location i.e 5-1=4 th position to 5-4 = 1 this position will be printed