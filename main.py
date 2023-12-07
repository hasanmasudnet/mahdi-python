#user input
#username = input("enter your username:")
#password = input("enter your password:")
#print(username)
#print(password)



#type cast
name="32424242"
print(int(name))
print(type(int(name)))

num=32
print(float(num))



#my list
l=[1,2,3]
print(l[1])

l[2]=32
print(l)

list=["mahdi","wasif","neel"]
print(list)


list1=[True,False,False]
print(list1)



#access list items
Mahdi=["channelName","website","group","page"]
print(Mahdi[1])

#change lists
Mahdi[3]= "facebook"
print(Mahdi)


#append
Mahdi.append("Youtube")
print(Mahdi)

#insert
Mahdi.insert(2,"Roblox Bedwars")
print(Mahdi)

#delete
del Mahdi [1]
print (Mahdi)
#or,
Mahdi.pop(1)
print(Mahdi)


#clear list
Mahdi.clear()
print(Mahdi)




#loop lists


#for loop
looplist = ["mahdi", "wasif", "tahseen","neel","abul"]
for adamjee in looplist:
    print(adamjee)


#range() and len() loop X_X :
for i in range(len(looplist)):
    print(i)

x=0
while x<len(looplist):
    print(looplist[x])
    x=x+1



#list comprehensions
num=[1,2,3,4,5,6]
for i in (num):
    print(i*2)


double=[i*2 for i in num ]
print(double)
double=[i*3 for i in num]
print(double)



#sort list
number = [5,2,9,12,6]
number.sort()
print(number)


eng=["a","f","x",'g',"r","y"]
eng.sort()
print(eng)

math =[1,5,7,9,11]
math.reverse()
print(math)


num1=[1,2,3,4,5,6,7,8,9,10]
num2=num1.copy()
print(num2)


#join two lists
num1=[1,2,3]
num2=[4,5,6]
num3=num1+num2
print(num3)

num1.extend(num2)
print(num1)

print("hi world")