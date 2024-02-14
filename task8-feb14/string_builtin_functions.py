#1.capitalize..
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
#2.find..
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
#3strip..
txt = "banana"
x = txt.strip()
print("of all fruits", x, "is my favorite")
#4.format..
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
#5.isalnum
txt = "Company12"
x = txt.isalnum()
print(x)
#6.isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)
#7.lower..
txt = "COMPANYX"
x = txt.lower()
print(x)
#8.upper..
txt = "company"
x = txt.upper()
print(x)
#9.replace..
txt = "your company is good"
x = txt.replace('company','house')
print(x)
#10.split
txt = "your company is good"
x = txt.split()
print(x)
#11.count..
txt = "your company is good.company has lot of employe"
x = txt.count('company')
print(x)
#12.index..
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
# 13.isdigit..
txt = "50800"
x = txt.isdigit()
print(x)
#14. islower..
txt = "hello world!"
x = txt.islower()
print(x)
#15. isupper..
txt = "HELLO WORLD!"
x = txt.isupper()
print(x)
