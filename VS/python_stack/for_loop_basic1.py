#1. Basic
for x in range(151):
    print(x)

#2. Multiples of Five
for x in range(5, 1005, 5):
    print(x)

#3. Counting, the Dojo Way
for x in range(1, 101, 1):
    print(x)
    if (x % 5) == 0:
        print("Coding")
    if (x % 10) == 0:
        print("Coding Dojo")

#4. Whoa. That Sucker's Huge
temp = 0
for x in range(0, 500000, 1):
    if (x % 2) != 0:
        temp = temp + x
print(temp)

#5. Countdown by Fours
for x in range(2018, 0, -4):
    if (x > 0):
        print (x)

#6. Flexible Counter
lowNum= 1
highNum= 15
mult= 4
for x in range(lowNum, highNum, 1):
    if x % 4 ==0:
        print(x)