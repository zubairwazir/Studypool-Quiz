# def prime_num(num):
#     if num>1:
#         s=int(num/2)
#         for i in range(2,s+1):
#             if num%i==0:
#                 print("not prime")
#                 print("The factors of",num,"are:")
#                 for i in range(1, num + 1):
#                     if num % i == 0:
#                         print(i)
#                 break
#             return("prime")

# num = int(input("Enter a Number: "))
# print(prime_num(num)) 

for X in range(-5, 6):
    # print(X)
    Y = 8*X**2 + 1
    print(Y)