L = []
binary_number = [x for x in input("Enter Binary Number:").split(',')]
for num in binary_number:
    x = int(num, 2)
    if x % 5 == 0:
        L.append(num)
    else:
        print("try again")


print(','.join(L))
print(L)
