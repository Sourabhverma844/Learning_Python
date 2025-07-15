"""
MY Method
days = ["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
day = int(input("Enter Day Value it Should between 0 to 6: "))
n_before_days = int(input("Enter Before Days : "))
if 0 <= day < 7:
    if n_before_days > 6:
        n_before_days = n_before_days % 6
        print(days[day-n_before_days])
    else:
        print(days[day-n_before_days])
else:
    print("Enter Valid Day Value From 0 To 6")
"""
days = ["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
d = int(input("Enter d: "))
n = int(input("Enter n: "))
print(days[(d-n)%7])