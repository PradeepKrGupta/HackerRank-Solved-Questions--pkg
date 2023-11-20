# >>>>>>>>>>>>>>>>>>Question 2<<<<<<<<<<<<<<<<<<<<<<<

# n = int(input("Enter the size of the array :"))
# arr = []

# for i in range(n):
#     val = int(input(f"Enter the value {i} in the list :"))
#     arr.append(val)

# arr.sort()
# sum = 0
# for i in range(n):
#     sum+=(arr[i]*i)

# print("The sum of number is :",sum)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>Question 3<<<<<<<<<<<<<<<<<<<
# n = int(input("Enter the size of the array :"))
# arr_one = []
# arr_two = []
# for i in range(n):
#     val1 = int(input(f"Enter the value {i} in the first list :"))
#     arr_one.append(val1)

# for i in range(n):
#     val2 = int(input(f"Enter the value {i} in the second list :"))
#     arr_two.append(val2)

# arr_one.sort()
# arr_two.sort(reverse=True)
# print(arr_one)
# print(arr_two)

# sum = 0
# for i in range(n):
#     sum+=(arr_one[i]*arr_two[i])

# print("The minimum sum is :",sum)


n=3
strval = f'{n}'
if n%3==0:
    newStr = strval *5

print(newStr)