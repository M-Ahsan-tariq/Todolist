# num = (1, 4, 9, 16, 25, 36, 49, 64, 81,1000)
# index = 0
# x = int(input("Enter the number"))
# while index < len(num):
#     if (num[index] == x):
#         print("number found at",index)
#     else:
#         print("not found")
#     index+=1
# ______________________________________________________
# x = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0
# num = int(input("enter the num"))
# while idx < len(x):
#     if num == x[idx]:
#         print("number founded")
#         break
#     else:
#         print("finding..")
#     idx+=1
# print("loop ended")
# _________________________________________________________________
# price = 78.59878625
# txt = f"the price is just {price:.2f}!"
# print(txkaracji


# _________________________________________________
# def describe_city(city, country = "india"):
#     print(city,"is in",country)
#     return
# # recalling the condition
# describe_city("karachi", "pakistan")
# describe_city("United States", "North America")
# describe_city("Dehli", )
# __________________________________________________
# def max(a , b , c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# result = max(65 , 78 , 21)
# print(result,"is the largest number")
# _______________________________________________________
# def find_gcd(a,b):
#     while b!=0:
#         r = a % b
#         a = b 
#         b = r
#     return a
    
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# result = find_gcd(num1,num2)
# print("GCD of",num1,"and",num2,"is",result)
# # ____________________________________
# def find_gcd(a, b):          # Step 1: We define a function called find_gcd that takes 2 numbers (a and b)
#     while b != 0:            # Step 2: Keep doing this as long as b is not 0
#         r = a % b            # Step 3: r is the remainder when a is divided by b
#         a = b                # Step 4: Now, set a to b
#         b = r                # Step 5: Set b to the remainder (r)
#     return a                 # Step 6: When b becomes 0, a is the GCD (we return it)

# # Getting input from user
# num1 =int(input("Enter the first number")) # Step 7: Ask the user to enter the first number
# num2 = int(input("Enter second number: "))  # Step 8: Ask for the second number

# # Calling the function
# gcd = find_gcd(num1, num2)   # Step 9: Call the function using the two numbers and save the result in gcd
# # Showing the result
# print("GCD is", gcd)         # Step 10: Show the answer to the user
# num = 2
# while num<10:
#     fact = 1
#     i = 1
#     while i<=num:
#         fact*=i
#         i+=1
#     print(f"The factorial of {num} is {fact}")
#     num+=1
# for i in range(2,6):
#     for j in range(2,i+1):
#         j*=i
#     print(f'|The factorial of {i} is {j}')

# for i in range(2, 6):
#     fact = 1
#     for j in range(2, i + 1):
#         fact *= j
#     print(f'The factorial of {i} is {fact}')
# choice = 'y'
# while choice == 'y' or choice == 'Y':
#     num = int(input('Enter the num for table: '))
#     i = 1
#     while i<11:
#         print(num,'x',i,'=',i*num)
#         i+=1
#     choice = input('Do you want to do it again?(y/n)')

# def sum(i1, i2):
#  result = 0
#  for i in range(i1, i2+1):
#      result += i
#      return result
# def main():
#     print("Sum from 1 to 10 is", sum(1, 10)) 
#     print("Sum from 20 to 37 is", sum(20, 37))
#     print("Sum from 35 to 49 is", sum(35, 49))
# main() # Call the main function
# def sum(number1, number2):
#   total = number1 + number2
# print(sum(1, 2))
# def sta(message,n):
#    for i in range(0,n):
#       print(message)
# sta(n=4,message="welcome to python")
# x = eval(input("Enter a number: "))
# if (x > 0):
#  y = 4
# print(y)
# def reverse(lst):
#     result = []
#     for i in lst:
#         result.insert(0,i)
#     return result
# list1 = [1,2,3,4,5,6]
# list2 = reverse(list1)
# print(list2)

# def reverse(lst):
#     result=[]
#     for i in list:
#         result.insert(0,i)
#     return result
# list1 = [1,2,3,4,5,6]
# list2 =
# -----------------------------
# books = []
# Stationery = []
# for i in range(1,6):
#     books_items = input("Enter the five items for book")
#     books.append(books_items)

# for j in range(1,6):
#     Stationery_items = input("Enter the five items for book")
#     Stationery.append(Stationery_items)



print("Enter 5 items for each category.\n")

books = []
stationery = []
electronics = []

print("Enter Books:")
for _ in range(5):
    books.append(input("Book: "))

print("\nEnter Stationery:")
for _ in range(5):
    stationery.append(input("Stationery: "))

print("\nEnter Electronic Gadgets:")
for _ in range(5):
    electronics.append(input("Gadget: "))

combined = books + stationery + electronics

n = len(combined)
for i in range(n):
    for j in range(0, n - i - 1):
        if combined[j].lower() > combined[j + 1].lower():
            combined[j], combined[j + 1] = combined[j + 1], combined[j]

sorted_books = []
sorted_stationery = []
sorted_electronics = []

for item in combined:
    if item in books:
        sorted_books.append(item)
    elif item in stationery:
        sorted_stationery.append(item)
    elif item in electronics:
        sorted_electronics.append(item)

print("\nSorted Books:")
for b in sorted_books:
    print("-", b)

print("\nSorted Stationery:")
for s in sorted_stationery:
    print("-", s)

print("\nSorted Electronic Gadgets:")
for e in sorted_electronics:
    print("-", e)
