# 1st question
x=int(input('enter the score'))
if x<25:
    print('grade is F')
elif x>=25 and x<45:
    print('grade is E')
elif x>=45 and x<50:
    print('grade is D')
elif x>=50 and x<60:
    print('grade is C')
elif x>=60 and x<80:
    print('grade is B')
elif x>=80:
    print('grade is A')
    
# 2nd question
x=int(input('Enter the year'))

if x%4==0 and x%400==0:
    print('It is a leap year')
elif x%4==0 and x%100==0:
    print('It is not a leap year')
elif x%4==0:
    print('It is a leap year')
else:
    print('It is not a leap year')

# 3rd question
import random
i=0
while i<10:
    i+=1
    a=random.randint(0,10)
    b=random.randint(0,10)
    print("question",i,"=",a,"*",b)
    ans=int(input("enter your answer"))
    
    if ans==a*b:
        print("correct answer")
    else:
        print("incorrect answer. the correct answer is",a*b)
        
# 4th question
for candies in range (200):
    if (candies%5!=2):
        continue
    if (candies%6!=3):
        continue
    if (candies%7!=2):
        continue
    print(str(candies),"is the answer")
