
# # ~`~CHECK PRIME NUMBER USING FOR LOOP~`~

# # Check specific number


num = int(input("Enter Number:"))
for i in range (2, num):
        if num % i == 0:
            print(num, "is not prime number")
            break
else:
    print(num, "is prime number")


# # 1 to 100 using For Loop


print("\n 1 to 100 Numbers")
for num in range (1,101):
    count = 0
    for i in range (2,(num // 2 + 1)):
        if (num % i == 0):
            count = count + 1
            break
    if (count == 0 and num != 1):
        print(" %d " %num, end = '   ')


# #  1 to N using For Loop


min = int(input("\nEnter MINIMUM value:"))
max = int(input("\nEnter MAXIMUM value:"))
for num in range(min, max + 1):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        print("%d" %num, end='    ')


print("\t\t\t\n\nThanks")



