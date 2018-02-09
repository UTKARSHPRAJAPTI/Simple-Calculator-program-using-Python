
# coding: utf-8

# In[21]:


def sum(a1,a2):
    print("Addition")
    print(a1+a2)
def mul(a1,a2):
    print("Multiply")
    print(a1*a2)
def div(a1,a2):
    print("Division")
    print(a1/a2)
def sub(a1,a2):
    print("Subtraction")
    print(a1-a2)

print("Please Select any Opreation \n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n")

select=input("Slect Opreation from 1,2,3,4")
a1=int(input("Enter first number"))
a2=int(input("Enter secound number"))
if select=='1':
    sum(a1,a2)
elif select=='2':
    sub(a1,a2)
elif select=='3':
    mul(a1,a2)
elif select=='4':
    div(a1,a2)
else:
    print("Invalid key please try again")

