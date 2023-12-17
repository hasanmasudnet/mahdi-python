'''
#user input
username = input("enter your username:")
password = input("enter your password:")
print(username)
print(password)





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


5>2
print(5>2)




#matrix
Mahdilist=[
    [1,2,3,4,5],
    [6,7,8,9,10]
]
print(Mahdilist[0][3])


#tuples
Newtuple=(1,2,3,"Mahdi","Wasiul",False)
print(type(Newtuple))


#negative indexing
print(Newtuple[-3])

#range of indexes
print(Newtuple[2:4])


#update tuples
x=list(Newtuple)
x.append("Mahad")
print(x)
Newtuple=tuple(x)
print(Newtuple)




#Unpack Tuples
games = ("roblox","gta5","minecraft")
(r,g,m) = games
print(g)
(*r,)= games
print(r)

#tuple loop
for i in games:
    print(i)
for x in range(len(games)):
    print(x)

z=0
while z<len(games):
    print(games[z])
    z=z+1




#join 2 tuple
num1=(1,2,3,4,5)
num2=(6,7,8,9,10)
print(num1+num2)
x= num1*2
print(x)

#count
num1=(3,4,2,4,2,4,6,2,4,7,5)
x=num1.count(2)
print(x)

#index
y=num1.index(7)
print(y)


#sets
Myset = {False,1,"Mahdi"}
print(Myset)
print(len(Myset))


#Access set items
for i in Myset:
    print(i)
    print(1 in Myset)



#add set items
Mylist1={"Mahdi","Wasif","Ahiyaan","Tahseen"}
Mylist1.add("Mahad")
print(Mylist1)


#set update
Set2={"Roblox","Bedwars","Minecraft","GTA6"}
Set3={10,5,2,1}
Set2.update(Set3)
print(Set2)


#Remove set items
num1={1,2,3,4,5,6}
num1.remove(4)
print(num1)


#discard set items
num1.discard(1002320930)
print(num1)

#pop set items
num2={6,7,8,9,10}
num2.pop()
print(num2)


#clear set items
num2.clear()
print(num2)


#loop set items
fruits={"apple","banana","cherry"}
for mahdi in fruits:
    print(mahdi)


#join set items
set1={"a","b","c"}
set2={1,2,3}
print(set1.union(set2))



#dictionaries
StudentInfo={
    "Mahdi":{
        "location":"Dhaka",
        "roll":15,
        "class":5,
   },
    "Wasif":{
        "location":"Dhaka",
        "roll":9,
        "class":5,
   },
    "year":2012


}

print(StudentInfo)
print(StudentInfo["Wasif"]["roll"])



#dictionary accessing items


#get function
print(StudentInfo["year"])
x=StudentInfo.get("Wasif")
print(x)


#keys function
y=StudentInfo.keys()
print(y)


#values function
print(StudentInfo.values())



#dictionaries changing items
StudentInfo["year"]=1971
print(StudentInfo["year"])

#update function
StudentInfo.update({"Mahdi":"Mahdi is a roblox player"})
print(StudentInfo["Mahdi"])



#pop fuction
print(StudentInfo.pop("Mahdi"))


#popitem fuction
print(StudentInfo.popitem())





#loop dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print(x)
for y in thisdict.values():
    print(y)
for z in thisdict.keys():
    print(z)
for item in thisdict.items():
    print(item)



#copy dictionary
a=thisdict.copy()
print(a)


b=dict(thisdict)
print(b)

#conditions


a=500**2
b=2**500000000

if (a>b):
    print("a is greater than b")

elif (a<b):
    print("b is greater than a")

elif (a!=b):
    print("they are not equal")

elif (a==b):
    print("they are equal")

else:
    print("sorry! a is not greater than b")




#loops
mahdi=0
while mahdi<50:
    print("yes mahdi is less than ",mahdi)
    mahdi=mahdi+1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#functions

sum1=23
sum2=44
sum3=sum1+sum2
print(sum3)

sum4=23
sum5=44
sum6=sum1-sum2
print(sum6)
'''


def Mahdifun(a, b):
    sum=a+b
    print(sum)

Mahdifun(20,50)
Mahdifun(40,80)
Mahdifun(80,35)
Mahdifun(20,30)
Mahdifun(70,570)
Mahdifun(550,860)




#continue and break
MahdiList=[1,2,3,4,5,6,7,8,9,10]
for x in range(len(MahdiList)):
    if x==6:
        break
    print(x)

MahdiList=[1,2,3,4,5,6,7,8,9,10]
for x in range(len(MahdiList)):
    if x==6:
        continue
    print(x)