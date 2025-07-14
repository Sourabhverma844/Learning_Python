number1 = int(input("Enter Numb 1:"))
number2 = int(input("Enter Numb 2:"))
numblist = []
for i in range (number1,number2):
    numblist.append(i)
for i in range (0,len(numblist)):
    if numblist[i]>5:
        numblist[i]%2 == 0
        print("First even number greater than 5:",numblist[i])
        break
for i in range (0,len(numblist)):
    if numblist[i]%7 == 0:
        print("First number divisible by 7:",numblist[i])