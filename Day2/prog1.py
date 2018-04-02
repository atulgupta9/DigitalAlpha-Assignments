# Write a program which will find all
# such numbers which are divisible by 9 but are
#  not a multiple of 5,between 0 and 3000 (both included). Print them on screen

for x in range(0, 3000):
    if x % 9 == 0 and x % 5 != 0:
        print(x)
