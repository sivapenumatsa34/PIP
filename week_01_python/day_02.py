# # # # # # #conditional statements

# # # # # # #num = int(input("Enter a number: "))
# # # # # # #if num%2 == 0:
# # # # # #     #print(num,"is a even number")
# # # # # # #else:
# # # # # #     #print(num,"is a odd number")


# # # # # # temp_c = int(input("Enter the temp in celsius: "))

# # # # # # if temp_c < 15:
# # # # # #     print("Cold")
# # # # # # elif temp_c <= 29:
# # # # # #     print("Pleasant")
# # # # # # elif temp_c <= 39:
# # # # # #     print("Warm")
# # # # # # else:
# # # # # #     print("Heatwave")

# # # # # year=int(input("Enter the year: "))
# # # # # if year%400 == 0 or (year%4 == 0 and year%100 != 0):
# # # # #     print(year,"is a leap year")
# # # # # else:
# # # # #     print(year,"is not leap year")

# # # # n=int(input("Enter a number:"))
# # # # if n%2!= 0:
# # # #     print("weird")
# # # # elif 2 <= n <=5:
# # # #     print("not weird")
# # # # elif 6 <=n <=20:
# # # #     print("weird")
# # # # else:
# # # #     if n>20:
# # # #         print("not weird")


# # # # Loops
# # # for i in range(1,6):
# # #     print(i)

# # number = 1
# # while number <= 5:
# #     print(number)
# #     number +=1

# # n=int(input("Enter a number:"))
# # count=0
# # for i in range(n):
# #     if i%2==0:
# #         print(i)
# #         count+=1
# # print("Count of even numbers:", count)

# n=int(input("Enter a number:"))
# sum=0
# for i in range(n+1):
#     sum=i+sum
# print(sum)

# n=int(input("num"))
# for i in range(n+1):
#     print(i**2)

# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime==True:
#         print(i)

n = input("Enter a number:")
reverse=""
for i in n:
    reverse=i+reverse
print(reverse)

