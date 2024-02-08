#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("enter the number of student:"))
print("1.tamil\n2.english\n3.maths\n4.science\n5.social:")
if n>0:
    for i in range(1,n+1):
        name=input("enter student name:")
        tamil=int(input("enter the tamil mark:"))
        english=int(input("enter the english mark:"))
        maths=int(input("enter the maths mark:"))
        science=int(input("enter the science mark:"))
        social=int(input("enter the social mark:"))
        percentage=(tamil+english+maths+science+social)/5
        print("name:",name,"\ntamil",tamil,"\nenglish",english,"\nmaths",maths,"\nscience",science,"\nsocial",social,"\npercentage",percentage,"%")
        if percentage<=100 and percentage >=90:
            print("grade=O")
        elif percentage<=89 and percentage >=80:
            print("grade=A+")
        elif percentage<=79 and  percentage>=70:
            print("grade=A")
        elif percentage<=69 and  percentage>=60:
            print("grade=B+")
        elif percentage<=59 and  percentage>=50:
            print("grade=B")
        elif percentage<=49 and percentage >=40:
            print("grade=C+")
        elif percentage<=39 and  percentage>=35:
            print("grade=C")
        else:
            print("grade=U")
        
            

